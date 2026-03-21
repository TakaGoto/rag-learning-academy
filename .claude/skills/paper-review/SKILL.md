---
name: paper-review
description: "Walk through a RAG research paper together"
---

# Paper Review: Understand RAG Research Papers

Break down RAG research papers into understandable pieces, connecting academic innovations to practical applications the learner can use in their pipeline.

## Step 1: Identify the Paper

If the user provides a paper title or URL (e.g., `/paper-review "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"`), use that. Otherwise, suggest papers from a curated list organized by topic:

### Foundational Papers
- "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020)
- "Dense Passage Retrieval for Open-Domain Question Answering" (Karpukhin et al., 2020)
- "REALM: Retrieval-Augmented Language Model Pre-Training" (Guu et al., 2020)

### Chunking and Retrieval
- "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks" (Reimers & Gurevych, 2019)
- "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction" (Khattab & Zaharia, 2020)

### Advanced RAG
- "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection" (Asai et al., 2023)
- "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval" (Sarthi et al., 2024)

### Evaluation
- "RAGAS: Automated Evaluation of Retrieval Augmented Generation" (Es et al., 2023)

Ask the learner which paper interests them or recommend one based on their current module.

## Step 2: Set Context

Before diving in, give the learner context:
- What problem was this paper trying to solve?
- When was it published and why did it matter at that time?
- What should they pay attention to while reading?
- How does it connect to what they have already learned?

## Step 3: Section-by-Section Walkthrough

Break the paper down into digestible sections:

### Abstract and Introduction
- Summarize the core claim in one sentence
- What gap in existing work does this address?
- What is the proposed solution at a high level?

### Background and Related Work
- What prior work does this build on?
- What are the key concepts the reader needs to understand?
- Fill in any knowledge gaps the learner might have

### Methodology / Approach
- How does the proposed system work? Explain the architecture.
- Draw an ASCII diagram of the system if helpful.
- Translate mathematical notation into plain English where needed.
- Connect each component to practical RAG concepts the learner knows.

### Experiments and Results
- What did they test and how?
- What were the key results? Present the important numbers.
- Were the baselines fair? Any concerns about the evaluation?

### Discussion and Limitations
- What are the acknowledged limitations?
- What are the unacknowledged limitations you can spot?
- What follow-up work did this inspire?

## Step 4: Practical Takeaways

The most important step. Extract actionable insights:

1. **What can you use today?** Specific techniques or ideas applicable to the learner's pipeline.
2. **Key insight**: The one idea from this paper that changes how you think about RAG.
3. **Implementation hints**: How would you implement the core idea in a practical system?
4. **What to skip**: Parts of the paper that are specific to their experimental setup and less useful in practice.

## Step 5: Connect to Curriculum

Map the paper's concepts to specific curriculum modules and lessons. If the learner has not covered a prerequisite concept, briefly explain it or suggest the relevant `/lesson`.

## Step 6: Discussion Questions

Pose 2-3 thought-provoking questions:
- "How would this approach perform on your specific use case?"
- "What trade-offs does this design make that you might handle differently?"
- "If you could extend this work, what would you try?"

Discuss the learner's thoughts. This builds critical thinking about research.

## Guidelines

- Assume the learner has not read the paper — make it accessible
- Do not just summarize; explain and connect to practical knowledge
- Be honest about limitations — not every paper is a breakthrough
- Encourage the learner to read the original paper after the walkthrough
- Track paper reviews in `progress/papers-reviewed.md`
