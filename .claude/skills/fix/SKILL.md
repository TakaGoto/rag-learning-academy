---
name: fix
description: "Diagnose and fix your RAG pipeline — skip the teaching, get to the answer"
---

# Fix: Fast-Track RAG Diagnosis

For learners who already have a RAG pipeline and just need help fixing it. No curriculum, no lessons — straight to diagnosis and solutions.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Get the Symptom

Ask one question: "What's going wrong?"

Common symptoms and what to probe for:

| Symptom | Follow-up |
|---------|-----------|
| "Bad retrieval results" | Ask for a sample query + what it returns vs what it should return |
| "Hallucinating" | Ask if context is being passed, and what the prompt looks like |
| "Slow" | Ask about data size, embedding model, vector DB, and whether they're batching |
| "No results" | Ask if data is indexed, and check the collection exists |
| "Works sometimes" | Ask for a working query and a failing query — compare them |

## Step 2: Read Their Code

Ask the learner to point you to their pipeline code. Read the files in `src/` or wherever they indicate. Look at:

1. **Chunking** — strategy, size, overlap
2. **Embedding** — model, dimensions, normalization
3. **Storage** — vector DB config, distance metric
4. **Retrieval** — top-k, filters, search type
5. **Generation** — prompt template, context injection, grounding instructions

## Step 3: Diagnose

Identify the likely root cause. Present it clearly:

```
Diagnosis: [one-line summary]
Root cause: [what's actually happening]
Evidence: [what in their code/output points to this]
```

If you're not certain, rank the top 2-3 most likely causes and explain how to verify each.

## Step 4: Fix It

Provide the specific code change needed. Show a before/after diff if possible. Explain *why* the fix works in 1-2 sentences — enough to understand, not a lecture.

If the fix requires multiple changes, prioritize: "Fix this first, then we'll check if the other issues resolve."

## Step 5: Verify

Help them test the fix:
1. Re-run the failing query
2. Compare the output to what they expected
3. If still broken, go back to Step 3 with the new information

## Step 6: Optional Learning

After the fix works, offer (don't push): "Want to understand why this happened? `/explain [relevant concept]` goes deeper on this."

Log the fix to `progress/debug-log.md` if the file exists.
