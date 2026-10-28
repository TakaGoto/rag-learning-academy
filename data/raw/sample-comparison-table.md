---
last_reviewed: 2026-10-28
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
| Approximate cost | Free (open source) | Free tier; usage-based paid plans | Free (open source) | Free (open source) | Free (open source) |

### When to choose what

- **ChromaDB**: Best starting point for learning and prototyping. Zero configuration, runs in-process.
- **Pinecone**: Best when you want fully managed infrastructure with no cluster maintenance.
- **Qdrant**: Best for self-hosted production with advanced filtering and high-performance requirements.
- **pgvector**: Best when your data is already in PostgreSQL and you want to avoid a separate system.
- **Weaviate**: Best for multi-modal search and teams that prefer GraphQL-style APIs.

## Embedding Model Comparison

| Model | Provider | Dimensions | Max tokens | Quality tier | Open weights | Runs on |
|-------|----------|------------|------------|--------------|--------------|---------|
| text-embedding-3-small | OpenAI | 1,536 | 8,191 | Strong | No | API |
| text-embedding-3-large | OpenAI | 3,072 (Matryoshka, truncatable) | 8,191 | Strong | No | API |
| voyage-4-large | Voyage AI (MongoDB) | 1,024 (256/512/2,048 optional) | 32K | Top | No | API |
| Cohere Embed 5 | Cohere | See model card | See model card | Strong | No | API |
| Qwen3-Embedding-8B | Qwen | See model card | See model card | Top | Yes (Apache 2.0) | Local, GPU |
| Qwen3-Embedding-0.6B | Qwen | See model card | See model card | Strong for its size | Yes (Apache 2.0) | Local, CPU or small GPU |
| EmbeddingGemma-300m | Google | See model card | See model card | Strong for its size | Yes | Local, CPU / edge |
| BGE-M3 | BAAI | See model card | See model card | Strong (dense + sparse + multi-vector) | Yes (MIT) | Local, GPU recommended |
| all-MiniLM-L6-v2 | Sentence Transformers | 384 | 256 | Baseline | Yes | Local, CPU (22M params) |

Quality tiers are rough groupings, not scores. The leaderboard is now MTEB v2, and its numbers don't line up with the old MTEB v1 scores you'll see in older blog posts. For exact rankings, check the live MTEB(eng, v2) or MTEB(Multilingual, v2) leaderboard. On the multilingual board, Microsoft's harrier-oss-v1-27b (MIT) currently leads.

### Key trade-offs

- **API-based models** (OpenAI, Voyage, Cohere): Easy to set up, consistent performance, but add latency and per-token cost. Suitable when you do not want to manage GPU infrastructure.
- **Small open-weight models** (MiniLM, EmbeddingGemma-300m, Qwen3-Embedding-0.6B): Fast local inference on CPU. MiniLM is the zero-setup teaching default, but it's far from state of the art; the newer small models close a lot of that gap. Good for prototyping, edge devices, or cost-sensitive workloads.
- **Larger open-weight models** (Qwen3-Embedding-8B, BGE-M3): Qwen3-Embedding-8B sits near the top of MTEB(eng, v2), and BGE-M3 gives you dense, sparse, and multi-vector output from one model. Plan on a GPU for reasonable latency. Best for production workloads where you need control over the model.
