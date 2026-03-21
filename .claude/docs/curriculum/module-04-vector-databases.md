---
last_reviewed: 2026-03-21
review_cycle: monthly
staleness_risk: high
---

# Module 04: Vector Databases

## Module Objectives

By the end of this module, learners will be able to:

- Explain why specialized vector storage is needed beyond traditional databases
- Compare index types (HNSW, IVF, flat) and their performance characteristics
- Set up and operate ChromaDB for local development and small-scale production
- Implement metadata filtering alongside vector similarity search
- Evaluate vector database options for different scale and deployment requirements

## Prerequisites

- Module 01: RAG Foundations (completed)
- Module 03: Embeddings (completed)
- Basic understanding of database concepts (CRUD operations, indexing)

### Before You Begin

Verify you're comfortable with these concepts from prior modules:

- [ ] How embeddings encode semantic meaning as high-dimensional vectors (Module 03)
- [ ] Similarity metrics: cosine similarity, Euclidean distance, dot product (Module 03)
- [ ] Batch embedding pipelines with caching and retry logic (Module 03)
- [ ] The difference between the indexing pipeline and the query pipeline (Module 01)

## Lessons

### 4.1 Vector DB Fundamentals — `core`

**Description:** Why traditional databases (PostgreSQL, MySQL, MongoDB) struggle with high-dimensional similarity search. Introduces approximate nearest neighbor (ANN) search, the curse of dimensionality, and why brute-force exact search does not scale beyond ~100K vectors. Overview of the vector database landscape: embedded (ChromaDB, FAISS), client-server (Qdrant, Milvus, Weaviate), and managed cloud (Pinecone, Qdrant Cloud).

**Key concepts:** ANN search, brute-force vs approximate, recall/speed trade-off, curse of dimensionality, embedded vs client-server vs managed deployment models.

**Duration:** 45 minutes

### 4.2 Setting Up ChromaDB — `core`

**Description:** Hands-on setup of ChromaDB as the course's primary vector store. Covers installation (`pip install chromadb`), creating and managing collections, adding documents with embeddings and metadata, persistence to disk, switching between in-memory and persistent modes, and the client/server architecture for multi-process access. ChromaDB is chosen for its simplicity and zero-config local operation.

**Key concepts:** Collections, documents, IDs, metadata, persistence directory, embedding functions, ChromaDB client modes (ephemeral, persistent, client-server).

**Duration:** 45 minutes

### 4.3 Indexing Strategies — `optional`

**Description:** Deep dive into vector index types that power fast similarity search. HNSW (the default for most databases): a graph-based algorithm where vectors are connected in a navigable small-world graph, tunable via M (connections per node) and ef (search breadth). IVF (inverted file index): partitions vectors into clusters and searches only nearby clusters, tunable via nlist and nprobe. Flat index: brute-force exact search for small datasets or ground-truth benchmarking.

**Key concepts:** HNSW graph construction, M parameter, ef_construction, ef_search, IVF partitions, nlist, nprobe, flat index, index build time vs query time trade-offs, memory usage.

**Duration:** 45 minutes

### 4.4 Querying and Filtering — `optional`

**Description:** Moving beyond simple top-k similarity retrieval. Covers metadata filtering with WHERE clauses (exact match, range, IN), combining vector similarity with metadata constraints, pre-filtering vs post-filtering strategies and their performance implications, distance thresholds for minimum relevance, and result post-processing. Demonstrates how filtering dramatically improves precision for multi-tenant or categorized data.

**Key concepts:** Pre-filtering, post-filtering, WHERE clauses, metadata schemas, distance thresholds, multi-tenancy patterns, compound queries.

**Duration:** 45 minutes

### 4.5 Scaling Vector Storage — `optional`

**Description:** Comparison of vector databases for production workloads. Pinecone (fully managed serverless, zero ops), Qdrant (self-hosted or cloud, rich filtering, named vectors), pgvector (PostgreSQL extension, familiar ops tooling), Weaviate (multi-modal, GraphQL API), Milvus (high-throughput, GPU acceleration). Covers sharding strategies, replication for availability, backup/restore procedures, migration between databases, and cost modeling at scale.

**Key concepts:** Horizontal scaling, sharding by metadata, replication, managed vs self-hosted trade-offs, cost per million vectors, migration strategies, vendor lock-in considerations.

**Duration:** 45 minutes

## Hands-On Exercises

1. **ChromaDB CRUD:** Create a collection, add 500 chunks with rich metadata (source, page, section, date), query with various filter combinations, update document metadata, delete by filter, and verify that data persists across process restarts. Write assertions for each operation.

2. **Index Tuning:** Using FAISS (or Qdrant locally), create the same 10K-vector dataset with HNSW (varying M from 8 to 64 and ef_search from 50 to 500) and IVF (varying nlist from 10 to 1000 and nprobe from 1 to 50). Benchmark query latency and recall@10 for each configuration. Plot the recall vs latency Pareto frontier.

3. **Multi-Tenant Store:** Design and implement a vector store that isolates data by tenant using metadata filtering. Load data for 3 simulated tenants. Verify with test queries that tenant A's queries never return tenant B's or C's documents.

4. **Migration Exercise:** Load 1000 chunks with metadata into ChromaDB, then export the data and load it into pgvector (using a local PostgreSQL instance). Run the same 20 test queries against both stores and compare result rankings to verify consistency.

5. **Cost Calculator:** Build a spreadsheet or Python script that estimates monthly vector database costs for a given workload: N vectors, D dimensions, Q queries/day, with pricing data for ChromaDB (self-hosted), Pinecone Serverless, Qdrant Cloud, and Supabase pgvector.

## Key Takeaways

- Vector databases solve the specific problem of fast approximate similarity search in high dimensions — they are not general-purpose databases and should be used alongside, not instead of, traditional databases.
- HNSW is the dominant index type for most use cases, offering excellent recall/speed trade-offs with tunable parameters. Start with defaults and tune only after benchmarking.
- Metadata filtering is as important as vector search itself; most real-world queries combine similarity with filters (by date, source, category, tenant).
- ChromaDB is ideal for development and prototyping; evaluate managed options (Pinecone, Qdrant Cloud) or pgvector for production deployments depending on scale and ops capacity.
- Index parameter tuning can yield 10x latency improvements with minimal recall loss — always benchmark with your actual data and query patterns.

## Suggested Reading

- ChromaDB documentation (collections, querying, deployment)
- FAISS documentation (index types and parameter tuning)
- Pinecone learning center (vector database concepts)
- pgvector GitHub README (PostgreSQL extension setup)

---

← **Previous:** [Module 03 — Embeddings](module-03-embeddings.md) | **Next:** [Module 05 — Retrieval Strategies](module-05-retrieval.md) →
