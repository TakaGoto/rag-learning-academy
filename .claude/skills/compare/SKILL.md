---
name: compare
description: "Compare two RAG approaches side by side"
---

# Compare: Side-by-Side RAG Approach Analysis

Provide structured, balanced comparisons of RAG approaches so learners can make informed decisions for their pipelines.

## Step 1: Identify What to Compare

If the user specifies two approaches (e.g., `/compare fixed vs semantic chunking`), use those. Otherwise, present common comparison topics:

### Chunking Strategies
- Fixed-size vs. semantic chunking
- Sentence-based vs. paragraph-based
- Recursive character vs. document-structure aware

### Vector Databases
- Chroma vs. Pinecone vs. Weaviate vs. Qdrant
- In-memory vs. hosted vs. self-hosted
- FAISS vs. purpose-built vector DBs

### Search Methods
- Dense (vector) vs. sparse (BM25) vs. hybrid
- Single-stage vs. two-stage (retrieve + re-rank)
- Keyword vs. semantic vs. hybrid search

### Embedding Models
- OpenAI embeddings vs. open-source (sentence-transformers)
- Small vs. large embedding models
- Domain-specific vs. general-purpose embeddings

### Architecture Patterns
- Naive RAG vs. advanced RAG vs. modular RAG
- Single-hop vs. multi-hop retrieval
- RAG vs. fine-tuning vs. long-context models

Ask the learner to pick one or suggest their own comparison.

## Step 2: Present the Structured Comparison

For each approach, cover these dimensions in a clear side-by-side format:

### Concept Overview
Explain each approach in 2-3 sentences. What is it and how does it work?

### How It Works (Technical Detail)
Describe the mechanism. Include a short code snippet or pseudocode for each.

### Pros and Cons Table

```
| Dimension        | Approach A        | Approach B        |
|------------------|-------------------|-------------------|
| Ease of setup    | ...               | ...               |
| Performance      | ...               | ...               |
| Scalability      | ...               | ...               |
| Cost             | ...               | ...               |
| Flexibility      | ...               | ...               |
| Maintenance      | ...               | ...               |
```

### Performance Characteristics
Discuss latency, throughput, accuracy trade-offs with concrete numbers or ranges where possible.

### Code Examples
Provide a minimal working code example for each approach so the learner can see the practical difference.

## Step 3: Decision Framework

Help the learner decide which approach fits their situation:

- **Choose A when**: [specific scenarios]
- **Choose B when**: [specific scenarios]
- **Consider combining both when**: [specific scenarios]

Frame this as trade-offs, not absolute recommendations. The right choice depends on the use case.

## Step 4: Hands-On Experiment

Suggest a quick experiment the learner can run to compare both approaches with their own data:
1. Set up both approaches with minimal code
2. Run the same set of test queries through each
3. Compare results on relevancy, latency, and output quality
4. Draw their own conclusions

## Step 5: Key Takeaway

Summarize the comparison in one or two sentences that capture the essential trade-off. For example: "Fixed chunking is simpler and faster to set up, but semantic chunking preserves meaning boundaries — start with fixed, switch to semantic when you see context-boundary issues."

Suggest 2-3 relevant next steps using slash commands:

- `/build` — implement the approach you chose and see it in action
- `/architecture` — design a full RAG architecture using the approach that fits your use case
- `/benchmark` — benchmark both approaches with your own data to confirm the trade-offs

## Guidelines

- Stay balanced — do not push one approach over another without justification
- Use concrete numbers and examples, not vague qualitative claims
- Acknowledge that best practices evolve as the field moves fast
- Connect the comparison back to the learner's current project when possible
