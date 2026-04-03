---
name: explain
description: "Get a deep-dive explanation of any RAG concept"
---

# Explain: Deep-Dive into Any RAG Concept

Provide a thorough, multi-layered explanation of any RAG concept. Unlike `/glossary` (which gives quick definitions), `/explain` goes deep — this is for when the learner really wants to understand something.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Identify the Concept and Calibrate Depth

If the user specifies a concept (e.g., `/explain cosine similarity`), explain that. If they give a vague topic (e.g., "retrieval"), ask a clarifying question to narrow the scope. Good explanations are focused.

### ELI5 Mode

If the learner says `/explain eli5 [concept]` or includes "eli5", "simple", "for dummies", or "no jargon":
- Give the entire explanation using only everyday language and analogies
- Zero technical terms. If you must use one, define it in parentheses immediately
- Skip the code example and math. Use diagrams and real-world comparisons instead
- Keep the whole explanation under 20 lines
- End with: "Want the technical version? Just say 'go deeper.'"

### Standard Mode

- If the learner seems to want a quick answer (short question, or they say "briefly" / "quickly"), provide a **2-3 sentence TL;DR** first, then ask "Want me to go deeper?" before proceeding through the full 9-step explanation.
- If the learner wants depth, proceed normally through all steps.

Common concepts learners ask about:
- How embeddings work
- Vector similarity and distance metrics
- Chunking strategies and trade-offs
- How retrieval-augmented generation works end-to-end
- Re-ranking and why it helps
- Hybrid search (combining dense and sparse)
- Prompt engineering for RAG
- Evaluation metrics (RAGAS, faithfulness, etc.)
- Hallucination and how to reduce it
- Context window management
- Fine-tuning vs. RAG

## Step 2: The ELI5 Version

Start with the simplest possible explanation. Use an everyday analogy that anyone could understand. No jargon, no code, just the core idea.

Example for "vector embeddings": "Imagine every piece of text gets a home address in a huge city. Similar texts live in the same neighborhood. When you search, you are just looking for the nearest neighbors to your query's address."

This gives the learner the intuition before the details.

## Step 3: The Technical Explanation

Now go deeper with precision:
- Define the concept formally
- Explain the mechanism step by step
- Cover the mathematics where relevant (but always explain what the math means)
- Discuss the key parameters and how they affect behavior
- Explain where this fits in the RAG pipeline

Use clear section headers to organize the explanation. Break complex ideas into numbered steps.

## Step 4: Code Example

Provide a working code example in the learner's chosen language that demonstrates the concept:
- Keep it self-contained and runnable
- Use comments to explain each meaningful line
- Show the output so the learner knows what to expect
- Use common libraries for the learner's language (see `language-support.md` for mappings)

If the concept is architectural rather than code-level, provide pseudocode or a configuration example instead.

## Step 5: Visual Diagram

Create an ASCII diagram that illustrates the concept visually:

```
Query: "How does photosynthesis work?"
         |
         v
  [ Embedding Model ]
         |
         v
  [0.23, -0.45, 0.67, ...]  <-- query vector (384 dims)
         |
         v
  [ Vector DB: find nearest neighbors ]
         |
    cosine similarity
         |
   +-----+-----+-----+
   |     |     |     |
  0.92  0.87  0.84  0.61  <-- similarity scores
   |     |     |
  Doc1  Doc3  Doc7   <-- top-3 retrieved
```

Diagrams should clarify, not complicate. Only include them when they add understanding.

## Step 6: Common Misconceptions

List 2-4 things people commonly get wrong about this concept:

- **Misconception**: [what people think]
- **Reality**: [what is actually true]
- **Why it matters**: [practical consequence of the misunderstanding]

This is often the most valuable part of the explanation, because misconceptions are where bugs come from.

## Step 7: Practical Implications

Connect the concept to real-world RAG pipeline decisions:
- How does this affect pipeline quality?
- What goes wrong when you get this wrong?
- What are the typical tuning knobs and their trade-offs?
- When would you choose one approach over another?

## Step 8: Further Reading

Point the learner to:
- The relevant curriculum module and lesson (via `/lesson`)
- Key papers that introduced or advanced the concept (via `/paper-review`)
- Any related concepts they should understand next (via `/glossary`)

## Step 9: Check Understanding

Ask the learner one focused question to see if they grasped the key idea. Keep it conversational. If they are uncertain, offer to explain a specific part again from a different angle.

Suggest 2-3 relevant next steps using slash commands:

- `/quiz` — test your understanding of this concept and related ideas
- `/lesson` — learn about this topic in a structured lesson with exercises
- `/build` — apply this concept hands-on by building a RAG component

## Guidelines

- Layer the explanation from simple to complex — let the learner go as deep as they want
- Never assume knowledge the learner might not have — define terms as you use them
- Use concrete examples with actual data, not abstract descriptions
- If you are uncertain about a detail, say so rather than guessing
- Tailor the depth to the learner's level (check their profile if available)
- The goal is genuine understanding, not memorization
