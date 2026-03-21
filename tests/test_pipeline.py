"""
Tests for RAG pipeline integration.
Fill these in as you work through Module 6 and Module 9.
"""

import pytest

# ---------------------------------------------------------------------------
# Mock fixtures — use these as starting points for your own tests.
# Replace with real implementations as you build out src/pipelines/.
# ---------------------------------------------------------------------------


class MockRetriever:
    """A fake retriever that returns canned results.

    Usage in tests:
        retriever = MockRetriever(results=[
            {"id": "doc-1", "score": 0.95, "text": "RAG stands for ..."},
            {"id": "doc-2", "score": 0.80, "text": "Chunking splits ..."},
        ])
        results = retriever.retrieve("What is RAG?")
        assert len(results) == 2
    """

    def __init__(self, results: list[dict] | None = None, error: Exception | None = None):
        self.results = results or []
        self.error = error
        self.last_query: str | None = None

    def retrieve(self, query: str, top_k: int = 10) -> list[dict]:
        self.last_query = query
        if self.error is not None:
            raise self.error
        return self.results[:top_k]


class MockGenerator:
    """A fake generator that returns a predetermined response.

    Usage in tests:
        generator = MockGenerator(response="Paris is the capital of France.")
        answer = generator.generate("What is the capital of France?", context="...")
        assert "Paris" in answer
    """

    def __init__(self, response: str = "Mock answer"):
        self.response = response
        self.last_query: str | None = None
        self.last_context: str | None = None

    def generate(self, query: str, context: str) -> str:
        self.last_query = query
        self.last_context = context
        return self.response


class TestPipelineIntegration:
    """Module 6 / Module 9: End-to-end pipeline tests"""

    def test_pipeline_with_mock_components_returns_string(self):
        """Pipeline.run() with mock retriever and generator should return a string response.

        Hint:
            # from src.pipelines import RAGPipeline
            # retriever = MockRetriever(results=[
            #     {"id": "doc-1", "score": 0.9, "text": "RAG combines retrieval and generation."},
            # ])
            # generator = MockGenerator(response="RAG combines retrieval and generation.")
            # pipeline = RAGPipeline(retriever=retriever, generator=generator)
            # result = pipeline.run("What is RAG?")
            # assert isinstance(result, str)
            # assert len(result) > 0
        """
        pytest.skip("Implement in Module 6 — see src/pipelines/ and pipeline-code rules")

    def test_dry_run_returns_retrieved_doc_ids(self):
        """Pipeline.run(dry_run=True) should return doc IDs without calling the generator.

        Hint:
            # retriever = MockRetriever(results=[
            #     {"id": "doc-1", "score": 0.9, "text": "..."},
            #     {"id": "doc-2", "score": 0.7, "text": "..."},
            # ])
            # generator = MockGenerator()
            # pipeline = RAGPipeline(retriever=retriever, generator=generator)
            # result = pipeline.run("test query", dry_run=True)
            # assert "retrieved_docs" in result
            # assert result["retrieved_docs"] == ["doc-1", "doc-2"]
            # assert generator.last_query is None  # generator was never called
        """
        pytest.skip("Implement in Module 6 — see pipeline-code rule #4 (dry-run mode)")

    def test_pipeline_propagates_retriever_error(self):
        """If the retriever raises an exception, the pipeline should propagate it.

        Hint:
            # retriever = MockRetriever(error=ConnectionError("Vector DB unavailable"))
            # generator = MockGenerator()
            # pipeline = RAGPipeline(retriever=retriever, generator=generator)
            # with pytest.raises(ConnectionError, match="Vector DB unavailable"):
            #     pipeline.run("any query")
        """
        pytest.skip("Implement in Module 9 — error handling in production pipelines")

    def test_pipeline_logs_each_stage(self, caplog):
        """Pipeline should emit log messages for retrieval, context building, and generation.

        Hint:
            # import logging
            # with caplog.at_level(logging.INFO):
            #     retriever = MockRetriever(results=[
            #         {"id": "doc-1", "score": 0.9, "text": "..."},
            #     ])
            #     generator = MockGenerator(response="answer")
            #     pipeline = RAGPipeline(retriever=retriever, generator=generator)
            #     pipeline.run("test query")
            #
            # log_messages = [r.message for r in caplog.records]
            # assert any("retrieval_done" in m for m in log_messages)
            # assert any("context_built" in m for m in log_messages)
            # assert any("generation_done" in m for m in log_messages)
        """
        pytest.skip("Implement in Module 9 — see pipeline-code rule #3 (logging)")
