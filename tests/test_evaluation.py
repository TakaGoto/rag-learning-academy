"""
Tests for evaluation metrics.
Fill these in as you work through Module 7.
"""

import pytest


class TestRetrievalMetrics:
    """Module 7, Lesson 7.2: Retrieval Metrics"""

    def test_precision_at_k(self):
        """Precision@K should return correct value for known results."""
        # Example: 3 relevant docs in top 5 → precision = 0.6
        pytest.skip("Implement in Module 7, Lesson 7.2")

    def test_recall_at_k(self):
        """Recall@K should return correct value for known results."""
        pytest.skip("Implement in Module 7, Lesson 7.2")

    def test_mrr(self):
        """MRR should return 1/rank of first relevant result."""
        pytest.skip("Implement in Module 7, Lesson 7.2")


class TestGenerationMetrics:
    """Module 7, Lesson 7.3: Generation Metrics"""

    def test_faithfulness_score_range(self):
        """Faithfulness score should be between 0 and 1."""
        pytest.skip("Implement in Module 7, Lesson 7.3")

    def test_answer_relevancy_score_range(self):
        """Answer relevancy score should be between 0 and 1."""
        pytest.skip("Implement in Module 7, Lesson 7.3")
