---
path: src/retrieval/**
last_reviewed: 2026-03-21
review_cycle: semi-annually
staleness_risk: low
---

# Retrieval Code Rules

## 1. Always return relevance scores with results

Scores enable downstream filtering and ranking decisions.

```python
# Correct
@dataclass
class RetrievalResult:
    document: Document
    score: float  # relevance / similarity score

def retrieve(query: str, top_k: int = 10) -> list[RetrievalResult]:
    query_embedding = embedder.embed(query)  # embed the query first
    raw = vector_db.search(query_embedding, limit=top_k)
    return [RetrievalResult(document=to_document(r), score=r.score) for r in raw]

# Incorrect - discarding scores
def retrieve(query: str) -> list[Document]:
    raw = vector_db.search(query_embedding)
    return [to_document(r) for r in raw]  # score lost
```

## 2. Implement a maximum retrieval limit (default 10)

Unbounded retrieval wastes context window and degrades generation quality.

```python
# Correct
DEFAULT_TOP_K = 10
MAX_TOP_K = 50

def retrieve(query: str, top_k: int = DEFAULT_TOP_K) -> list[RetrievalResult]:
    top_k = min(top_k, MAX_TOP_K)
    return vector_db.search(query_embedding, limit=top_k)

# Incorrect
def retrieve(query: str, top_k: int = 10000):  # no upper bound
    ...
```

## 3. Log query and result count for debugging

```python
# Correct
import logging
logger = logging.getLogger(__name__)

def retrieve(query: str, top_k: int = 10) -> list[RetrievalResult]:
    results = vector_db.search(query_embedding, limit=top_k)
    logger.info("query=%r result_count=%d top_k=%d", query[:80], len(results), top_k)
    return results
```

## 4. Use async where possible for I/O-bound operations

```python
# Correct
async def retrieve(query: str, top_k: int = 10) -> list[RetrievalResult]:
    query_embedding = await embedder.aembed(query)
    results = await vector_db.asearch(query_embedding, limit=top_k)
    return results

# Incorrect - blocking calls in an async context
async def retrieve(query: str, top_k: int = 10):
    query_embedding = embedder.embed(query)  # blocks the event loop
    ...
```

## 5. Never return raw vector DB results -- always map to document objects

Raw results leak storage details and make code fragile.

```python
# Correct
def to_document(raw: dict) -> Document:
    return Document(
        id=raw["id"],
        text=raw["metadata"]["text"],
        source=raw["metadata"]["source"],
    )

# Incorrect - passing raw Qdrant/Pinecone/Chroma result dicts to callers
return vector_db.query(embedding)["matches"]
```
