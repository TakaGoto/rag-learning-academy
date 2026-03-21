---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# RAG Glossary

Comprehensive glossary of terms used throughout the RAG Learning Academy. Terms are organized alphabetically.

---

**ANN (Approximate Nearest Neighbor):** A search algorithm that finds vectors close to a query vector without exhaustively comparing every vector. Trades perfect accuracy for dramatically faster search. HNSW and IVF are common ANN algorithms.

**Answer Correctness:** An evaluation metric measuring whether the generated answer is factually correct, regardless of whether it was derived from the retrieved context.

**Answer Relevancy:** An evaluation metric measuring whether the generated answer directly addresses the user's question.

**Batch Embedding:** The practice of embedding multiple texts in a single API call to improve throughput and reduce per-request overhead.

**Bi-Encoder:** An embedding architecture that encodes queries and documents independently into vectors. Fast for retrieval (vectors are precomputed) but less accurate than cross-encoders for relevance scoring.

**BM25 (Best Matching 25):** A probabilistic ranking function used in information retrieval. Scores documents based on term frequency and inverse document frequency. The dominant sparse retrieval method. *Analogy: like a librarian who finds books by matching the exact words on their spines, ranking higher the books where those words appear prominently and unusually.*

**Chunk:** A segment of a document produced by splitting the full text. Chunks are the fundamental unit of storage and retrieval in most RAG systems. Typical sizes range from 200 to 2000 tokens.

**Chunking:** The process of dividing documents into smaller segments for embedding and retrieval. Strategies include fixed-size, recursive, and semantic chunking.

**Citation:** A reference in the generated answer pointing to the specific source chunk(s) that support a claim. Enables users to verify the answer.

**ColBERT:** A late-interaction retrieval model that encodes queries and documents into token-level embeddings, then computes similarity via MaxSim. Balances efficiency and accuracy between bi-encoders and cross-encoders.

**ColPali:** A multi-modal retrieval model that processes document page images directly (without OCR) using vision-language models, producing embeddings for visual document retrieval.

**Community Detection:** In Graph RAG, the process of identifying clusters of densely connected entities in a knowledge graph. Used to generate summaries at different levels of abstraction.

**Context Precision:** A RAGAS metric measuring what fraction of the retrieved context is actually relevant to answering the question.

**Context Recall:** A RAGAS metric measuring what fraction of the information needed to answer the question is present in the retrieved context.

**Context Stuffing:** The naive approach of inserting all retrieved chunks into the prompt without filtering or ranking. Can waste context window space and introduce noise that degrades answer quality.

**Context Window:** The maximum number of tokens an LLM can process in a single request, including system prompt, retrieved context, conversation history, and the generated response.

**Contrastive Learning:** A training paradigm where models learn by comparing positive pairs (similar items) with negative pairs (dissimilar items). Used to train embedding models.

**Corrective RAG (CRAG):** An advanced RAG pattern that evaluates retrieval quality and takes corrective action (query rewriting, web search fallback) when the initial retrieval is insufficient.

**Cosine Similarity:** A similarity metric that measures the cosine of the angle between two vectors. Ranges from -1 (opposite) to 1 (identical direction). The most commonly used metric for text embedding similarity.

**Cross-Encoder:** A model that takes a query-document pair as joint input and outputs a relevance score. More accurate than bi-encoders but too slow for first-stage retrieval. Used for reranking.

**Data Drift:** Gradual change in the distribution of queries or documents over time, which can degrade RAG system performance if not monitored and addressed.

**Dense Retrieval:** Retrieval using learned vector representations (embeddings). Captures semantic similarity, including synonyms and paraphrases, but may miss exact keyword matches.

**Dimensionality:** The number of dimensions in an embedding vector. Common values: 384, 768, 1024, 1536, 3072. Higher dimensions can capture more nuance but increase storage and computation costs.

**Dot Product (Inner Product):** A similarity metric computed as the sum of element-wise products of two vectors. Equivalent to cosine similarity when vectors are normalized.

**Embedding:** A dense vector representation of text (or other data) in a continuous vector space, where semantic similarity corresponds to geometric proximity. *Analogy: like converting words into GPS coordinates so that similar topics end up near each other on a map.*

**Embedding Cache:** A storage layer that maps text inputs to their precomputed embeddings, avoiding redundant embedding API calls.

**Entity Extraction:** The process of identifying named entities (people, organizations, concepts) from text. A key step in building knowledge graphs for Graph RAG.

**Euclidean Distance (L2):** A distance metric measuring the straight-line distance between two points in vector space. Lower values indicate greater similarity.

**Faithfulness:** An evaluation metric measuring whether every claim in the generated answer is supported by the retrieved context. A faithfulness failure indicates hallucination.

**Flat Index:** A vector index that performs exact (brute-force) nearest neighbor search by comparing the query against every stored vector. Perfect recall but O(n) complexity.

**Graph RAG:** A RAG pattern that augments vector retrieval with knowledge graph traversal. Entities and relationships extracted from documents form a graph, enabling multi-hop reasoning.

**Grounding:** The practice of ensuring an LLM's response is based on provided context rather than its parametric (training) knowledge. Reduces hallucination.

**Hallucination:** When an LLM generates information that is not supported by the provided context or is factually incorrect. A primary motivation for RAG.

**Hard Negative:** In embedding training, a negative example that is superficially similar to the positive but semantically different. Hard negatives improve embedding quality.

**HNSW (Hierarchical Navigable Small World):** A graph-based ANN index algorithm that builds a multi-layer navigable graph. The most widely used index type in modern vector databases. Tuned via M (connections per node) and ef (search breadth) parameters. *Analogy: like an express-train network where you start on a sparse high-speed layer and progressively zoom in to local stops near your destination.*

**HyDE (Hypothetical Document Embeddings):** A query strategy where the LLM generates a hypothetical answer to the query, and the embedding of that hypothetical answer is used for retrieval instead of the query embedding.

**Hybrid Search:** Combining dense (embedding-based) and sparse (keyword-based) retrieval, typically merging results with a fusion algorithm like RRF. Captures both semantic and lexical matches.

**IVF (Inverted File Index):** A partition-based ANN index that clusters vectors and searches only the nearest clusters at query time. Tuned via nlist (number of clusters) and nprobe (clusters searched).

**Knowledge Graph:** A graph structure where nodes represent entities and edges represent relationships between them. Used in Graph RAG to capture structured information from documents.

**Langfuse:** An open-source LLM observability platform for tracing, monitoring, and evaluating LLM application pipelines including RAG.

**LangSmith:** A platform by LangChain for tracing, debugging, and monitoring LLM applications.

**Lost in the Middle:** A phenomenon where LLMs pay more attention to content at the beginning and end of the context window, potentially missing information placed in the middle. *Analogy: like reading a long email — you remember the opening and closing but skim the middle paragraphs.*

**Map-Reduce:** A RAG generation pattern where each retrieved chunk is processed independently (map), then results are combined into a final answer (reduce). Useful when context exceeds the window.

**Matryoshka Embeddings:** Embedding models trained so that truncating the vector to fewer dimensions produces a valid lower-dimensional embedding. Enables flexible dimensionality/quality trade-offs.

**Metadata Filtering:** Restricting vector search results based on metadata attributes (source, date, category, author). Dramatically improves precision for scoped queries.

**MMR (Maximal Marginal Relevance):** A result selection algorithm that balances relevance to the query with diversity among selected results. Controlled by a lambda parameter (0 = max diversity, 1 = max relevance). *Analogy: like a hiring manager who picks candidates that are each strong but also bring different skills to the team.*

**MRR (Mean Reciprocal Rank):** A retrieval metric that averages the reciprocal of the rank of the first relevant result across queries. Higher is better. MRR = 1.0 means the relevant result is always first.

**MTEB (Massive Text Embedding Benchmark):** A comprehensive benchmark for evaluating embedding models across multiple tasks (retrieval, classification, clustering, etc.).

**Multi-Modal RAG:** RAG systems that handle non-text data types including images, tables, code, and audio alongside text.

**NDCG (Normalized Discounted Cumulative Gain):** A retrieval metric that evaluates ranking quality using graded relevance scores, with higher-ranked results weighted more heavily.

**Overlap:** In chunking, the number of tokens or characters shared between consecutive chunks. Prevents information loss at chunk boundaries.

**Parametric Knowledge:** Information encoded in an LLM's weights during training. Contrasted with non-parametric knowledge retrieved at query time.

**pgvector:** A PostgreSQL extension that adds vector similarity search to your existing Postgres instance. Unlike standalone vector databases (Pinecone, Qdrant), it runs inside Postgres — ideal when you already have a Postgres-backed application.

**Precision@k:** The fraction of the top-k retrieved documents that are relevant to the query.

**Prompt Compression:** Techniques for reducing the token count of context passed to the LLM while preserving relevant information. Reduces cost and latency.

**Query Decomposition:** Breaking a complex query into simpler sub-queries, retrieving for each, and combining the results.

**Query Expansion:** Adding related terms or synonyms to the original query to improve retrieval recall.

**RAGAS (Retrieval-Augmented Generation Assessment):** A framework and library for evaluating RAG pipelines. Core metrics: faithfulness, answer relevancy, context precision, context recall.

**Recall@k:** The fraction of all relevant documents that appear in the top-k retrieved results.

**Reciprocal Rank Fusion (RRF):** A rank aggregation algorithm that combines ranked lists from multiple retrievers. Each document's score is the sum of 1/(k + rank) across all lists, where k is a constant (typically 60).

**Refine:** A RAG generation pattern where the LLM generates an initial answer from the first chunk, then iteratively refines it as each subsequent chunk is processed.

**Relation Extraction:** The process of identifying relationships between entities in text (e.g., "works at", "located in"). A key step in knowledge graph construction.

**Reranking:** A second-stage retrieval step that uses a more accurate (but slower) model to reorder the initial retrieval results. Typically uses cross-encoders.

**Retriever:** The component of a RAG pipeline responsible for finding relevant documents or chunks given a query. May use dense, sparse, or hybrid methods.

**Self-RAG:** A RAG pattern where the model generates special reflection tokens to decide when to retrieve, assess retrieval relevance, and critique its own generation for faithfulness.

**Semantic Cache:** A cache that matches incoming queries against previous queries by semantic similarity (not exact match). Returns cached responses for sufficiently similar queries.

**Semantic Chunking:** A chunking strategy that uses embedding similarity between sentences to identify natural topic boundaries for splitting.

**Sentence Transformers:** An open-source Python library for computing dense vector embeddings using transformer models. A popular alternative to API-based embeddings (OpenAI, Cohere), running locally without API costs.

**SPLADE (Sparse Lexical And Expansion):** A learned sparse representation model that combines keyword matching with semantic term expansion. Outperforms BM25 on most benchmarks while maintaining the interpretability and efficiency of sparse vectors.

**Sparse Retrieval:** Retrieval using term-frequency-based representations (e.g., BM25). Excels at exact keyword matching but misses semantic relationships.

**Step-Back Prompting:** A query strategy where the LLM first identifies the broader concept behind a specific query, then retrieval is performed on the more general formulation.

**Stuff:** The simplest RAG generation pattern: concatenate all retrieved chunks into the context and send to the LLM in a single call. Works when total context fits within the window.

**Token:** The basic unit of text processing for LLMs. A token is approximately 4 characters or 0.75 words in English. Embeddings, context windows, and costs are measured in tokens.

**Tokenizer / Tokenization:** The process (and tool) that splits text into tokens. Different models use different tokenizers — OpenAI uses tiktoken (cl100k_base), while open-source models often use SentencePiece. The same text produces different token counts with different tokenizers.

**Top-k:** The number of results returned by a retrieval operation. A key hyperparameter balancing recall (more results) against precision and context window usage (fewer results).

**Two-Stage Retrieval:** A retrieval pattern where an initial fast retrieval (bi-encoder or BM25) produces a candidate set, followed by a slower but more accurate reranking step (cross-encoder). The standard approach for production RAG systems.

**Vector Database:** A specialized database optimized for storing, indexing, and querying high-dimensional vectors. Examples: ChromaDB, Pinecone, Qdrant, pgvector, Weaviate, Milvus.

**Vector Space:** A mathematical space where each point is a vector of fixed dimensionality. Text embeddings live in vector spaces where proximity corresponds to semantic similarity.

---

## Terms by Topic

Quick lookup by domain — find related terms grouped together.

### Document Processing
Chunk, Chunking, Citation, Metadata Filtering, Overlap, Semantic Chunking

### Embeddings & Vector Spaces
Batch Embedding, Bi-Encoder, Contrastive Learning, Cosine Similarity, Dense Retrieval, Dimensionality, Dot Product (Inner Product), Embedding, Embedding Cache, Euclidean Distance (L2), Hard Negative, Matryoshka Embeddings, MTEB, Sentence Transformers, Vector Space

### Retrieval
BM25, Cross-Encoder, Dense Retrieval, Hybrid Search, HyDE, MMR, Query Decomposition, Query Expansion, Reciprocal Rank Fusion (RRF), Reranking, Retriever, Sparse Retrieval, Step-Back Prompting, Top-k, Two-Stage Retrieval

### Indexing & Storage
ANN, Flat Index, HNSW, IVF, pgvector, Vector Database

### Generation & Prompting
Context Stuffing, Context Window, Grounding, Hallucination, Lost in the Middle, Map-Reduce, Parametric Knowledge, Prompt Compression, Refine, Stuff, Token, Tokenizer / Tokenization

### Evaluation
Answer Correctness, Answer Relevancy, Context Precision, Context Recall, Data Drift, Faithfulness, MRR, NDCG, Precision@k, RAGAS, Recall@k

### Advanced Patterns
ColBERT, ColPali, Community Detection, Corrective RAG (CRAG), Entity Extraction, Graph RAG, Knowledge Graph, Multi-Modal RAG, Relation Extraction, Self-RAG, SPLADE

### Infrastructure & Observability
Langfuse, LangSmith, Semantic Cache
