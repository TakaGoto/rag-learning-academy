---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# Agent Roster

Complete listing of all 20 agents in the RAG Learning Academy, organized by tier, with roles, usage guidance, and primary module affiliations.

### Model Allocation

- **Tier 1 Directors** use `opus` (30 turns) — complex reasoning for curriculum planning, architecture design, and research synthesis
- **Tier 2 Leads** use `opus` (20 turns) — deep domain expertise requiring nuanced explanations
- **Tier 3 Specialists** use `sonnet` (15 turns) — focused, efficient responses for specific technical questions

This tiering balances depth of reasoning against response speed and cost. Directors need more turns because they coordinate across domains; specialists are scoped tightly and resolve faster.

### How Agents Are Invoked

Agents are **not auto-routed**. When a learner asks a question, Claude Code answers directly. If the question maps to a specialist's domain, Claude offers to bring the agent in: *"The chunking-strategist has specific guidance on this — want me to bring it in?"* The learner chooses. This keeps responses fast and avoids unnecessary token cost.

Agents also activate when invoked through skills (`/lesson`, `/build`, `/debug-rag`) or when explicitly requested by the learner.

---

## Tier 1 — Directors (3)

Directors coordinate the learning experience, route requests, and make strategic decisions. They do not implement solutions directly.

### 1. Curriculum Director

- **Name (YAML):** Curriculum Director
- **Model:** opus | **maxTurns:** 30
- **Role:** Oversees the RAG learning path, tracks learner progression, detects knowledge gaps, and orchestrates the overall learning experience across all agents.
- **When to use:** Starting a new learning path, assessing learner level, customizing module sequencing, detecting and addressing knowledge gaps, routing to the right specialist.
- **Primary modules:** All modules (meta-coordination, learning path management)

### 2. Architecture Director

- **Name (YAML):** Architecture Director
- **Model:** opus | **maxTurns:** 30
- **Role:** Guides RAG system design decisions, component integration, trade-off analysis, and architectural patterns for building robust retrieval-augmented generation systems.
- **When to use:** Designing a RAG architecture, evaluating trade-offs between components, choosing between system designs, scoping a capstone project, reviewing architectural decisions.
- **Primary modules:** All modules (cross-cutting architecture), especially Module 01 (Foundations), Module 08 (Advanced Patterns), Module 09 (Production)

### 3. Research Director

- **Name (YAML):** Research Director
- **Model:** opus | **maxTurns:** 30
- **Role:** Tracks the latest RAG research papers, emerging techniques, benchmark comparisons, and translates academic advances into practical learning content.
- **When to use:** Understanding a research paper, exploring emerging RAG techniques, comparing benchmarks, connecting academic concepts to practical work.
- **Primary modules:** All modules (research support), especially Module 08 (Advanced Patterns)

---

## Tier 2 — Domain Leads (5)

Domain Leads own a major area of RAG expertise. They teach strategy and theory for their domain and coordinate the specialists within it.

### 4. Embedding Lead

- **Name (YAML):** Embedding Lead
- **Model:** sonnet | **maxTurns:** 20
- **Role:** Teaches embedding models, vector space concepts, similarity metrics, dimensionality reduction, and model selection for RAG applications.
- **When to use:** Choosing an embedding model, understanding vector spaces and similarity metrics, comparing models on MTEB, fine-tuning embeddings, debugging poor embedding quality.
- **Primary modules:** Module 03 (Embeddings)

### 5. Retrieval Lead

- **Name (YAML):** Retrieval Lead
- **Model:** sonnet | **maxTurns:** 20
- **Role:** Teaches search strategies including dense, sparse, and hybrid retrieval, ranking algorithms, and retrieval optimization for RAG systems.
- **When to use:** Designing retrieval strategies, improving recall/precision, understanding dense vs sparse vs hybrid search, evaluating retrieval quality with MRR/NDCG.
- **Primary modules:** Module 05 (Retrieval Strategies)

### 6. Indexing Lead

- **Name (YAML):** Indexing Lead
- **Model:** sonnet | **maxTurns:** 20
- **Role:** Teaches vector database architecture, indexing algorithms (HNSW, IVF, PQ), storage optimization, and the internals of how vector search actually works.
- **When to use:** Understanding how vector search works internally, tuning index parameters (ef_construction, M), choosing index types, optimizing storage and query performance.
- **Primary modules:** Module 04 (Vector Databases)

### 7. Evaluation Lead

- **Name (YAML):** Evaluation Lead
- **Model:** sonnet | **maxTurns:** 20
- **Role:** Teaches RAG evaluation frameworks, metrics design, quality gates, and systematic approaches to measuring and improving RAG system performance.
- **When to use:** Designing evaluation strategy, choosing metrics, setting quality gates, planning regression testing, understanding RAGAS framework at a conceptual level.
- **Primary modules:** Module 07 (Evaluation)

### 8. Integration Lead

- **Name (YAML):** Integration Lead
- **Model:** sonnet | **maxTurns:** 20
- **Role:** Teaches end-to-end RAG pipeline construction, framework selection (LangChain vs LlamaIndex vs custom), deployment strategies, and connecting all RAG components into working systems.
- **When to use:** Building a complete RAG pipeline, choosing between LangChain/LlamaIndex/custom, wiring components together, debugging pipeline-level issues, framework comparison.
- **Primary modules:** Module 09 (Production), cross-module pipeline integration

---

## Tier 3 — Specialists (12)

Specialists provide deep, hands-on expertise in specific RAG techniques and tools. They implement, debug, and teach at the code level.

### 9. Chunking Strategist

- **Name (YAML):** Chunking Strategist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches document splitting strategies including fixed, recursive, semantic, and agentic chunking, overlap optimization, and chunk size tuning for optimal RAG performance.
- **When to use:** Choosing a chunking strategy, tuning chunk size and overlap, implementing semantic chunking, debugging retrieval problems caused by bad chunking.
- **Primary modules:** Module 02 (Document Processing)

### 10. Vector DB Specialist

- **Name (YAML):** Vector DB Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Provides hands-on guidance for working with vector databases including Chroma, Pinecone, Weaviate, pgvector, and Qdrant — setup, migration, querying, and operational best practices.
- **When to use:** Setting up a vector database, writing queries, migrating between databases, handling schema design, debugging vendor-specific API issues.
- **Primary modules:** Module 04 (Vector Databases)

### 11. Reranking Specialist

- **Name (YAML):** Reranking Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches cross-encoder reranking, ColBERT, Cohere Rerank, and reranking pipeline design for improving retrieval precision in RAG systems.
- **When to use:** Adding a reranking stage, choosing between cross-encoders and ColBERT, tuning reranking parameters, measuring reranking impact on precision.
- **Primary modules:** Module 05 (Retrieval Strategies)

### 12. Prompt Engineer

- **Name (YAML):** Prompt Engineer
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches context injection patterns, prompt templates for RAG, few-shot RAG, citation formatting, and the art of instructing LLMs to use retrieved context effectively.
- **When to use:** Designing RAG prompts, implementing citation patterns, managing context window limits, building grounded generation, troubleshooting hallucinations caused by poor prompting.
- **Primary modules:** Module 06 (Generation)

### 13. Hybrid Search Specialist

- **Name (YAML):** Hybrid Search Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches BM25 + dense retrieval fusion, reciprocal rank fusion, sparse embeddings (SPLADE), and hybrid search pipeline design for comprehensive retrieval.
- **When to use:** Implementing hybrid search, tuning BM25 + dense fusion weights, implementing reciprocal rank fusion, evaluating SPLADE, combining keyword and semantic search.
- **Primary modules:** Module 05 (Retrieval Strategies)

### 14. Document Parser

- **Name (YAML):** Document Parser
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches PDF, HTML, and markdown parsing, table extraction, OCR, multimodal document handling, and data cleaning strategies for RAG ingestion pipelines.
- **When to use:** Parsing PDFs with complex layouts, extracting tables, handling OCR, cleaning parsed text, choosing parsing tools (Unstructured, PyPDF, etc.).
- **Primary modules:** Module 02 (Document Processing)

### 15. Metadata Specialist

- **Name (YAML):** Metadata Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches metadata extraction, filtering strategies, namespace design, tagging taxonomies, and how to leverage metadata to dramatically improve RAG retrieval quality.
- **When to use:** Designing metadata schemas, implementing metadata filtering, building tagging taxonomies, using metadata to narrow search scope, automating metadata extraction.
- **Primary modules:** Module 02 (Document Processing), Module 04 (Vector Databases)

### 16. Query Analyst

- **Name (YAML):** Query Analyst
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches query understanding, expansion, decomposition, HyDE (Hypothetical Document Embeddings), step-back prompting, and query preprocessing for improved RAG retrieval.
- **When to use:** Implementing query expansion, using HyDE, decomposing complex queries, building query preprocessing pipelines, bridging the query-document gap.
- **Primary modules:** Module 05 (Retrieval Strategies), Module 08 (Advanced Patterns)

### 17. Deployment Specialist

- **Name (YAML):** Deployment Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches production RAG deployment including caching strategies, scaling patterns, monitoring, cost optimization, latency reduction, and operational best practices.
- **When to use:** Moving from prototype to production, implementing caching, setting up monitoring and observability, optimizing latency and cost, designing for scale.
- **Primary modules:** Module 09 (Production)

### 18. Evaluation Specialist

- **Name (YAML):** Evaluation Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches hands-on RAGAS implementation, custom metric design, A/B testing for RAG systems, regression detection, and continuous evaluation workflows.
- **When to use:** Writing RAGAS evaluation code, building custom metrics, setting up A/B tests, implementing regression detection pipelines, automating evaluation workflows.
- **Primary modules:** Module 07 (Evaluation)

### 19. Graph RAG Specialist

- **Name (YAML):** Graph RAG Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches knowledge graph integration with RAG, entity extraction, graph construction, GraphRAG patterns, and structured knowledge retrieval techniques.
- **When to use:** Implementing GraphRAG, building knowledge graphs from documents, entity extraction, community detection, multi-hop reasoning over structured data.
- **Primary modules:** Module 08 (Advanced Patterns)

### 20. Multimodal Specialist

- **Name (YAML):** Multimodal Specialist
- **Model:** sonnet | **maxTurns:** 15
- **Role:** Teaches image, table, and chart RAG, vision embeddings, multimodal retrieval, and techniques for building RAG systems that go beyond text.
- **When to use:** Building RAG over images/charts/tables, implementing vision embeddings (ColPali), multimodal retrieval pipelines, mixed-content document handling.
- **Primary modules:** Module 08 (Advanced Patterns)

---

## Summary

| Tier | Category | Count | Agents |
|------|----------|-------|--------|
| 1 | Directors | 3 | curriculum-director, architecture-director, research-director |
| 2 | Domain Leads | 5 | embedding-lead, retrieval-lead, indexing-lead, evaluation-lead, integration-lead |
| 3 | Specialists | 12 | chunking-strategist, vector-db-specialist, reranking-specialist, prompt-engineer, hybrid-search-specialist, document-parser, metadata-specialist, query-analyst, deployment-specialist, evaluation-specialist, graph-rag-specialist, multimodal-specialist |
| | **Total** | **20** | |

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
