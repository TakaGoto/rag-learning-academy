---
last_reviewed: 2026-03-21
review_cycle: monthly
staleness_risk: high
---

# RAG Component Comparisons

Reference tables comparing popular vector databases and embedding models. Use this document to practice handling tabular data in RAG -- tables are notoriously difficult for chunking and retrieval.

---

## Vector Database Comparison

| Feature | ChromaDB | Pinecone | Qdrant | pgvector | Weaviate |
|---------|----------|----------|--------|----------|----------|
| Deployment | Embedded / Docker | Managed cloud | Self-hosted / Cloud | PostgreSQL extension | Self-hosted / Cloud |
| Max dimensions | Unlimited | 20,000 | 65,536 | 2,000 | 65,536 |
| Metadata filtering | Yes | Yes | Yes (rich filters) | Yes (SQL WHERE) | Yes (GraphQL) |
| Hybrid search | No (dense only) | Yes (sparse+dense) | Yes (sparse+dense) | BM25 via tsvector | Yes (BM25+dense) |
| Scalability | Single node | Fully managed, auto-scale | Distributed clusters | Depends on Postgres setup | Horizontal sharding |
| Best for | Prototyping, local dev | Production SaaS, zero-ops | Self-hosted production | Teams already on PostgreSQL | Multi-modal, GraphQL fans |
| Approximate cost | Free (open source) | $70/mo+ (Starter) | Free (open source) | Free (open source) | Free (open source) |

### When to choose what

- **ChromaDB**: Best starting point for learning and prototyping. Zero configuration, runs in-process.
- **Pinecone**: Best when you want fully managed infrastructure with no cluster maintenance.
- **Qdrant**: Best for self-hosted production with advanced filtering and high-performance requirements.
- **pgvector**: Best when your data is already in PostgreSQL and you want to avoid a separate system.
- **Weaviate**: Best for multi-modal search and teams that prefer GraphQL-style APIs.

## Embedding Model Comparison

| Model | Provider | Dimensions | Max tokens | MTEB Avg | Open source | Latency |
|-------|----------|------------|------------|----------|-------------|---------|
| text-embedding-3-small | OpenAI | 1,536 | 8,191 | 62.3 | No | ~20ms/query |
| text-embedding-3-large | OpenAI | 3,072 | 8,191 | 64.6 | No | ~30ms/query |
| embed-v3 | Cohere | 1,024 | 512 | 64.5 | No | ~25ms/query |
| all-MiniLM-L6-v2 | Sentence Transformers | 384 | 256 | 56.3 | Yes | ~5ms/query (local) |
| BGE-large-en-v1.5 | BAAI | 1,024 | 512 | 64.2 | Yes | ~15ms/query (local) |
| E5-mistral-7b-instruct | Microsoft | 4,096 | 32,768 | 66.6 | Yes | ~50ms/query (GPU) |

### Key trade-offs

- **API-based models** (OpenAI, Cohere): Easy to set up, consistent performance, but add latency and per-token cost. Suitable when you do not want to manage GPU infrastructure.
- **Small open-source models** (MiniLM, BGE-base): Fast local inference on CPU, lower quality. Good for prototyping or cost-sensitive workloads.
- **Large open-source models** (E5-mistral, BGE-large): Competitive with API models, but require GPU for reasonable latency. Best for production workloads where you need control over the model.
