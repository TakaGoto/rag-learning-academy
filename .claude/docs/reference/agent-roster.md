---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# Agent Roster

Quick-reference lookup for all 20 agents. For full role details, teaching approach, and delegation rules, see individual agent files in `.claude/agents/`.

### Model Allocation

- **Tier 1 Directors** use `opus` (30 turns) — complex reasoning for curriculum planning, architecture design, and research synthesis
- **Tier 2 Leads** use `opus` (20 turns) — deep domain expertise requiring nuanced explanations
- **Tier 3 Specialists** use `sonnet` (15 turns) — focused, efficient responses for specific technical questions

### How Agents Are Invoked

Agents are **not auto-routed**. When a learner asks a question, Claude Code answers directly. If the question maps to a specialist's domain, Claude offers to bring the agent in: *"The chunking-strategist has specific guidance on this — want me to bring it in?"* The learner chooses. This keeps responses fast and avoids unnecessary token cost.

Agents also activate when invoked through skills (`/lesson`, `/build`, `/debug-rag`) or when explicitly requested by the learner.

---

## Tier 1 — Directors (3)

| Agent | When to Use | Primary Modules |
|-------|-------------|-----------------|
| `curriculum-director` | Starting a learning path, assessing level, routing to specialists | All (meta-coordination) |
| `architecture-director` | RAG system design, trade-off analysis, component integration | 01, 08, 09 |
| `research-director` | Latest papers, emerging techniques, benchmarks | All (research support), esp. 08 |

## Tier 2 — Domain Leads (5)

| Agent | When to Use | Primary Modules |
|-------|-------------|-----------------|
| `embedding-lead` | Choosing models, vector spaces, similarity metrics, MTEB, fine-tuning | 03 |
| `retrieval-lead` | Dense/sparse/hybrid search, ranking, MRR/NDCG | 05 |
| `indexing-lead` | Vector DB internals, HNSW/IVF/PQ, index tuning | 04 |
| `evaluation-lead` | Evaluation strategy, metrics, quality gates, RAGAS concepts | 07 |
| `integration-lead` | End-to-end pipelines, LangChain vs LlamaIndex, deployment | 09 |

## Tier 3 — Specialists (12)

| Agent | When to Use | Primary Modules |
|-------|-------------|-----------------|
| `chunking-strategist` | Chunking strategy, chunk size, overlap, semantic chunking | 02 |
| `vector-db-specialist` | Chroma/Pinecone/Weaviate/pgvector/Qdrant setup and queries | 04 |
| `reranking-specialist` | Cross-encoders, ColBERT, reranking pipelines | 05 |
| `prompt-engineer` | Context injection, prompt templates, few-shot, citations | 06 |
| `hybrid-search-specialist` | BM25 + dense fusion, RRF, SPLADE | 05 |
| `document-parser` | PDF/HTML/markdown parsing, table extraction, OCR | 02 |
| `metadata-specialist` | Metadata schemas, filtering, tagging taxonomies | 02, 04 |
| `query-analyst` | Query expansion, HyDE, decomposition, preprocessing | 05, 08 |
| `deployment-specialist` | Production RAG, caching, scaling, monitoring, cost | 09 |
| `evaluation-specialist` | RAGAS code, custom metrics, A/B testing, regression | 07 |
| `graph-rag-specialist` | Knowledge graphs, GraphRAG, entity extraction | 08 |
| `multimodal-specialist` | Image/table/chart RAG, vision embeddings, ColPali | 08 |

---

## Summary

| Tier | Count | Agents |
|------|-------|--------|
| Directors | 3 | curriculum-director, architecture-director, research-director |
| Domain Leads | 5 | embedding-lead, retrieval-lead, indexing-lead, evaluation-lead, integration-lead |
| Specialists | 12 | chunking-strategist, vector-db-specialist, reranking-specialist, prompt-engineer, hybrid-search-specialist, document-parser, metadata-specialist, query-analyst, deployment-specialist, evaluation-specialist, graph-rag-specialist, multimodal-specialist |
| **Total** | **20** | |

## Module Coverage

| Module | Primary Agents |
|--------|---------------|
| 01 — Foundations | curriculum-director, architecture-director |
| 02 — Document Processing | document-parser, chunking-strategist, metadata-specialist |
| 03 — Embeddings | embedding-lead |
| 04 — Vector Databases | indexing-lead, vector-db-specialist |
| 05 — Retrieval Strategies | retrieval-lead, reranking-specialist, hybrid-search-specialist, query-analyst |
| 06 — Generation | prompt-engineer |
| 07 — Evaluation | evaluation-lead, evaluation-specialist |
| 08 — Advanced Patterns | research-director, graph-rag-specialist, multimodal-specialist, query-analyst |
| 09 — Production | integration-lead, deployment-specialist |
