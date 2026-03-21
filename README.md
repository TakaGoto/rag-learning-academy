# RAG Learning Academy

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/TakaGoto/rag-learning-academy/actions/workflows/ci.yml/badge.svg)](https://github.com/TakaGoto/rag-learning-academy/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/downloads/)

A structured, multi-agent learning environment for mastering Retrieval-Augmented Generation (RAG) — powered by Claude Code.

Inspired by [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios), reimagined as an interactive learning guide for RAG systems.

## What Is This?

RAG Learning Academy transforms Claude Code into a **personal RAG tutor** with 20 specialized AI agents, 17 interactive slash commands, and a 9-module curriculum that takes you from "what is RAG?" to production deployment.

Every concept is paired with a hands-on exercise. Every exercise is paired with evaluation metrics. You learn by building.

## Quick Start

```bash
git clone https://github.com/TakaGoto/rag-learning-academy.git
cd rag-learning-academy
cp .env.example .env          # Add your API keys
pip install -r requirements.txt
claude                         # Open Claude Code
# Then type: /start
```

## What's Inside

### 20 Specialist Agents

| Tier | Count | Role | Model |
|------|-------|------|-------|
| Directors | 3 | Curriculum, Architecture, Research | opus |
| Domain Leads | 5 | Embedding, Retrieval, Indexing, Evaluation, Integration | sonnet |
| Specialists | 12 | Chunking, Vector DB, Reranking, Prompt Engineering, Hybrid Search, Document Parsing, Metadata, Query Analysis, Deployment, Evaluation Metrics, Graph RAG, Multimodal | sonnet |

### 17 Slash Commands

| Command | What It Does |
|---------|-------------|
| `/start` | Assess your level, pick a learning track |
| `/lesson` | Start or continue a curriculum lesson |
| `/quiz` | Test your understanding |
| `/build` | Build a RAG component step by step |
| `/evaluate` | Run metrics on your pipeline |
| `/debug-rag` | Diagnose common RAG failures |
| `/compare` | Compare two approaches side by side |
| `/benchmark` | Benchmark pipeline performance |
| `/architecture` | Design a RAG system for a use case |
| `/paper-review` | Walk through a research paper |
| `/code-review` | Get feedback on your RAG code |
| `/glossary` | Look up RAG terminology |
| `/challenge` | Take on a hands-on challenge |
| `/explain` | Deep-dive into any concept |
| `/roadmap` | View your progress and next steps |
| `/triage` | Not sure where to go? Get routed to the right skill |
| `/audit-content` | Check materials for outdated references |

### 9-Module Curriculum

| # | Module | Lessons | Key Topics |
|---|--------|---------|------------|
| 1 | Foundations | 4 | What is RAG, architecture, RAG vs fine-tuning |
| 2 | Document Processing | 5 | Parsing, chunking strategies, metadata |
| 3 | Embeddings | 5 | Models, vector spaces, similarity, fine-tuning |
| 4 | Vector Databases | 5 | Chroma, Pinecone, pgvector, indexing |
| 5 | Retrieval Strategies | 5 | Dense, sparse, hybrid, reranking, MMR |
| 6 | Generation | 5 | Prompt engineering, grounding, citations |
| 7 | Evaluation | 5 | RAGAS, retrieval/generation metrics |
| 8 | Advanced Patterns | 5 | Agentic RAG, Graph RAG, CRAG, multimodal |
| 9 | Production | 5 | Deployment, caching, monitoring, scaling |

### 3 Guided Projects

| Level | Project | What You Build |
|-------|---------|---------------|
| Starter | Simple Q&A | Basic RAG pipeline over documents |
| Intermediate | Multi-Source Hybrid | Hybrid search + reranking + citations |
| Advanced | Agentic RAG | Self-correcting RAG with routing and tools |

## Token Usage

Total project content: **~98,000 tokens**

### By Component

| Component | Files | Est. Tokens | % of Total |
|-----------|-------|-------------|------------|
| Agents | 20 | ~34,730 | 35% |
| Curriculum | 9 | ~14,960 | 15% |
| Skills | 17 | ~16,700 | 16% |
| Reference Docs | 5 | ~12,930 | 13% |
| Rules | 7 | ~5,120 | 5% |
| Templates | 3 | ~4,480 | 5% |
| Sample Data | 6 | ~5,700 | 5% |
| Config (CLAUDE.md + settings) | 2 | ~2,090 | 2% |
| Projects + Tests | 6 | ~3,500 | 4% |
| Other (hooks, .env, etc.) | 20 | ~2,860 | 3% |

### Per Session (What Actually Gets Loaded)

Not everything loads at once. A typical session uses:

| Loaded Content | Est. Tokens |
|----------------|-------------|
| CLAUDE.md (always) | ~1,800 |
| 1 agent definition | ~1,500–2,100 |
| 1 skill prompt | ~700–1,200 |
| 1 curriculum module | ~1,200–2,000 |
| 1-2 rule files (path-scoped) | ~500–900 |
| **Typical session** | **~6,000–8,000** |

This fits comfortably in any Claude model's context window. The full ~98k project would fit entirely within Claude's 200k context if needed.

### Curriculum Modules (Individual)

| Module | Topic | Est. Tokens |
|--------|-------|-------------|
| 01 | Foundations | ~1,200 |
| 02 | Document Processing | ~1,500 |
| 03 | Embeddings | ~1,550 |
| 04 | Vector Databases | ~1,650 |
| 05 | Retrieval Strategies | ~1,700 |
| 06 | Generation | ~1,700 |
| 07 | Evaluation | ~1,670 |
| 08 | Advanced Patterns | ~1,950 |
| 09 | Production | ~2,040 |

> Token estimates use the ~4 chars/token approximation. Actual counts vary by tokenizer (cl100k_base, etc.).

## Tech Stack

| Component | Default (API) | Free/Local Alternative |
|-----------|---------------|----------------------|
| Language | Python 3.10+ | — |
| LLM | Claude (Anthropic SDK) | Ollama (llama3, mistral) |
| Embeddings | OpenAI text-embedding-3-small | all-MiniLM-L6-v2, nomic-embed-text |
| Vector DB | ChromaDB (local) | FAISS, Pinecone, pgvector, Qdrant |
| Framework | LangChain | LlamaIndex |
| Evaluation | RAGAS | Custom metrics |
| Docs | Unstructured, PyPDF | pdfplumber, BeautifulSoup |

## Project Structure

```
rag-learning-academy/
├── CLAUDE.md                    # Master config + token estimates
├── .claude/
│   ├── settings.json            # Hooks, permissions
│   ├── agents/                  # 20 specialist agents
│   ├── skills/                  # 17 slash commands
│   ├── hooks/                   # Session lifecycle scripts
│   ├── rules/                   # Path-scoped coding standards
│   └── docs/
│       ├── curriculum/          # 9-module learning path
│       ├── reference/           # Glossary, roster, standards
│       └── templates/           # Architecture, eval, project templates
├── src/                         # Your RAG code goes here
│   ├── embeddings/
│   ├── chunking/
│   ├── retrieval/
│   ├── generation/
│   ├── evaluation/
│   ├── vector_db/
│   ├── pipelines/
│   └── utils/
├── projects/                    # Guided build projects
│   ├── starter/
│   ├── intermediate/
│   └── advanced/
├── tests/                       # Test scaffolds
├── data/                        # Sample documents
└── progress/                    # Your learning progress
```

## Learning Tracks

Run `/start` and you'll be assessed into one of three tracks:

| Track | Score | Modules | For |
|-------|-------|---------|-----|
| Beginner | 0-3 | 1 → 4 | New to RAG and embeddings |
| Intermediate | 4-6 | 3 → 7 | Know the basics, want depth |
| Advanced | 7-10 | 6 → 9 | Ready for production patterns |

## Philosophy

> "Understand → Build → Evaluate → Iterate"

- Agents **teach**, they don't just code for you
- Every concept comes with a **hands-on exercise**
- Every exercise has **evaluation criteria**
- You choose your path — agents advise, you decide

## Credits

Architecture inspired by [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) by Donchitos.

## License

MIT
