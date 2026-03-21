"""
Tests for chunking strategies.
These tests serve as both validation and learning exercises.
Fill them in as you work through Module 2.
"""

import pytest


class TestFixedSizeChunking:
    """Module 2, Lesson 2.3: Fixed-Size Chunking"""

    def test_chunks_respect_max_size(self):
        """Every chunk should be <= chunk_size characters."""
        # TODO: Import your chunker and test it
        # from src.chunking.fixed import fixed_chunk
        # chunks = fixed_chunk("your text here", chunk_size=500, overlap=50)
        # for chunk in chunks:
        #     assert len(chunk.text) <= 500
        pytest.skip("Implement in Module 2, Lesson 2.3")

    def test_overlap_is_preserved(self):
        """Adjacent chunks should share overlap_size characters."""
        pytest.skip("Implement in Module 2, Lesson 2.3")

    def test_no_empty_chunks(self):
        """Chunking should never produce empty chunks."""
        pytest.skip("Implement in Module 2, Lesson 2.3")

    def test_full_text_is_covered(self):
        """Joining chunks (accounting for overlap) should reproduce the original text."""
        pytest.skip("Implement in Module 2, Lesson 2.3")


class TestRecursiveChunking:
    """Module 2, Lesson 2.4: Recursive Chunking"""

    def test_respects_paragraph_boundaries(self):
        """Chunks should prefer splitting at paragraph boundaries."""
        pytest.skip("Implement in Module 2, Lesson 2.4")

    def test_falls_back_to_sentence_split(self):
        """If a paragraph exceeds chunk_size, split at sentences."""
        pytest.skip("Implement in Module 2, Lesson 2.4")


class TestSemanticChunking:
    """Module 2, Lesson 2.5: Semantic Chunking"""

    def test_topic_change_triggers_split(self):
        """Text with distinct topics should be split at topic boundaries."""
        pytest.skip("Implement in Module 2, Lesson 2.5")
