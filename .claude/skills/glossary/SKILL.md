---
name: glossary
description: "Look up RAG terminology and concepts"
---

# Glossary: RAG Terminology and Concepts

An interactive glossary that provides clear, multi-layered definitions of RAG terminology. Designed to be a quick reference that also teaches.

## Step 1: Determine What to Look Up

- If the user provides a term (e.g., `/glossary embeddings`), define that term.
- If the user provides a module number (e.g., `/glossary module 3`), list all key terms for that module.
- If no argument is given, present the full glossary organized by category.

## Step 2: Present the Definition

For each term, provide a structured definition with these layers:

### One-Line Definition
A concise, precise definition in one sentence. Example: "An embedding is a dense numerical vector that represents the semantic meaning of a piece of text."

### Analogy
An everyday analogy that makes the concept intuitive. Example: "Think of embeddings like GPS coordinates for meaning — texts with similar meanings have coordinates that are close together on the map of all possible meanings."

### Technical Detail
A deeper technical explanation for learners who want to understand the mechanism. Include relevant details like dimensions, algorithms, or mathematical concepts — but keep it accessible.

### Code Example
A minimal Python code snippet that demonstrates the concept in action:

```python
# Example: Creating an embedding
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode("What is RAG?")
print(f"Dimension: {len(embedding)}")  # 384
```

### Common Misconceptions
One or two things people often get wrong about this concept. Example: "Embeddings are not word-for-word encodings — the same word in different contexts will have different embeddings in contextual models."

### Related Terms
Links to other glossary terms that are closely related, so the learner can explore connected concepts.

### Curriculum Connection
Which module and lesson covers this concept in depth, so the learner can dive deeper if needed.

## Step 3: Glossary Categories

Organize terms into these categories for browsing:

### Foundations
- RAG (Retrieval-Augmented Generation)
- LLM (Large Language Model)
- Embedding / Vector Embedding
- Token / Tokenization
- Context Window
- Prompt / Prompt Template

### Document Processing
- Chunking / Chunk
- Overlap (chunk overlap)
- Document Loader
- Metadata
- Preprocessing / Cleaning

### Retrieval
- Vector Database / Vector Store
- Similarity Search / Nearest Neighbor
- Cosine Similarity
- Top-k Retrieval
- BM25 / Sparse Retrieval
- Hybrid Search
- Re-ranking

### Generation
- Grounding
- Hallucination
- Faithfulness
- System Prompt
- Few-shot Examples
- Chain-of-Thought

### Evaluation
- RAGAS
- Precision / Recall
- MRR (Mean Reciprocal Rank)
- Faithfulness Score
- Answer Relevancy

### Advanced Concepts
- Hypothetical Document Embedding (HyDE)
- Multi-hop Retrieval
- Agentic RAG
- Self-RAG
- Query Decomposition
- Recursive Retrieval

## Step 4: Interactive Features

- If the learner asks "what does X mean in the context of Y?", tailor the explanation to that specific context.
- If they ask to compare two terms, provide a brief comparison highlighting the key difference.
- If they seem confused, offer the simpler analogy first and build up to the technical detail.

## Guidelines

- Keep definitions precise — do not conflate terms that have distinct meanings
- Use consistent terminology throughout (match what the curriculum uses)
- Update examples to match the learner's tech stack when possible
- Be honest when terms have multiple definitions in the field — note the ambiguity
- This should feel like a knowledgeable colleague explaining things, not a textbook
