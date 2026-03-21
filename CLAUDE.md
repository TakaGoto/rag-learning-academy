# RAG Learning Academy — Multi-Agent Learning Architecture

A structured learning environment for mastering Retrieval-Augmented Generation (RAG), powered by 20 specialized Claude Code agents, 15 interactive skills, and a 9-module curriculum.

## Philosophy

> "Understand → Build → Evaluate → Iterate"

This system teaches RAG through guided, hands-on learning. Every concept is paired with a buildable exercise. Every exercise is paired with an evaluation framework. The learner drives all decisions — agents advise, explain, and review but never auto-execute.

## Collaboration Framework

All agents follow this interaction model:

> "Question → Explanation → Options → Hands-On → Review"

- Agents explain concepts before suggesting implementations
- Code examples are always accompanied by explanations of *why*, not just *how*
- Learners choose their own path through the curriculum
- Agents adapt explanations to the learner's current level
- No code is generated without the learner understanding what it does

### Agent Suggestions

When a learner asks a question that falls within a specialist agent's domain, **answer the question directly first**, then offer to bring in the specialist for a deeper dive. Use this format:

> "For a deeper dive, the **[agent-name]** has specific guidance on [topic] — want me to bring it in?"

**When to suggest an agent:**
- The question is clearly domain-specific (chunking, reranking, graph RAG, deployment, etc.)
- The learner seems to want depth beyond a quick answer
- The agent's Common Misconceptions or reference material would add value

**When NOT to suggest an agent:**
- Simple factual questions ("what does top-k mean?")
- The learner is in the middle of a `/lesson` or `/build` flow (don't interrupt)
- The question is conversational ("thanks", "yes", "got it")
- You already suggested an agent in the last 2-3 messages (don't nag)

This keeps the UX lightweight — no extra token cost unless the learner opts in.

## Agent Hierarchy

### Tier 1 — Directors
| Agent | Domain |
|-------|--------|
| `curriculum-director` | Learning path, progression, knowledge gaps |
| `architecture-director` | RAG system design, component integration |
| `research-director` | Latest papers, techniques, benchmarks |

### Tier 2 — Domain Leads
| Agent | Domain |
|-------|--------|
| `embedding-lead` | Embedding models, vector spaces, similarity |
| `retrieval-lead` | Search strategies, ranking, hybrid approaches |
| `indexing-lead` | Vector DBs, indexing algorithms, storage |
| `evaluation-lead` | Metrics, benchmarks, quality assessment |
| `integration-lead` | End-to-end pipelines, deployment, monitoring |

### Tier 3 — Specialists
| Agent | Domain |
|-------|--------|
| `chunking-strategist` | Document splitting, overlap, semantic chunking |
| `vector-db-specialist` | Pinecone, Chroma, Weaviate, pgvector, Qdrant |
| `reranking-specialist` | Cross-encoders, ColBERT, reranking pipelines |
| `prompt-engineer` | Context injection, prompt templates, few-shot |
| `hybrid-search-specialist` | BM25 + dense, fusion algorithms, sparse vectors |
| `document-parser` | PDF, HTML, markdown, table extraction, OCR |
| `metadata-specialist` | Filtering, tagging, namespace strategies |
| `query-analyst` | Query understanding, expansion, decomposition |
| `deployment-specialist` | Production RAG, caching, scaling, monitoring |
| `evaluation-specialist` | RAGAS, custom metrics, A/B testing |
| `graph-rag-specialist` | Knowledge graphs, GraphRAG, entity extraction |
| `multimodal-specialist` | Multi-modal RAG, image/table retrieval, ColPali |

## Curriculum Modules

| # | Module | Key Topics |
|---|--------|------------|
| 1 | Foundations | What is RAG, architecture overview, when to use RAG vs fine-tuning |
| 2 | Document Processing | Parsing, cleaning, chunking strategies, metadata extraction |
| 3 | Embeddings | Models (OpenAI, Cohere, open-source), vector spaces, similarity metrics |
| 4 | Vector Databases | Chroma, Pinecone, pgvector, Qdrant — indexing and querying |
| 5 | Retrieval Strategies | Dense, sparse, hybrid, MMR, reranking |
| 6 | Generation | Prompt engineering, context window management, grounding |
| 7 | Evaluation | RAGAS, faithfulness, relevancy, answer correctness |
| 8 | Advanced Patterns | Agentic RAG, Graph RAG, multi-modal, self-RAG, CRAG |
| 9 | Production | Deployment, caching, monitoring, cost optimization, scaling |

## Learning Skills (Slash Commands)

| Command | Purpose |
|---------|---------|
| `/start` | Begin your RAG learning journey — assess level, pick a path |
| `/lesson` | Start or continue a curriculum lesson |
| `/quiz` | Test your understanding of a concept |
| `/build` | Hands-on: build a RAG component step by step |
| `/evaluate` | Evaluate your RAG pipeline with metrics |
| `/debug-rag` | Diagnose common RAG failure modes |
| `/compare` | Compare two approaches side by side |
| `/benchmark` | Benchmark your pipeline's performance |
| `/architecture` | Design a RAG architecture for a use case |
| `/paper-review` | Walk through a RAG research paper |
| `/code-review` | Get feedback on your RAG code |
| `/glossary` | Look up RAG terminology |
| `/challenge` | Take on a hands-on RAG challenge |
| `/explain` | Deep-dive explanation of any RAG concept |
| `/roadmap` | View your learning progress and next steps |
| `/triage` | Not sure where to start? Get routed to the right skill |
| `/audit-content` | Audit materials for outdated references and stale content |

## Tech Stack (Default)

- **Language:** Python 3.10+
- **Embeddings:** OpenAI `text-embedding-3-small` (API) or `all-MiniLM-L6-v2` / `nomic-embed-text` (local/free)
- **Vector DB:** ChromaDB (local dev), FAISS (low-level alternative), Pinecone/pgvector (production lessons)
- **LLM:** Claude API (via Anthropic SDK) or Ollama with local models (free, no API key needed — requires 8-16GB RAM; see quick-start for hardware guidance)
- **Framework:** LangChain or LlamaIndex (learner's choice)
- **Evaluation:** RAGAS, custom metrics
- **Document Processing:** Unstructured, PyPDF, pdfplumber, BeautifulSoup

## Directory Structure

```
rag-learning-academy/
├── CLAUDE.md                    # This file — master configuration
├── .claude/
│   ├── settings.json            # Hooks, permissions, validation
│   ├── agents/                  # 20 specialist agent definitions
│   ├── skills/                  # 17 slash command workflows
│   ├── hooks/                   # Lifecycle, validation & freshness scripts
│   ├── rules/                   # Path-scoped coding standards
│   └── docs/                    # Curriculum, templates, references
│       ├── curriculum/          # 9-module learning path
│       ├── templates/           # Project & exercise templates
│       └── reference/           # Quick-reference guides
├── src/                         # Learner's RAG code
│   ├── embeddings/              # Embedding generation & management
│   ├── chunking/                # Document chunking strategies
│   ├── retrieval/               # Retrieval & reranking logic
│   ├── generation/              # LLM prompt templates & generation
│   ├── evaluation/              # Evaluation metrics & frameworks
│   ├── vector_db/               # Vector store setup & operations
│   ├── pipelines/               # End-to-end RAG pipelines
│   └── utils/                   # Shared utilities
├── projects/                    # Guided build projects
│   ├── starter/                 # Simple Q&A over docs
│   ├── intermediate/            # Multi-source hybrid RAG
│   └── advanced/                # Agentic RAG with self-correction
├── tests/                       # Test suites for RAG components
└── data/                        # Sample documents & datasets
    ├── raw/                     # Source documents
    ├── processed/               # Chunked & cleaned documents
    └── embeddings/              # Cached embeddings
```

## Token Usage Estimates

Estimated token counts for each component, useful for context window planning. Total project content: **~98k tokens**.

### Curriculum Modules (~15k tokens total)

| Module | Topic | Est. Tokens |
|--------|-------|-------------|
| Module 01 | Foundations | ~1,200 |
| Module 02 | Document Processing | ~1,500 |
| Module 03 | Embeddings | ~1,550 |
| Module 04 | Vector Databases | ~1,650 |
| Module 05 | Retrieval Strategies | ~1,700 |
| Module 06 | Generation | ~1,700 |
| Module 07 | Evaluation | ~1,670 |
| Module 08 | Advanced Patterns | ~1,950 |
| Module 09 | Production | ~2,040 |

### Agents (~35k tokens total)

| Tier | Agents | Avg. Tokens | Total |
|------|--------|-------------|-------|
| Directors (3) | curriculum, architecture, research | ~1,570 | ~4,720 |
| Leads (5) | embedding, retrieval, indexing, evaluation, integration | ~1,630 | ~8,150 |
| Specialists (12) | chunking, vector-db, reranking, prompt, hybrid-search, document-parser, metadata, query, deployment, evaluation, graph-rag, multimodal | ~1,820 | ~21,860 |

### Skills / Slash Commands (~17k tokens total)

| Skill | Est. Tokens | | Skill | Est. Tokens |
|-------|-------------|---|-------|-------------|
| `/start` | ~720 | | `/architecture` | ~1,190 |
| `/lesson` | ~760 | | `/paper-review` | ~1,050 |
| `/quiz` | ~770 | | `/code-review` | ~1,080 |
| `/build` | ~860 | | `/glossary` | ~950 |
| `/evaluate` | ~870 | | `/challenge` | ~1,210 |
| `/debug-rag` | ~1,090 | | `/explain` | ~1,120 |
| `/compare` | ~900 | | `/roadmap` | ~1,200 |
| `/benchmark` | ~970 | | `/triage` | ~850 |
| `/audit-content` | ~1,100 | | | |

### Reference Docs (~13k tokens total)

| Document | Est. Tokens |
|----------|-------------|
| Agent Roster | ~3,050 |
| Coordination Rules | ~3,490 |
| Glossary (60+ terms) | ~3,170 |
| Coding Standards | ~2,070 |
| Quick Start | ~1,160 |

### Rules (~5k tokens total)

| Rule File | Scope | Est. Tokens |
|-----------|-------|-------------|
| pipeline-code | `src/pipelines/**` | ~910 |
| vector-db-code | `src/vector_db/**` | ~860 |
| evaluation-code | `src/evaluation/**` | ~740 |
| prompt-templates | `src/generation/**` | ~770 |
| chunking-code | `src/chunking/**` | ~710 |
| retrieval-code | `src/retrieval/**` | ~600 |
| embedding-code | `src/embeddings/**` | ~530 |

### Templates (~4.5k tokens total)

| Template | Est. Tokens |
|----------|-------------|
| Project Brief | ~1,600 |
| Evaluation Report | ~1,530 |
| RAG Architecture | ~1,350 |

### Sample Data (~2.6k tokens total)

| File | Est. Tokens |
|------|-------------|
| RAG Overview | ~930 |
| Evaluation Guide | ~880 |
| Chunking Guide | ~770 |

### Context Window Usage Per Session

A typical learning session loads:

| What's Loaded | Est. Tokens | Notes |
|---------------|-------------|-------|
| CLAUDE.md | ~1,800 | Always loaded |
| settings.json | ~270 | Always loaded |
| 1 agent definition | ~1,500–2,100 | Per active agent |
| 1 skill prompt | ~700–1,200 | Per slash command |
| 1 curriculum module | ~1,200–2,000 | Per lesson |
| 1-2 rule files | ~500–900 | Path-scoped, auto-loaded |
| **Typical session total** | **~6,000–8,300** | Fits easily in any model's context |

> **Note:** Token estimates use the ~4 chars/token approximation. Actual counts vary by tokenizer. The full project (~98k tokens) fits within Claude's 200k context window, but in practice only relevant files are loaded per session.

## Getting Started

Run `/start` to begin your RAG learning journey. The curriculum director will assess your current knowledge level and recommend a personalized learning path.

Not sure where to go? Run `/triage` to get routed to the right skill based on your current needs.

## Content Freshness

Academy materials are monitored for staleness via:
- **Session hook:** `check-freshness.sh` warns on startup if content files haven't been updated in 90+ days
- **On-demand audit:** Run `/audit-content` to scan for deprecated models, outdated libraries, and stale references
- **CI pipeline:** Monthly GitHub Actions workflow creates issues for stale content
- **Research director:** Extended with content currency auditing responsibilities

## Resource References

- Curriculum details: `.claude/docs/curriculum/`
- Agent roster: `.claude/docs/reference/agent-roster.md`
- Coding standards: `.claude/docs/reference/coding-standards.md`
- Coordination rules: `.claude/docs/reference/coordination-rules.md`
