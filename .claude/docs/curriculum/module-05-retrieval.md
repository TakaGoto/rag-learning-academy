# Module 05: Retrieval Strategies

## Module Objectives

By the end of this module, learners will be able to:

- Implement dense, sparse, and hybrid retrieval strategies from scratch
- Apply fusion algorithms (RRF, weighted combination) to merge retrieval signals
- Use reranking models to dramatically improve precision of initial retrieval
- Apply Maximal Marginal Relevance (MMR) to diversify retrieval results
- Diagnose and fix common retrieval failures using systematic analysis

## Prerequisites

- Module 03: Embeddings (completed)
- Module 04: Vector Databases (completed)
- Understanding of information retrieval basics (precision, recall)

## Lessons

### 5.1 Dense Retrieval

**Description:** Retrieval using embedding similarity — the default RAG approach and the foundation of modern semantic search. Covers how dense retrieval works (embed query, find nearest vectors), its strengths (semantic understanding, synonym handling, paraphrase matching), and its weaknesses (exact keyword matching failures, rare term blindness, out-of-distribution queries). Practical implementation patterns with vector databases.

**Key concepts:** Bi-encoder retrieval, top-k selection, semantic matching, query embedding, retrieval pipeline, query-document embedding asymmetry.

**Duration:** 45 minutes

### 5.2 BM25 and Sparse Methods

**Description:** Classic information retrieval with BM25 and TF-IDF, still highly relevant in modern RAG. Explains term frequency, inverse document frequency, and the BM25 scoring formula with its k1 and b parameters. Demonstrates when sparse methods outperform dense retrieval (exact matches, rare terms, acronyms, named entities). Implementation with rank_bm25 library and comparison with Elasticsearch.

**Key concepts:** BM25, TF-IDF, term frequency, inverse document frequency, k1 and b parameters, sparse vectors, keyword matching, lexical search, inverted index.

**Duration:** 45 minutes

### 5.3 Hybrid Search

**Description:** Combining dense and sparse retrieval to capture both semantic and lexical matches. Covers fusion algorithms: Reciprocal Rank Fusion (RRF) — merge ranked lists using reciprocal rank scores; Convex Combination — normalize and weight-average scores; Distribution-Based Score Fusion — normalize based on score distributions. Practical implementation and tuning the balance between dense and sparse signals.

**Key concepts:** Reciprocal Rank Fusion (RRF), score normalization (min-max, z-score), alpha weighting, retrieval ensemble, rank aggregation, the RRF k parameter (typically 60).

**Duration:** 45 minutes

### 5.4 Reranking with Cross-Encoders

**Description:** Using cross-encoder models to reorder initial retrieval results for dramatically higher precision. Explains why cross-encoders are more accurate than bi-encoders (they process query and document jointly, capturing token-level interactions) but too slow for first-stage retrieval (O(n) vs O(1)). Covers Cohere Rerank API, sentence-transformers cross-encoder models, ColBERT late interaction, and designing the retrieve-then-rerank pipeline with appropriate top-k at each stage.

**Key concepts:** Cross-encoder vs bi-encoder architecture, two-stage retrieval, retrieve-then-rerank pipeline, Cohere Rerank API, sentence-transformers cross-encoders, ColBERT, latency budget allocation.

**Duration:** 45 minutes

### 5.5 Retrieval Optimization

**Description:** Systematic approaches to improving retrieval quality beyond basic retrieve-and-rerank. Query expansion (add synonyms and related terms), query rewriting with LLMs (rephrase for better retrieval), HyDE (generate hypothetical answer, embed it for retrieval), parent-child chunk relationships (retrieve small chunks, return parent context), result deduplication, and MMR for diversity. Includes a diagnostic framework for identifying why retrieval is failing.

**Key concepts:** Query expansion, HyDE (Hypothetical Document Embeddings), MMR (lambda parameter), parent-document retriever, small-to-big retrieval, deduplication by content hash, retrieval failure taxonomy.

**Duration:** 60 minutes

## Hands-On Exercises

1. **Dense vs Sparse Showdown:** Run the same 50 test queries against a dense-only retriever (embedding similarity) and a BM25-only retriever. For each query, record which method returned the correct chunk in the top-5. Categorize query types where each method wins and write a 1-paragraph analysis.

2. **Hybrid Retriever:** Implement RRF-based hybrid search combining dense and BM25 retrieval. Experiment with the RRF k parameter (20, 40, 60, 100) and the alpha weight between dense and sparse scores. Demonstrate improvement over either method alone on your 50 test queries.

3. **Reranking Pipeline:** Add Cohere Rerank (or a local cross-encoder from sentence-transformers) as a second stage. Retrieve top-20 with dense search, rerank to select top-5. Measure precision@5 improvement over dense-only top-5. Time the reranking step and verify it fits within a 3-second latency budget.

4. **MMR Implementation:** Implement MMR (Maximal Marginal Relevance) from scratch using the formula: MMR = argmax[lambda * sim(d, q) - (1 - lambda) * max(sim(d, d_selected))]. Demonstrate how varying lambda from 0.0 to 1.0 in steps of 0.2 controls the relevance/diversity trade-off on a query that has many near-duplicate relevant chunks.

5. **Query Rewriting:** Use Claude or GPT-4 to rewrite 20 ambiguous or poorly-formed queries before retrieval (e.g., "how does it work" -> "how does the HNSW index algorithm perform approximate nearest neighbor search"). Compare retrieval precision@5 with and without query rewriting.

## Key Takeaways

- No single retrieval method dominates all query types — hybrid search combining dense and sparse is the production default for good reason.
- Reranking with cross-encoders is the single highest-ROI improvement you can make to a RAG system; it typically improves precision by 15-30% at modest latency cost (100-300ms).
- MMR prevents redundant context from consuming your LLM's context window with near-duplicate passages, directly improving generation quality.
- Query understanding (rewriting, expansion, HyDE) addresses the fundamental query-document vocabulary mismatch problem that pure embedding similarity cannot solve.
- Always measure retrieval quality independently from generation quality — retrieval failures are the number one cause of bad RAG answers, and fixing them is easier than fixing generation.

## Suggested Reading

- Robertson & Zaragoza, "The Probabilistic Relevance Framework: BM25 and Beyond" (2009)
- Cormack et al., "Reciprocal Rank Fusion" (2009)
- Gao et al., "Precise Zero-Shot Dense Retrieval without Relevance Labels" (HyDE paper, 2022)
- Carbonell & Goldstein, "The Use of MMR, Diversity-Based Reranking" (1998)
