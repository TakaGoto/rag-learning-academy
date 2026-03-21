---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# RAG Learning Academy — Quick Start Guide

Get up and running in 5 minutes.

## Prerequisites

Before starting, ensure you have:

- **Python 3.10+** installed (`python --version` to check)
- **Claude Code** installed — this is your LLM (no separate API key needed beyond your Claude subscription)
- **Git** for version control
- **A terminal** with bash or zsh

**No API keys are required to start.** The academy works out of the box using:
- **Claude Code** for LLM generation (you're already running it)
- **all-MiniLM-L6-v2** for embeddings (runs locally, downloads automatically, lightweight)
- **ChromaDB** for vector storage (runs locally, no setup)

Optional upgrades (add later if you want):
- **OpenAI API key** — for `text-embedding-3-small` embeddings (higher quality, costs ~$0.02/million tokens)
- **Cohere API key** — for reranking exercises in Module 05
- **Ollama** — for running local LLMs instead of Claude (`ollama pull llama3`). See hardware warning below.
- **uv** — for fast Python package management (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

> **Local LLM warning (Ollama):** Running LLMs locally is free but resource-intensive. A 7B parameter model needs ~4-8GB of RAM. If you're on a laptop with 8GB RAM, close heavy applications before running. Signs of trouble: system slowdown, spinning fans, or crashes. The default path (Claude Code + local embeddings) avoids this entirely.

## Setup

### Step 1: Clone and Enter the Project

```bash
git clone <repository-url> rag-learning-academy
cd rag-learning-academy
```

### Step 2: Create a Virtual Environment

Using uv (recommended):
```bash
uv venv
source .venv/bin/activate
```

Using standard Python:
```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
uv pip install -r requirements.txt
# or
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import chromadb; import sentence_transformers; print('Setup complete!')"
```

### Step 5 (Optional): Add API Keys

Only needed if you want to use OpenAI embeddings or Cohere reranking:

```bash
cp .env.example .env
# Edit .env and add keys — or skip this entirely and use the free defaults
```

## Your First Command: `/start`

Run the `/start` command to begin your learning journey. This will:

1. **Assess your current knowledge** — A brief series of questions to determine your starting point
2. **Recommend a learning path** — Based on your experience, you may skip foundational modules
3. **Set up your workspace** — Create project directories for exercises and capstone work
4. **Launch Module 01** — Begin with RAG Foundations (or your recommended starting point)

## What to Expect

### Learning Flow

Each module follows this pattern:

1. **Concept Introduction** — The relevant specialist agent explains the topic with examples
2. **Guided Implementation** — Step-by-step coding with the Exercise Coach
3. **Hands-On Exercises** — Independent practice with hints available on request
4. **Code Review** — The Code Review Agent evaluates your implementation
5. **Knowledge Check** — Quick assessment before moving to the next module

### Agent Interactions

You will interact with specialized agents throughout the course:

- **Specialists** teach and guide you through their domain (one per pipeline stage)
- **The Exercise Coach** helps when you are stuck without giving away answers
- **The Debug Agent** helps diagnose issues in your code
- **The Concept Explainer** provides alternative explanations when something is unclear

You can request a specific agent at any time by name.

### Time Estimates

| Module | Estimated Time |
|---|---|
| 01: RAG Foundations | 2-3 hours |
| 02: Document Processing | 3-4 hours |
| 03: Embeddings | 3-4 hours |
| 04: Vector Databases | 3-4 hours |
| 05: Retrieval Strategies | 4-5 hours |
| 06: Generation | 3-4 hours |
| 07: Evaluation | 3-4 hours |
| 08: Advanced Patterns | 5-6 hours |
| 09: Production RAG | 4-5 hours |
| **Total** | **30-39 hours** |

### Key Commands

| Command | Description |
|---|---|
| `/start` | Begin or resume your learning journey |
| `/roadmap` | See your current progress across all modules |
| `/code-review` | Request a code review of your current work |
| `/explain <concept>` | Get a detailed explanation or hint for a RAG concept |
| `/glossary <term>` | Look up RAG terminology |
| `/debug-rag` | Diagnose common RAG failure modes and debug issues |

## Troubleshooting

**"ModuleNotFoundError"** — Ensure your virtual environment is activated and dependencies are installed.

**"OPENAI_API_KEY not set"** — You're using code that expects OpenAI embeddings. Either add the key to `.env`, or switch to local embeddings (`all-MiniLM-L6-v2`) which need no key.

**"ChromaDB connection error"** — ChromaDB runs in embedded mode by default. Ensure you have write permissions to the project directory.

**Slow embedding operations** — Local embedding models are slower than API-based ones on first run (model download). Subsequent runs are fast. For large batches, consider using OpenAI's API.

## Next Steps

After completing the quick start:

1. Run `/start` to begin the assessment and get your personalized learning path
2. Work through Module 01 to build your first RAG pipeline
3. Proceed sequentially through modules, or follow your customized path
4. Build a capstone project in Modules 08-09 to apply everything you have learned
