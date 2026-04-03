---
name: break-it
description: "Find the bug — learn RAG by debugging intentionally broken pipelines"
---

# Break It: Learn by Debugging

Introduce a realistic bug into a RAG pipeline and challenge the learner to find and fix it. Debugging teaches more than building because you have to understand *why* things work to figure out *why they don't*.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Choose a Difficulty

If the learner specifies a difficulty (e.g., `/break-it hard`), use that. Otherwise, calibrate based on their progress:

- **Easy** — One obvious bug. The pipeline runs but gives clearly wrong results.
- **Medium** — One subtle bug. The pipeline runs and results look plausible but are wrong.
- **Hard** — Two bugs that interact. Fixing one makes the other more visible.

## Step 2: Select a Bug Category

Pick from these common RAG failure modes. Rotate through categories so the learner sees variety:

### Chunking Bugs
- Chunk size set way too small (10 tokens) — fragments lose all context
- Zero overlap — information at boundaries is lost
- Wrong separator for the document type (splitting code on paragraphs)

### Embedding Bugs
- Mismatched embedding models between indexing and querying
- Missing query prefix for asymmetric models (e.g., no "query: " prefix for E5)
- Embeddings not normalized, breaking cosine similarity

### Retrieval Bugs
- Top-k set to 1 — missing relevant context spread across chunks
- Wrong distance metric (L2 instead of cosine)
- Metadata filter too restrictive — filtering out relevant results

### Generation Bugs
- Context placed after the question (lost-in-the-middle effect)
- No grounding instruction — model ignores context and hallucinates
- Context window exceeded — retrieved chunks silently truncated

### Pipeline Bugs
- Stale index — new documents added but not re-embedded
- Document not chunked before embedding (entire doc as one vector)
- Query embedded with a different model than the corpus

## Step 3: Present the Broken Pipeline

Show the learner a complete, runnable pipeline with the bug(s) already in place. Include:

1. The code (with the bug hidden in plain sight)
2. Sample data
3. A query that exposes the bug
4. The actual output (showing the wrong behavior)
5. What the correct output should look like

Say: "Something's wrong with this pipeline. The query should return [expected], but it's returning [actual]. Can you find the bug?"

## Step 4: Guide the Debugging

Let the learner investigate. If they're stuck after 2 attempts, offer graduated hints:

- **Hint 1** (gentle): Point to the general area — "The issue is in the retrieval step" or "Look at how the chunks are created"
- **Hint 2** (specific): Narrow it down — "Compare the embedding model used for indexing vs querying"
- **Hint 3** (direct): Explain the bug and why it causes the behavior

## Step 5: Explain and Connect

Once they find the bug (or after hints), explain:
1. **Why** this bug causes the observed behavior
2. **How common** this bug is in real RAG systems
3. **How to prevent** it — what checks or tests would catch this early
4. **The concept** behind the fix — link to the relevant `/lesson` or `/explain` topic

## Step 6: Track and Suggest

Log the debugging session to `progress/debug-log.md` with the date, bug type, difficulty, and whether they found it independently.

Suggest next steps:
- `/break-it [harder difficulty]` to level up
- `/lesson` on the concept behind the bug
- `/build` to implement the correct pattern from scratch
