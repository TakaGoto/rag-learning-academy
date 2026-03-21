# Module 03: Embeddings

## Module Objectives

By the end of this module, learners will be able to:

- Explain what embeddings are and how they encode semantic meaning in vector spaces
- Select an appropriate embedding model for a given use case, budget, and latency requirement
- Implement production-grade batch embedding pipelines with error handling and caching
- Compute and interpret similarity metrics between vectors (cosine, euclidean, dot product)
- Understand when and how to fine-tune embedding models for domain-specific applications

## Prerequisites

- Module 01: RAG Foundations (completed)
- Module 02: Document Processing (recommended)
- Basic linear algebra concepts (vectors, distance, dot product)

## Lessons

### 3.1 Understanding Vector Spaces

**Description:** Foundational lesson on how text gets mapped to high-dimensional vector spaces. Covers the intuition behind semantic similarity as geometric proximity, the evolution from word2vec through GloVe to modern transformer-based sentence embeddings, and how embedding models are trained using contrastive learning on large paired datasets.

**Key concepts:** Vector space, semantic similarity, high-dimensional geometry, contrastive learning, sentence embeddings vs word embeddings, the embedding hypothesis.

**Duration:** 45 minutes

### 3.2 Choosing an Embedding Model

**Description:** Comparative analysis of embedding models available today. OpenAI text-embedding-3-small/large, Cohere embed-v3, open-source options (BAAI/bge-base, nomic-embed-text, E5-mistral, GTE-large). Covers dimensions, max input length, MTEB benchmark performance, cost per million tokens, and inference latency. Provides a decision framework: when to use API models vs self-hosted.

**Key concepts:** MTEB leaderboard, dimensions vs quality trade-off, API vs self-hosted models, Matryoshka embeddings, multilingual support, context length limits.

**Duration:** 45 minutes

### 3.3 Batch Embedding

**Description:** Production-grade embedding pipelines for datasets of any size. Covers batching strategies (optimal batch sizes per model), rate limit handling with exponential backoff, retry logic for transient failures, progress tracking with tqdm, and embedding caching to avoid recomputation on re-runs. Includes async patterns for maximum throughput.

**Key concepts:** Batch API usage, rate limiting, exponential backoff, embedding cache (SQLite, Redis), token budgeting, async/await patterns, idempotent pipelines.

**Duration:** 45 minutes

### 3.4 Similarity Search Fundamentals

**Description:** Deep dive into similarity metrics used in vector retrieval. Cosine similarity (measures direction, ignores magnitude), Euclidean distance (measures absolute distance), and dot product (combines direction and magnitude). When to use each metric, how L2 normalization makes cosine and dot product equivalent, and practical implications for retrieval ranking. Includes geometric visualizations.

**Key concepts:** Cosine similarity, L2/Euclidean distance, inner/dot product, normalized vs unnormalized vectors, metric selection per model, similarity score interpretation.

**Duration:** 30 minutes

### 3.5 Fine-tuning Embeddings

**Description:** When off-the-shelf embeddings are not good enough for your domain. Covers creating training data from your corpus (positive pairs from co-occurring chunks, hard negatives from BM25 near-misses), fine-tuning with the sentence-transformers library, evaluating improvements on a held-out test set, and domain adaptation strategies for specialized vocabularies.

**Key concepts:** Contrastive fine-tuning, hard negative mining, training triplets/pairs, MultipleNegativesRankingLoss, domain adaptation, evaluation before/after, when fine-tuning is worth the effort.

**Duration:** 60 minutes

## Hands-On Exercises

1. **Model Shootout:** Embed the same 100 passages with 3 different embedding models (e.g., text-embedding-3-small, nomic-embed-text, bge-base). Evaluate retrieval quality on 20 test queries using MRR@10. Build a comparison table including quality, cost per 1M tokens, and latency.

2. **Similarity Explorer:** Build an interactive script that takes a query string, embeds it, and displays the top-5 most similar chunks with similarity scores for each of the three metrics (cosine, euclidean, dot product). Observe where the rankings differ and explain why.

3. **Batch Pipeline:** Implement a production-ready embedding function with: configurable batch size, exponential backoff on rate limits, a progress bar (tqdm), and a local SQLite cache that skips already-embedded chunks. Test with 1000 chunks and verify idempotency by running twice.

4. **Dimensionality Experiment:** Using OpenAI text-embedding-3-large (which supports Matryoshka truncation), compare retrieval quality at 256, 512, 1024, and 3072 dimensions on your test queries. Plot MRR@10 vs dimension count and calculate storage cost at each level.

5. **Fine-tuning Starter:** Generate 200 training pairs from a domain-specific corpus (use BM25 to find hard negatives). Fine-tune bge-base for 3 epochs. Measure retrieval MRR@10 before and after fine-tuning on 20 domain-specific queries.

## Key Takeaways

- Embeddings are the bridge between human language and machine-searchable vector space — they are the single most impactful component for RAG retrieval quality.
- Model choice matters enormously: the best open-source models now rival commercial APIs in quality, and the MTEB leaderboard is the definitive comparison resource.
- Cosine similarity is the default metric for normalized embeddings, but always verify your model's documentation for the recommended metric.
- Batch embedding with caching and retry logic is essential for any dataset beyond toy size — never re-embed what you have already embedded.
- Fine-tuning embeddings is high-effort but can yield 10-20% retrieval improvements for domain-specific applications with specialized vocabulary.

## Suggested Reading

- OpenAI Embeddings Guide (text-embedding-3 family documentation)
- Sentence-Transformers documentation (training and fine-tuning)
- MTEB leaderboard on Hugging Face (model comparison)
- Nomic AI blog posts on Matryoshka embeddings
