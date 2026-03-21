"""
Tests for retrieval strategies.
Fill these in as you work through Module 5.
"""

import pytest


class TestDenseRetrieval:
    """Module 5, Lesson 5.1: Dense Retrieval"""

    def test_returns_top_k_results(self):
        """Retriever should return exactly k results."""
        pytest.skip("Implement in Module 5, Lesson 5.1")

    def test_results_have_scores(self):
        """Each result should include a relevance score.

        Fixture hint:
        # results = retriever.retrieve("What is chunking?", top_k=5)
        # for result in results:
        #     assert hasattr(result, "score"), "Every RetrievalResult must carry a score"
        #     assert isinstance(result.score, float)
        #     assert 0.0 <= result.score <= 1.0  # cosine similarity is in [0, 1] for normalized vecs
        """
        pytest.skip("Implement in Module 5, Lesson 5.1")

    def test_scores_are_descending(self):
        """Results should be ordered by relevance (highest first)."""
        pytest.skip("Implement in Module 5, Lesson 5.1")


class TestHybridRetrieval:
    """Module 5, Lesson 5.3: Hybrid Search"""

    def test_combines_dense_and_sparse(self):
        """Hybrid results should include contributions from both retrievers."""
        pytest.skip("Implement in Module 5, Lesson 5.3")

    def test_fusion_scoring(self):
        """Reciprocal rank fusion should produce valid fused scores."""
        pytest.skip("Implement in Module 5, Lesson 5.3")


class TestReranking:
    """Module 5, Lesson 5.4: Reranking"""

    def test_reranking_changes_order(self):
        """Cross-encoder reranking should potentially reorder initial results."""
        pytest.skip("Implement in Module 5, Lesson 5.4")

    def test_reranking_improves_precision(self):
        """Precision@K should improve after reranking on test queries."""
        pytest.skip("Implement in Module 5, Lesson 5.4")
