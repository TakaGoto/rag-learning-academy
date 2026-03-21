---
path: src/pipelines/**
---

# Pipeline Code Rules

## 1. All pipeline steps must be independently testable

Each step should work in isolation with mock inputs.

```python
# Correct - each component is a separate, testable unit
class RAGPipeline:
    def __init__(self, chunker, embedder, retriever, generator):
        self.chunker = chunker
        self.embedder = embedder
        self.retriever = retriever
        self.generator = generator

    def run(self, query: str) -> str:
        results = self.retriever.retrieve(query)
        context = self._format_context(results)
        return self.generator.generate(query, context)

# Each step is testable on its own:
# test_chunker(mock_doc) -> chunks
# test_retriever(mock_query) -> results

# Incorrect - monolithic function
def rag_pipeline(query):
    embedding = openai.embed(query)               # untestable without API
    results = pinecone.query(embedding)            # coupled to Pinecone
    response = openai.chat(query + str(results))   # no separation
    return response
```

## 2. Use dependency injection for components

```python
# Correct
from abc import ABC, abstractmethod

class Embedder(ABC):
    @abstractmethod
    def embed(self, text: str) -> list[float]: ...

class Retriever(ABC):
    @abstractmethod
    def retrieve(self, query: str, top_k: int = 10) -> list[RetrievalResult]: ...

class Pipeline:
    def __init__(self, embedder: Embedder, retriever: Retriever):
        self.embedder = embedder
        self.retriever = retriever

# Incorrect - hardcoded dependencies
class Pipeline:
    def __init__(self):
        self.embedder = OpenAIEmbedder("text-embedding-3-small")  # locked in
        self.retriever = PineconeRetriever("my-index")             # locked in
```

## 3. Include logging at each pipeline stage

```python
# Correct
import logging
logger = logging.getLogger(__name__)

class RAGPipeline:
    def run(self, query: str) -> str:
        logger.info("pipeline_start query=%r", query[:80])

        results = self.retriever.retrieve(query)
        logger.info("retrieval_done count=%d", len(results))

        context = self._format_context(results)
        logger.info("context_built length=%d", len(context))

        response = self.generator.generate(query, context)
        logger.info("generation_done response_length=%d", len(response))

        return response
```

## 4. Support dry-run mode for debugging

```python
# Correct
class RAGPipeline:
    def run(self, query: str, dry_run: bool = False) -> dict:
        results = self.retriever.retrieve(query)

        if dry_run:
            return {
                "query": query,
                "retrieved_docs": [r.document.id for r in results],
                "scores": [r.score for r in results],
                "context_preview": self._format_context(results)[:500],
                "would_generate": True,
            }

        context = self._format_context(results)
        return {"response": self.generator.generate(query, context)}
```

## 5. Configuration via environment variables or config files, not hardcoded

```python
# Correct — use pydantic-settings for validated, typed config from env vars
from pydantic_settings import BaseSettings

class PipelineConfig(BaseSettings):
    embedding_model: str = "text-embedding-3-small"
    top_k: int = 10
    max_context_tokens: int = 4000
    temperature: float = 0.1

    model_config = {"env_prefix": "RAG_"}  # reads RAG_EMBEDDING_MODEL, RAG_TOP_K, etc.

# Usage: config = PipelineConfig()  # auto-reads from environment, validates types

# Incorrect — hardcoded, no validation, change requires code edit
class Pipeline:
    EMBEDDING_MODEL = "text-embedding-3-small"
    TOP_K = 10
```
