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
        #
        # Sample text (560 chars — forces at least 2 chunks at size=500):
        # sample_text = (
        #     "Retrieval-Augmented Generation enhances LLMs by providing relevant "
        #     "external information at inference time. Instead of relying solely on "
        #     "parametric knowledge, RAG retrieves documents from a knowledge base "
        #     "and includes them in the prompt. This reduces hallucination and keeps "
        #     "answers grounded in source material. The technique is especially "
        #     "useful for domain-specific applications where the model has limited "
        #     "training data. A typical pipeline has two phases: an offline indexing "
        #     "phase that chunks, embeds, and stores documents, and an online query "
        #     "phase that retrieves and generates."
        # )
        #
        # chunks = fixed_chunk(sample_text, chunk_size=500, overlap=50)
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
        """Joining chunks (accounting for overlap) should reproduce the original text.

        How to verify with overlap:
        # Given chunk_size=100 and overlap=20, consecutive chunks share 20 chars.
        # To reconstruct, take the full first chunk, then append only the
        # non-overlapping tail of each subsequent chunk:
        #
        #   reconstructed = chunks[0].text
        #   for chunk in chunks[1:]:
        #       reconstructed += chunk.text[overlap:]
        #
        #   assert reconstructed == original_text
        #
        # This confirms no characters were lost or duplicated beyond the
        # expected overlap region.
        """
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
