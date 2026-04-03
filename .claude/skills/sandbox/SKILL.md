---
name: sandbox
description: "Spin up a minimal RAG pipeline instantly to experiment with"
---

# Sandbox: Get a Working RAG Pipeline in 5 Minutes

Scaffold a complete, minimal RAG pipeline with sample data so the learner has something running immediately. This is for experimentation, not production.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Check Environment

Read `progress/learner-profile.md` for the learner's chosen language. If no profile exists, default to Python.

Check if dependencies are installed. If not, guide the learner through setup:

**Python:**
```bash
pip install chromadb langchain sentence-transformers
```

**TypeScript:**
```bash
npm install chromadb langchain @langchain/community
```

For Go/Rust, note that setup is more manual and offer to walk through it.

## Step 2: Create the Sandbox

Create a `sandbox/` directory with three files:

### File 1: Sample Data (`sandbox/data.txt`)
A short collection of 5-10 paragraphs about a topic (e.g., coffee brewing methods, or RAG itself). Keep it under 2000 words. The data should be interesting enough that queries feel meaningful.

### File 2: The Pipeline (`sandbox/pipeline.[ext]`)
A single-file RAG pipeline that:
1. Loads the sample data
2. Chunks it (fixed-size, 200 tokens, 50 overlap)
3. Embeds chunks using a local model (all-MiniLM-L6-v2)
4. Stores in ChromaDB (in-memory)
5. Takes a query, retrieves top-3 chunks
6. Prints the retrieved chunks with similarity scores

No LLM generation step yet. Keep it simple: retrieval only.

### File 3: README (`sandbox/README.md`)
Quick instructions: how to run it, what to try, and 3 suggested experiments:
1. Try different queries and see what comes back
2. Change the chunk size and see how results change
3. Add your own data file and query it

## Step 3: Run It Together

Run the pipeline with a sample query and show the output. Walk through what happened at each step: "Here's where it chunked your data... here's the embedding step... here's what ChromaDB returned."

## Step 4: Suggest Experiments

Give the learner 3 things to try right now:

1. "Try a query where the answer spans two chunks. Notice how the pipeline only returns individual chunks."
2. "Change chunk size from 200 to 50 tokens. Run the same query. What changed?"
3. "Add a paragraph about something totally different to data.txt. Query for it. Does it retrieve correctly?"

Then suggest next steps:
- `/lesson` to understand the concepts behind what you just built
- `/break-it` to learn by debugging
- `/build` to extend this into a full pipeline with generation
