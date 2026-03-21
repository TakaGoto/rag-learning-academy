---
name: debug-rag
description: "Diagnose and fix common RAG failure modes"
---

# Debug RAG: Diagnose and Fix Pipeline Issues

An interactive debugging workflow that helps learners identify and resolve common RAG failure modes. This skill builds debugging intuition alongside technical problem-solving.

## Step 1: Identify the Symptom

Ask the learner to describe the problem they are seeing. Common symptoms include:

1. **Hallucination**: The model generates information not in the retrieved context
2. **Irrelevant retrieval**: The retrieved documents do not match the query
3. **Missing context**: Relevant information exists in the corpus but is not retrieved
4. **Incomplete answers**: The answer is partially correct but missing key details
5. **Contradictory answers**: The answer contradicts the source documents
6. **Repetitive or generic responses**: The model ignores context and gives generic answers
7. **Wrong format**: The answer is correct but not in the expected format
8. **High latency**: The pipeline is too slow

If the learner is not sure, ask them to share an example query, the expected answer, and the actual answer.

## Step 2: Follow the Diagnostic Tree

Based on the symptom, walk through the appropriate diagnostic path:

### For Retrieval Issues (irrelevant results, missing context)

Start by inspecting what the retriever actually returns:

```python
# Example diagnostic probe
results = retriever.retrieve("What is machine learning?", top_k=10)
for r in results:
    print(f"Score: {r.score:.3f} | Source: {r.metadata['source']} | Text: {r.text[:80]}...")
```

1. **Check the query**: Is the query well-formed? Try rephrasing it.
2. **Inspect chunks**: Look at the actual chunks in the vector store. Are they the right size? Do they contain the expected information?
3. **Test embedding similarity**: Compute the similarity between the query embedding and the expected chunk embedding. Is it above the retrieval threshold?
4. **Check top-k**: Are you retrieving enough documents? Try increasing top-k.
5. **Examine metadata filters**: Are any filters accidentally excluding relevant results?
6. **Compare search methods**: Try keyword search alongside vector search to see if the issue is in the embeddings.

### For Generation Issues (hallucination, contradictions, generic responses)

1. **Inspect the prompt**: Print the full prompt sent to the LLM. Is the context included correctly?
2. **Check context ordering**: Are the most relevant documents first in the context?
3. **Look for context overflow**: Is the context exceeding the model's context window?
4. **Test with perfect context**: Manually provide the correct context and see if the model generates correctly. This isolates retrieval vs. generation issues.
5. **Review system prompt**: Does it instruct the model to only use the provided context?
6. **Check temperature**: High temperature increases hallucination risk.

### For Indexing & Configuration Issues (chunk boundaries, model mismatches, filter bugs)

These are the sneakiest bugs — the pipeline runs without errors but produces bad results.

1. **Chunk boundary problems**: The answer to a question might be split across two chunks, with neither chunk containing the complete fact. To diagnose: retrieve the chunks immediately before and after the expected chunk (by index). If the fact spans the boundary, the fix is larger chunks, more overlap, or semantic chunking.
2. **Embedding model mismatch**: Verify the exact model name AND vector dimensions used at index time match query time. A mismatch (e.g., indexing with `text-embedding-3-large` at 3072 dims, querying with `text-embedding-3-small` at 1536 dims) produces nonsense scores that look numerically plausible. Print both configs side by side.
3. **Metadata filter bugs**: Run the exact same query with ALL metadata filters disabled. If results improve dramatically, re-enable filters one at a time. Common culprits: case-sensitive mismatches (`"PDF"` vs `"pdf"`), filtering on a field that was never populated, type mismatches (string `"2024"` vs integer `2024`).
4. **Stale index**: If you've added many vectors without rebuilding the index, HNSW recall degrades. Check if your vector DB needs an explicit optimize/compact call (Qdrant does, ChromaDB handles it automatically).
5. **Asymmetric embedding prefixes**: Many models (E5, BGE) require different prefixes for queries vs documents (`"query: "` vs `"passage: "`). If you embed both the same way, retrieval quality drops silently.

### For Performance Issues (high latency)

1. **Profile each stage**: Measure time for embedding, retrieval, and generation separately.
2. **Check batch sizes**: Are embeddings computed one at a time instead of in batches?
3. **Inspect vector DB performance**: Is the index optimized? How many vectors are stored?
4. **Review model selection**: Is the generation model appropriately sized for the task?

## Step 3: Apply the Fix

For each identified issue, provide:
- A clear explanation of why this causes the problem
- The specific code change or configuration adjustment needed
- A way to verify the fix worked

Walk the learner through making the change and re-testing.

## Step 4: Verify the Fix

Help the learner test that the fix resolved the original issue:
- Re-run the failing query
- Compare before and after results
- Check that the fix did not introduce new problems

## Step 5: Document the Fix

Encourage good practices by helping the learner document:
- What the symptom was
- What the root cause was
- What the fix was
- How to prevent it in the future

Save debugging notes to `progress/debug-log.md` for future reference.

## Step 6: Build Debugging Intuition

After resolving the issue, explain the broader pattern. For example: "Hallucination often comes from the prompt, not the model. Always check your prompt template first." This helps learners build a mental model for future debugging.

Suggest 2-3 relevant next steps using slash commands:

- `/evaluate` — run a full evaluation to confirm the fix improved overall quality
- `/build` — rebuild or improve the component that caused the issue
- `/code-review` — get expert feedback to catch other potential problems

## Guidelines

- Always start with the simplest possible cause before investigating complex ones
- Encourage the learner to form hypotheses before looking at the data
- Use the pipeline's actual data for debugging, not synthetic examples
- Teach the learner to isolate variables — change one thing at a time
