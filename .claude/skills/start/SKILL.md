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

Then transition: "To recommend the right starting point, I'll ask five quick questions about your background. There are no wrong answers — this just helps me calibrate."

## Step 1: Background Assessment

Ask the following questions one at a time. Wait for each answer before proceeding.

1. **Python experience**: "How comfortable are you with Python?" (beginner=0 / intermediate=1 / advanced=2)
2. **ML knowledge**: "Have you worked with machine learning concepts like training, inference, or model evaluation?" (none=0 / some exposure=1 / hands-on=2)
3. **LLM familiarity**: "Have you used large language models (ChatGPT, Claude, open-source models) in code — not just chat UIs?" (never=0 / a few times=1 / regularly=2)
4. **Embeddings awareness**: "Do you know what vector embeddings are and how they represent text?" (no idea=0 / heard of them=1 / have used them=2)
5. **Search/IR background**: "Any experience with search engines, information retrieval, or databases?" (none=0 / basic SQL or search=1 / built search systems=2)

## Step 2: Score and Place

Sum the points (0-10 range). Place into a track:

| Score | Track | Starting Module | Modules Covered |
|-------|-------|-----------------|-----------------|
| 0-3 | Beginner | Module 01 | 01 → 04 |
| 4-6 | Intermediate | Module 03 | 03 → 07 |
| 7-10 | Advanced | Module 06 | 06 → 09 |

Note: Track modules overlap intentionally — this provides continuity. Intermediate learners revisit Embeddings (Module 03) which Beginners just completed, but at a faster pace. Advanced learners start at Generation (Module 06) which Intermediates just covered.

## Step 3: Recommend a Learning Path

Present the recommended track with a brief overview:

- **Beginner**: "You'll start with what RAG is, learn to process documents, understand embeddings, and build your first retrieval pipeline. Expect lots of guided examples."
- **Intermediate**: "You'll dive into embeddings, vector databases, retrieval strategies, and prompt engineering. More independence, more architecture decisions."
- **Advanced**: "You'll focus on generation quality, evaluation frameworks, advanced patterns (agentic RAG, GraphRAG), and production deployment. You'll build systems, not just components."

Ask the learner if they want to accept the recommendation or choose a different track.

## Step 4: Create Learner Profile

Create the file `progress/learner-profile.md` with the following structure:

```markdown
# Learner Profile

- **Track**: [Beginner/Intermediate/Advanced]
- **Started**: [today's date]
- **Python level**: [answer]
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

## Step 5: Next Steps

Tell the learner their profile has been saved. Mention the milestone system: "Your track has milestones — concrete checkpoints that mark real progress. Run `/roadmap` anytime to see how far you've come."

Encourage them: "You're going to build real, working RAG systems. Let's start."

Suggest 2-3 relevant next steps using slash commands:

- `/lesson` — start your first lesson in the recommended track
- `/roadmap` — view the full curriculum map and track your progress
- `/glossary` — look up any unfamiliar RAG terms as you learn

Keep the tone warm, encouraging, and practical throughout.
