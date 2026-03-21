# Coding Standards for RAG Projects

Python coding standards and best practices for all code written within the RAG Learning Academy.

## Python Version and Style

- **Minimum Python version:** 3.10+
- **Formatter:** ruff format (or black as fallback)
- **Linter:** ruff check
- **Line length:** 100 characters maximum
- **Import ordering:** standard library, third-party, local (enforced by ruff isort)

## Type Hints

All functions must include type hints for parameters and return values.

```python
# Good
def chunk_text(text: str, chunk_size: int = 512, overlap: int = 50) -> list[str]:
    ...

# Good — complex types
def embed_documents(
    documents: list[str],
    model: str = "text-embedding-3-small",
    batch_size: int = 100,
) -> list[list[float]]:
    ...

# Bad — no type hints
def chunk_text(text, chunk_size=512, overlap=50):
    ...
```

Use `TypeAlias` or `type` (Python 3.12+) for complex types:

```python
from typing import TypeAlias

Embedding: TypeAlias = list[float]
Chunk: TypeAlias = dict[str, str | dict[str, str]]
RetrievalResult: TypeAlias = list[tuple[str, float]]  # (text, score)
```

## Docstrings

Use Google-style docstrings for all public functions and classes.

```python
def retrieve(
    query: str,
    top_k: int = 5,
    filter_metadata: dict[str, str] | None = None,
) -> list[RetrievalResult]:
    """Retrieve the most relevant chunks for a query.

    Performs dense retrieval using cosine similarity against the
    configured vector store. Supports optional metadata filtering.

    Args:
        query: The user's search query.
        top_k: Number of results to return.
        filter_metadata: Optional metadata filters as key-value pairs.

    Returns:
        List of (chunk_text, similarity_score) tuples, sorted by
        descending relevance.

    Raises:
        VectorStoreError: If the vector store is unreachable.
        EmbeddingError: If the embedding API call fails.
    """
```

## Error Handling

### Custom Exception Hierarchy

Define a project-level exception hierarchy:

```python
class RAGError(Exception):
    """Base exception for all RAG pipeline errors."""

class DocumentParsingError(RAGError):
    """Raised when a document cannot be parsed."""

class EmbeddingError(RAGError):
    """Raised when embedding generation fails."""

class RetrievalError(RAGError):
    """Raised when retrieval from the vector store fails."""

class GenerationError(RAGError):
    """Raised when LLM generation fails."""
```

### Error Handling Rules

1. **Catch specific exceptions**, never bare `except:` or `except Exception:`
2. **Always include context** in error messages (document name, chunk index, query text)
3. **Use retry logic** for transient failures (API rate limits, network errors)
4. **Log errors with structured data** before re-raising
5. **Fail fast on configuration errors** (missing API keys, invalid model names)

```python
# Good
try:
    embeddings = await client.embed(texts, model=model)
except openai.RateLimitError as e:
    logger.warning("Rate limited, retrying", extra={"batch_size": len(texts)})
    await asyncio.sleep(e.retry_after or 1.0)
    embeddings = await client.embed(texts, model=model)
except openai.APIError as e:
    raise EmbeddingError(f"Embedding failed for batch of {len(texts)} texts") from e
```

## Async Patterns

Use async/await for I/O-bound operations (API calls, database queries, file I/O).

```python
import asyncio
from typing import AsyncIterator

async def embed_batch(
    texts: list[str],
    batch_size: int = 100,
) -> list[Embedding]:
    """Embed texts in batches with concurrency control."""
    semaphore = asyncio.Semaphore(5)  # Max 5 concurrent API calls
    results: list[Embedding] = []

    async def _embed_one_batch(batch: list[str]) -> list[Embedding]:
        async with semaphore:
            return await embedding_client.embed(batch)

    tasks = [
        _embed_one_batch(texts[i:i + batch_size])
        for i in range(0, len(texts), batch_size)
    ]
    batched_results = await asyncio.gather(*tasks)
    for batch_result in batched_results:
        results.extend(batch_result)
    return results
```

### Async Rules

1. **Use `asyncio.gather`** for concurrent independent operations
2. **Use semaphores** to limit concurrent API calls and respect rate limits
3. **Prefer async context managers** for resource cleanup
4. **Never mix sync and async** — use `asyncio.to_thread` for sync libraries in async code

## Testing Requirements

### Test Structure

```
tests/
  test_chunking.py        # Unit tests for chunking strategies
  test_retrieval.py       # Unit tests for retrieval logic
  test_evaluation.py      # Unit tests for evaluation metrics
  conftest.py             # Shared fixtures
```

### Testing Rules

1. **Minimum coverage:** 80% for all pipeline components
2. **Use pytest** as the test framework
3. **Mock external APIs** (OpenAI, Cohere, vector databases) in unit tests
4. **Use fixtures** for shared test data (sample documents, embeddings, chunks)
5. **Integration tests** must use a real (local) vector database, not mocks
6. **Test edge cases:** empty input, single character, maximum length, unicode, malformed data

```python
import pytest
from unittest.mock import AsyncMock

@pytest.fixture
def sample_chunks() -> list[str]:
    return [
        "RAG combines retrieval with generation.",
        "Vector databases store embeddings for fast similarity search.",
        "Chunking strategies affect retrieval quality.",
    ]

@pytest.mark.asyncio
async def test_embed_batch_respects_batch_size(sample_chunks: list[str]) -> None:
    mock_client = AsyncMock()
    mock_client.embed.return_value = [[0.1] * 1536] * 2

    result = await embed_batch(sample_chunks, batch_size=2, client=mock_client)

    assert mock_client.embed.call_count == 2  # 3 chunks / batch_size 2 = 2 calls
    assert len(result) == 3
```

## Configuration

Use Pydantic Settings for configuration management:

```python
from pydantic_settings import BaseSettings

class RAGConfig(BaseSettings):
    embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536
    chunk_size: int = 512
    chunk_overlap: int = 50
    top_k: int = 5
    vector_db_path: str = "./chroma_db"
    openai_api_key: str  # Required, no default

    model_config = {"env_prefix": "RAG_"}
```

## Logging

Use structured logging with `structlog` or standard library `logging` with JSON formatting:

```python
import structlog

logger = structlog.get_logger()

logger.info(
    "retrieval_complete",
    query=query[:100],
    results_count=len(results),
    top_score=results[0].score if results else None,
    latency_ms=elapsed_ms,
)
```

## File and Module Organization

```
src/
  embeddings/             # Embedding generation & management
    client.py             # Embedding API client
    cache.py              # Embedding cache
  chunking/               # Document chunking strategies
    chunker.py            # Chunking implementations
    splitters.py          # Text splitting utilities
  retrieval/              # Retrieval & reranking logic
    dense.py              # Dense retrieval
    sparse.py             # BM25 / sparse retrieval
    hybrid.py             # Hybrid search + fusion
    reranker.py           # Cross-encoder reranking
  generation/             # LLM prompt templates & generation
    prompt.py             # Prompt templates
    generator.py          # LLM generation
    citation.py           # Citation extraction
  evaluation/             # Evaluation metrics & frameworks
    metrics.py            # Metric computation
    dataset.py            # Test dataset management
  vector_db/              # Vector store setup & operations
    base.py               # Abstract vector store interface
    chroma.py             # ChromaDB implementation
    pgvector.py           # pgvector implementation
  pipelines/              # End-to-end RAG pipelines
    config.py             # RAGConfig and settings
    exceptions.py         # Custom exception hierarchy
    pipeline.py           # Pipeline orchestration
  utils/                  # Shared utilities
    tokenizer.py          # Token counting helpers
    logging.py            # Structured logging setup
```
