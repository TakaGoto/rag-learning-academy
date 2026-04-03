---
name: start
description: "Begin your RAG learning journey — assess your level and pick a learning path"
---

# Start: Begin Your RAG Learning Journey

## Step 0: Welcome & Context

Before anything else, give a clear, casual picture of what they're about to learn. Follow the project's voice & tone (see CLAUDE.md) — conversational, direct, like a smart friend explaining something cool:

> Here's the short version: LLMs are smart but they don't know anything about *your* data. RAG fixes that. You grab relevant documents, stuff them into the prompt, and suddenly the model can answer questions about your PDFs, your codebase, your product docs — accurately, with sources.
>
> By the end of this, you'll be able to build that system yourself. Not just follow a tutorial — actually understand every piece well enough to debug it when things go wrong (and they will).

Briefly explain the learning structure: 9 modules, 3 guided projects, 17 slash commands. They'll learn by building, not just reading.

Mention the two paths: **API path** (OpenAI + Anthropic keys, computation in the cloud) or **local/free path** (Ollama, no cost but needs hardware). If they plan to use local models, add this note:

> **Heads up:** Running LLMs locally with Ollama needs 8-16GB of free RAM. If your machine has 8GB total, close heavy apps (browsers, Docker, IDEs) before running models. If you hit slowdowns or crashes, switch to the API path — local embedding models are lightweight but local LLMs are demanding. You can always mix: use local embeddings with a cloud LLM.

## Step 1: Choose Your Programming Language

Present the language options. Wait for the learner to choose before continuing.

> **What language do you want to code in?**
>
> 1. **Python** (default) — Best RAG ecosystem. LangChain, LlamaIndex, ChromaDB, RAGAS, sentence-transformers all native. Every exercise works out of the box.
>
> 2. **TypeScript** — Solid ecosystem. LangChain.js, ChromaDB client, OpenAI SDK. Most exercises translate directly; a few evaluation tools (RAGAS) need a Python fallback or manual implementation.
>
> 3. **Go** — Limited RAG tooling. No LangChain equivalent — you'll build more from scratch, which means you'll learn the internals deeply. Some exercises need adaptation.
>
> 4. **Rust** — Very limited RAG tooling. qdrant-client exists, but most RAG libraries are Python/TS. Recommended only if you're already fluent in Rust and want the challenge.
>
> Not sure? Pick Python — you can always switch later by editing your profile.

Default to Python if they skip or say "whatever."

## Step 2: Choose Your Track

Present the three tracks and let the learner self-select. Also offer the assessment as an option for those who aren't sure. Wait for the learner to choose before continuing.

> **Pick your track:**
>
> 1. **Beginner** — Start from scratch. What RAG is, document processing, embeddings, your first retrieval pipeline. Lots of guided examples. *(Modules 1–4)*
>
> 2. **Intermediate** — You know the basics. Dive into embeddings, vector databases, retrieval strategies, and prompt engineering. More independence, more architecture decisions. *(Modules 3–7)*
>
> 3. **Advanced** — You've built RAG before. Focus on generation quality, evaluation, agentic RAG, GraphRAG, and production deployment. You'll build systems, not just components. *(Modules 6–9)*
>
> **Not sure?** I can ask 5 quick questions to help you figure out where you fit. Just say "assess me."

If they pick a track (1, 2, or 3), go to **Step 3: Create Learner Profile**.

If they say "assess me" or similar, go to **Step 4: Background Assessment**.

## Step 3: Create Learner Profile

Create the file `progress/learner-profile.md` with the following structure:

```markdown
# Learner Profile

- **Track**: [Beginner/Intermediate/Advanced]
- **Language**: [Python/TypeScript/Go/Rust]
- **Started**: [today's date]
- **Assessment**: self-selected

## Current Module
Module [first module in track: 01 for Beginner, 03 for Intermediate, 06 for Advanced]

## Completed
(none yet)
```

Also create `progress/module-tracker.md` initialized with empty checkboxes for every lesson in the assigned track.

Then proceed to **Step 7: Next Steps**.

## Step 4: Background Assessment

Ask the following questions one at a time. Wait for each answer before proceeding.

1. **Programming experience**: "How comfortable are you with [their chosen language]?" (beginner=0 / intermediate=1 / advanced=2)
2. **ML knowledge**: "Have you worked with machine learning concepts like training, inference, or model evaluation?" (none=0 / some exposure=1 / hands-on=2)
3. **LLM familiarity**: "Have you used large language models (ChatGPT, Claude, open-source models) in code — not just chat UIs?" (never=0 / a few times=1 / regularly=2)
4. **Embeddings awareness**: "Do you know what vector embeddings are and how they represent text?" (no idea=0 / heard of them=1 / have used them=2)
5. **Search/IR background**: "Any experience with search engines, information retrieval, or databases?" (none=0 / basic SQL or search=1 / built search systems=2)

## Step 5: Score and Place

Sum the points (0-10 range). Place into a track:

| Score | Track | Starting Module | Modules Covered |
|-------|-------|-----------------|-----------------|
| 0-3 | Beginner | Module 01 | 01 → 04 |
| 4-6 | Intermediate | Module 03 | 03 → 07 |
| 7-10 | Advanced | Module 06 | 06 → 09 |

Note: Track modules overlap intentionally — this provides continuity.

## Step 6: Create Learner Profile (Assessed)

Present the recommended track. Ask the learner if they want to accept the recommendation or choose a different track.

Create the file `progress/learner-profile.md` with the following structure:

```markdown
# Learner Profile

- **Track**: [Beginner/Intermediate/Advanced]
- **Language**: [Python/TypeScript/Go/Rust]
- **Started**: [today's date]
- **Programming level**: [answer]
- **ML knowledge**: [answer]
- **LLM familiarity**: [answer]
- **Embeddings awareness**: [answer]
- **Search background**: [answer]
- **Assessment score**: [total]/10

## Current Module
Module [first module in track]

## Completed
(none yet)
```

Also create `progress/module-tracker.md` initialized with empty checkboxes for every lesson in the assigned track.

Then proceed to **Step 7: Next Steps**.

## Step 7: Quick-Start Scaffold

Before sending the learner off, give them something tangible. Create a minimal working RAG pipeline so they have code running in their first session:

1. Create `sandbox/data.txt` with 5-8 short paragraphs about RAG basics (use the content from Module 01 as source material)
2. Create `sandbox/pipeline.[ext]` (in their chosen language) that:
   - Loads the sample data
   - Chunks it (fixed-size, 200 tokens)
   - Embeds chunks with a local model (all-MiniLM-L6-v2 for Python/TS)
   - Stores in ChromaDB (in-memory)
   - Retrieves top-3 chunks for a sample query
   - Prints results with similarity scores
3. Create `sandbox/README.md` with run instructions

Run the pipeline and show the output: "Here's your first RAG retrieval. It's basic, but it works. You'll understand every piece of this by the end of Module 2."

If dependency installation is needed, guide them through it first.

## Step 8: Next Steps

Tell the learner their profile has been saved. Mention the milestone system: "Your track has milestones — concrete checkpoints that mark real progress. Run `/roadmap` anytime to see how far you've come."

Suggest next steps:

- `/lesson` — start your first lesson (your sandbox pipeline will make the concepts concrete)
- `/roadmap` — view the full curriculum map and track your progress
- `/journal` — jot down thoughts or questions as you learn

Keep the tone warm, encouraging, and practical throughout.
