---
path: src/vector_db/**
---

# Vector DB Code Rules

## 1. Abstract vector DB operations behind a common interface

Avoid coupling application code to a specific vector DB vendor.

```python
# Correct
from abc import ABC, abstractmethod

class VectorStore(ABC):
    @abstractmethod
    def upsert(self, ids: list[str], embeddings: list[list[float]], metadata: list[dict]) -> None: ...

    @abstractmethod
    def search(self, embedding: list[float], top_k: int = 10) -> list[SearchResult]: ...

    @abstractmethod
    def delete(self, ids: list[str]) -> None: ...

class ChromaStore(VectorStore):
    """Chroma implementation."""
    ...

class QdrantStore(VectorStore):
    """Qdrant implementation."""
    ...

# Incorrect - direct vendor usage scattered through codebase
results = chromadb.Client().get_collection("docs").query(query_embeddings=[emb])
```

## 2. Support batch upsert operations

Single inserts are slow. Always provide a batch API.

```python
# Correct
def upsert_batch(
    self,
    ids: list[str],
    embeddings: list[list[float]],
    metadata: list[dict],
    batch_size: int = 100,
) -> None:
    for i in range(0, len(ids), batch_size):
        batch_ids = ids[i:i + batch_size]
        batch_embs = embeddings[i:i + batch_size]
        batch_meta = metadata[i:i + batch_size]
        self._collection.upsert(ids=batch_ids, embeddings=batch_embs, metadatas=batch_meta)

# Incorrect - inserting one at a time
for id_, emb, meta in zip(ids, embeddings, metadata):
    collection.add(ids=[id_], embeddings=[emb], metadatas=[meta])
```

## 3. Include connection pooling for production code

```python
# Correct
from contextlib import contextmanager

class VectorDBPool:
    def __init__(self, url: str, pool_size: int = 5):
        self._pool = [self._create_connection(url) for _ in range(pool_size)]

    @contextmanager
    def get_connection(self):
        conn = self._pool.pop()
        try:
            yield conn
        finally:
            self._pool.append(conn)

# Incorrect - new connection per request
def search(query):
    client = QdrantClient(url=QDRANT_URL)  # new TCP connection every time
    return client.search(...)
```

## 4. Always validate embedding dimensions match collection schema

Mismatched dimensions cause silent failures or cryptic errors.

```python
# Correct
def upsert(self, ids: list[str], embeddings: list[list[float]], **kwargs) -> None:
    if embeddings and len(embeddings[0]) != self.expected_dim:
        raise ValueError(
            f"Embedding dimension {len(embeddings[0])} does not match "
            f"collection schema ({self.expected_dim})"
        )
    self._collection.upsert(ids=ids, embeddings=embeddings, **kwargs)

# Incorrect - no dimension check, DB gives a confusing error later
self._collection.upsert(ids=ids, embeddings=embeddings)
```

## 5. Implement health checks for database connections

```python
# Correct
class VectorStore:
    def health_check(self) -> dict:
        try:
            info = self._client.get_collection(self._collection_name)
            return {
                "status": "healthy",
                "collection": self._collection_name,
                "document_count": info.count,
                "dimensions": info.config.params.vectors.size,
            }
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}

# Incorrect - no way to verify the DB is reachable before running queries
```
