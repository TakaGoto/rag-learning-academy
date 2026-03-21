---
path: src/vector_db/**
last_reviewed: 2026-03-21
review_cycle: semi-annually
staleness_risk: low
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

## 3. Include connection pooling for networked vector databases

For client-server vector databases (Qdrant, Pinecone, pgvector) — not needed for embedded ChromaDB.

```python
# Correct — thread-safe pool using queue.Queue
import queue
from contextlib import contextmanager

class VectorDBPool:
    def __init__(self, url: str, pool_size: int = 5):
        self._pool = queue.Queue(maxsize=pool_size)
        for _ in range(pool_size):
            self._pool.put(self._create_connection(url))

    @contextmanager
    def get_connection(self):
        conn = self._pool.get()  # blocks if pool is exhausted (thread-safe)
        try:
            yield conn
        finally:
            self._pool.put(conn)

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
# Correct — abstract base returns basic status, subclasses add vendor details
class VectorStore(ABC):
    def health_check(self) -> dict:
        try:
            self._ping()  # subclass implements
            return {"status": "healthy", "collection": self._collection_name}
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}

class QdrantStore(VectorStore):
    def health_check(self) -> dict:
        base = super().health_check()
        if base["status"] == "healthy":
            info = self._client.get_collection(self._collection_name)
            base["document_count"] = info.count
            base["dimensions"] = info.config.params.vectors.size  # Qdrant-specific
        return base

# Incorrect - no way to verify the DB is reachable before running queries
```
