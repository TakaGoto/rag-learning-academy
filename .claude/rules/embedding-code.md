---
path: src/embeddings/**
---

# Embedding Code Rules

## 1. Always normalize embeddings before storing

Normalized vectors ensure consistent cosine similarity comparisons. Note: some models (e.g., OpenAI's text-embedding-3-small) return pre-normalized vectors — verify your model's output. This rule applies primarily to cosine similarity indexes; inner product indexes may need unnormalized vectors.

```python
# Correct
import numpy as np

def normalize(embedding: list[float]) -> list[float]:
    vec = np.array(embedding)
    norm = np.linalg.norm(vec)
    return (vec / norm).tolist() if norm > 0 else vec.tolist()

# Incorrect - storing raw embeddings
db.insert({"embedding": raw_embedding})  # unnormalized
```

## 2. Use batch processing for >100 documents

Single-document embedding calls are wasteful at scale.

```python
# Correct
def embed_documents(texts: list[str], batch_size: int = 64) -> list[list[float]]:
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        embeddings.extend(model.encode(batch).tolist())
    return embeddings

# Incorrect - one-by-one calls
for doc in documents:
    embedding = model.encode([doc.text])  # N API calls instead of N/batch_size
```

## 3. Cache embeddings to avoid re-computation

Re-embedding the same content wastes time and API credits.

```python
# Correct
import hashlib

def get_or_compute_embedding(text: str, cache: dict) -> list[float]:
    key = hashlib.sha256(text.encode()).hexdigest()
    if key not in cache:
        cache[key] = model.encode(text)
    return cache[key]
```

## 4. Document the embedding model and dimensions

Always record which model produced the embeddings and the vector dimension.

```python
# Correct
EMBEDDING_CONFIG = {
    "model": "text-embedding-3-small",
    "dimensions": 1536,
    "provider": "openai",
    "max_input_tokens": 8191,
}
```

## 5. Handle API rate limits with exponential backoff

```python
# Correct
import time

def embed_with_retry(texts: list[str], max_retries: int = 5) -> list[list[float]]:
    for attempt in range(max_retries):
        try:
            return [e.embedding for e in client.embeddings.create(input=texts, model=MODEL).data]
        except RateLimitError:
            wait = 2 ** attempt
            time.sleep(wait)
    raise RuntimeError("Embedding API rate limit exceeded after retries")
```
