# RAG Learning Academy

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/TakaGoto/rag-learning-academy/actions/workflows/ci.yml/badge.svg)](https://github.com/TakaGoto/rag-learning-academy/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/downloads/)

A structured, multi-agent learning environment for mastering Retrieval-Augmented Generation (RAG) — powered by Claude Code.

Inspired by [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios), reimagined as an interactive learning guide for RAG systems.

<p align="center">
  <img src="assets/demo.gif" alt="RAG Learning Academy demo" width="720">
</p>

## What Is This?

RAG Learning Academy transforms Claude Code into a **personal RAG tutor** with 20 specialized AI agents, 22 interactive slash commands, and a 9-module curriculum that takes you from "what is RAG?" to production deployment.

Every concept is paired with a hands-on exercise. Every exercise is paired with evaluation metrics. You learn by building.

## Quick Start

```bash
git clone https://github.com/TakaGoto/rag-learning-academy.git
cd rag-learning-academy
claude                         # Open Claude Code
/start                         # Begin your learning journey
```

That's it. No API keys, no `pip install`, no setup. Dependencies get installed when you need them (the first hands-on lesson will guide you).

## What's Inside

### 20 Specialist Agents

Agents don't auto-route — they answer directly when asked, and Claude will suggest the right specialist when a question goes deep into their domain.

| Tier | Count | Role | Model |
|------|-------|------|-------|
| Directors | 3 | Curriculum, Architecture, Research | opus |
| Domain Leads | 5 | Embedding, Retrieval, Indexing, Evaluation, Integration | opus |
| Specialists | 12 | Chunking, Vector DB, Reranking, Prompt Engineering, Hybrid Search, Document Parsing, Metadata, Query Analysis, Deployment, Evaluation Metrics, Graph RAG, Multimodal | sonnet |

### 22 Slash Commands

| Command | What It Does |
|---------|-------------|
| `/start` | Assess your level, pick a track, get a working pipeline |
| `/lesson` | Start or continue a lesson (checkpoint quizzes between modules) |
| `/quiz` | Test your understanding |
| `/build` | Build a RAG component step by step |
| `/evaluate` | Run metrics on your pipeline |
| `/debug-rag` | Diagnose common RAG failures |
| `/compare` | Compare two approaches with live side-by-side output diffs |
| `/benchmark` | Benchmark pipeline performance |
| `/architecture` | Design a RAG system for a use case |
| `/paper-review` | Walk through a research paper |
| `/code-review` | Get feedback on your RAG code |
| `/glossary` | Look up RAG terminology |
| `/challenge` | Take on a hands-on challenge |
| `/explain` | Deep-dive into any concept (supports ELI5 mode) |
| `/roadmap` | View progress, badges, streaks, and export GitHub badges |
| `/triage` | Not sure where to go? Get routed to the right skill |
| `/audit-content` | Check materials for outdated references |
| `/recap` | Quick summary of what you covered last session |
| `/sandbox` | Spin up a minimal RAG pipeline instantly |
| `/break-it` | Learn by debugging intentionally broken pipelines |
| `/fix` | Skip the teaching, diagnose and fix your pipeline |
| `/journal` | Write notes about what clicked or confused you |

### 9-Module Curriculum

Each lesson is tagged `core` or `optional`. The core path (~8.5 hours) gets you to a working, evaluated RAG system. Optional lessons add depth when you're ready.

| # | Module | Lessons | Core | Key Topics |
|---|--------|---------|------|------------|
| 1 | Foundations | 4 | 4 | What is RAG, architecture, RAG vs fine-tuning |
| 2 | Document Processing | 5 | 2 | Parsing, chunking strategies, metadata |
| 3 | Embeddings | 5 | 2 | Models, vector spaces, similarity, fine-tuning |
| 4 | Vector Databases | 5 | 2 | Chroma, Pinecone, pgvector, indexing |
| 5 | Retrieval Strategies | 5 | 1 | Dense, sparse, hybrid, reranking, MMR |
| 6 | Generation | 5 | 2 | Prompt engineering, grounding, citations |
| 7 | Evaluation | 5 | 2 | RAGAS, retrieval/generation metrics |
| 8 | Advanced Patterns | 5 | 0 | Agentic RAG, Graph RAG, CRAG, multimodal |
| 9 | Production | 5 | 0 | Deployment, caching, monitoring, scaling |

**Core path: ~8.5 hours** | Full curriculum: ~31 hours

### 8 Milestones + 4 Proficiency Levels

The curriculum is broken into milestones — concrete checkpoints that mark real capability, not just lessons read.

| # | Milestone | You Can Now... |
|---|-----------|---------------|
| 1 | First Light | Build a working RAG system from scratch |
| 2 | Data Wrangler | Turn any document into retrieval-ready chunks |
| 3 | Vector Navigator | Store and search embeddings effectively |
| 4 | Retrieval Engineer | Find the right information for any query |
| 5 | Prompt Architect | Generate grounded, cited answers |
| 6 | Quality Guardian | Measure everything and improve with data |
| 7 | Pattern Master | Go beyond basic RAG when it's warranted |
| 8 | Production Ready | Deploy, monitor, and scale a RAG system |

Complete milestones to earn proficiency levels:

| Level | Milestones | What It Means |
|-------|-----------|---------------|
| **RAG Explorer** | 1-2 | Can build a basic pipeline and process documents |
| **RAG Practitioner** | 3-5 | Can design retrieval systems with proper search and prompting |
| **RAG Engineer** | 6-7 | Can evaluate, optimize, and apply advanced patterns |
| **RAG Architect** | 8 + bonus | Can deploy, scale, and maintain production systems |

See [milestones.md](.claude/docs/reference/milestones.md) for full requirements and bonus milestones.

### 3 Guided Projects

| Level | Project | What You Build |
|-------|---------|---------------|
| Starter | Simple Q&A | Basic RAG pipeline over documents |
| Intermediate | Multi-Source Hybrid | Hybrid search + reranking + citations |
| Advanced | Agentic RAG | Self-correcting RAG with routing and tools |

### Progress Dashboard

Run `make dashboard` to generate an HTML progress page showing your milestones, proficiency level, module completion, and quiz scores.

## Tech Stack

No API keys required to start. The defaults work out of the box:

| Component | Default (zero config) | Optional Upgrade |
|-----------|----------------------|-----------------|
| LLM | Claude Code (you're already running it) | Ollama (local, needs 8-16GB RAM) |
| Embeddings | all-MiniLM-L6-v2 (local, no key) | OpenAI text-embedding-3-small |
| Vector DB | ChromaDB (local, no setup) | Pinecone, pgvector, Qdrant |
| Framework | LangChain | LlamaIndex |
| Evaluation | RAGAS | Custom metrics |
| Docs | PyPDF, BeautifulSoup | Unstructured, pdfplumber |

> **Running models locally?** Ollama is free but needs 8-16GB RAM for LLMs. Close heavy apps before running. If your machine slows down, switch to the API path. Local embedding models (all-MiniLM-L6-v2) are lightweight and run fine on most machines.

## Project Structure

```
rag-learning-academy/
├── CLAUDE.md                    # Master config, voice & tone, agent behavior
├── .claude/
│   ├── settings.json            # Hooks, permissions
│   ├── agents/                  # 20 specialist agents
│   ├── skills/                  # 22 slash commands
│   ├── hooks/                   # Freshness checks, validation scripts
│   ├── rules/                   # Path-scoped coding standards
│   └── docs/
│       ├── curriculum/          # 9-module learning path (core/optional tagged)
│       ├── reference/           # Glossary, roster, milestones, standards
│       └── templates/           # Architecture, eval, project templates
├── src/                         # Your RAG code goes here
├── scripts/                     # Dashboard generator, utilities
├── projects/                    # Guided build projects
├── tests/                       # 616 structural + content tests
├── data/                        # Sample documents (6 files incl. 1,247-line chunking doc)
└── progress/                    # Your learning progress + dashboard
```

## Learning Tracks

Run `/start` and you'll be assessed into one of three tracks:

| Track | Score | Modules | Level Earned | Est. Hours |
|-------|-------|---------|-------------|------------|
| Beginner | 0-3 | 1 → 4 | RAG Explorer | 15-25 |
| Intermediate | 4-6 | 3 → 7 | RAG Practitioner | 25-40 |
| Advanced | 7-10 | 6 → 9 | RAG Engineer | 30-45 |

Not sure where to go? Run `/triage` to get routed based on your situation.

## Content Freshness

Academy materials are actively monitored so nothing goes stale:

- **Weekly CI** — checks PyPI versions, deprecated patterns, MTEB model health, review cycles ([details](.github/workflows/weekly-knowledge-check.yml))
- **Monthly CI** — content age report, creates GitHub issues for stale files
- **On-demand** — run `/audit-content` for a deep review with web search verification
- **Frontmatter** — every content file has `last_reviewed`, `review_cycle`, and `staleness_risk` metadata

## Philosophy

> "Understand → Build → Evaluate → Iterate"

- Agents **teach**, they don't just code for you
- Every concept comes with a **hands-on exercise**
- Every exercise has **evaluation criteria**
- You choose your path — agents advise, you decide
- The tone is conversational and direct — like learning from a smart friend, not reading a textbook

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Reporting bugs and requesting features
- Development setup and running tests (`make ci`)
- Pull request process and checklist
- Content guidelines and voice & tone

```bash
make ci    # Run lint + shellcheck + 616 tests before submitting a PR
```

## Credits

Architecture inspired by [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) by Donchitos.

## License

[MIT](LICENSE)
