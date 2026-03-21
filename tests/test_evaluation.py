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
        #
        # Fixture data:
        #   retrieved = ["a", "b", "c", "d", "e"]
        #   relevant  = ["a", "c", "f"]
        #   k = 5
        #   Hits in top 5: "a" and "c" → 2 hits
        #   Precision@5 = 2 / 5 = 0.4
        #
        # from src.evaluation.metrics import precision_at_k
        # assert precision_at_k(retrieved, relevant, k=5) == pytest.approx(0.4)
        pytest.skip("Implement in Module 7, Lesson 7.2")

    def test_recall_at_k(self):
        """Recall@K should return correct value for known results."""
        #
        # Fixture data (same sets as precision test):
        #   retrieved = ["a", "b", "c", "d", "e"]
        #   relevant  = ["a", "c", "f"]
        #   k = 5
        #   Hits in top 5: "a" and "c" → 2 hits out of 3 relevant
        #   Recall@5 = 2 / 3 ≈ 0.6667
        #
        # from src.evaluation.metrics import recall_at_k
        # assert recall_at_k(retrieved, relevant, k=5) == pytest.approx(2 / 3)
        pytest.skip("Implement in Module 7, Lesson 7.2")

    def test_mrr(self):
        """MRR should return 1/rank of first relevant result."""
        #
        # Fixture data:
        #   retrieved = ["b", "a", "c"]
        #   relevant  = {"a"}
        #   First relevant result "a" is at index 1 → rank 2
        #   MRR = 1 / 2 = 0.5
        #
        # from src.evaluation.metrics import mean_reciprocal_rank
        # assert mean_reciprocal_rank(retrieved, relevant) == pytest.approx(0.5)
        pytest.skip("Implement in Module 7, Lesson 7.2")


class TestGenerationMetrics:
    """Module 7, Lesson 7.3: Generation Metrics"""

    def test_faithfulness_score_range(self):
        """Faithfulness score should be between 0 and 1."""
        pytest.skip("Implement in Module 7, Lesson 7.3")

    def test_answer_relevancy_score_range(self):
        """Answer relevancy score should be between 0 and 1."""
        pytest.skip("Implement in Module 7, Lesson 7.3")
