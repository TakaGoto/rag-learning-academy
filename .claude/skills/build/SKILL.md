---
name: build
description: "Build a RAG component hands-on with guided steps"
---

# Build: Hands-On RAG Component Construction

> **Scope:** This skill provides **step-by-step guided construction** of individual RAG components. For open-ended, multi-component challenges that require design decisions, use `/challenge`.

Guide the learner through building a real RAG component from scratch. This is the core hands-on skill — learners write actual code with step-by-step guidance.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Choose What to Build

If the user specifies a component (e.g., `/build chunker`), use that. Otherwise, present the available components based on their track progress:

| Component          | Difficulty   | Prerequisites         |
|--------------------|--------------|-----------------------|
| Document loader    | Beginner     | Programming basics in your chosen language |
| Text chunker       | Beginner     | Module 1              |
| Embedding pipeline | Intermediate | Modules 1-2           |
| Vector store setup | Intermediate | Modules 1-3           |
| Retriever          | Intermediate | Modules 1-4           |
| RAG chain          | Intermediate | Modules 1-5           |
| Re-ranker          | Advanced     | Modules 1-6           |
| Evaluation harness | Advanced     | Modules 1-7           |
| Full RAG pipeline  | Advanced     | Modules 1-8           |

## Step 2: Set Up the Project

- Check if a project workspace exists in `projects/`. If not, help the learner create one.
- Explain the dependencies needed and help install them.
- Reference templates in `.claude/docs/templates/` if available.
- Create the file structure for the component.

## Step 3: Guided Implementation

Walk through the build in clear stages. For each stage:

1. **Explain the goal** of this stage — what are we building and why?
2. **Show the interface** — what inputs does this piece take, what does it output?
3. **Let the learner write the code** — provide the function signature and docstring, let them fill in the implementation.
4. **Review their code** — check for correctness, efficiency, and best practices.
5. **Suggest improvements** — offer one or two ways to make it better (error handling, performance, configurability).

Keep each stage small and focused. A chunker build might look like:
- Stage 1: Read a document into text
- Stage 2: Implement fixed-size chunking
- Stage 3: Add overlap between chunks
- Stage 4: Handle edge cases (empty docs, very short docs)
- Stage 5: Add metadata to chunks

For example, provide a skeleton in the learner's chosen language with the function signature, docstring/comments, and placeholder logic. Use idiomatic patterns for the language.

## Step 4: Test the Component

Help the learner write tests for their component:
- Provide sample input data
- Define expected outputs
- Run the tests and verify correctness
- Discuss edge cases they should think about

## Step 5: Integration Check

Explain how this component fits into the larger RAG pipeline. Show how it connects to the previous and next components in the chain. If the learner has already built other components, help them wire this one in.

## Step 6: Review and Reflect

Summarize what was built:
- What the component does
- Key design decisions made
- What they learned
- Ideas for extending it further

Update `progress/module-tracker.md` to note the completed build exercise.

Suggest 2-3 relevant next steps using slash commands:

- `/evaluate` — measure the quality of what you just built with RAG metrics
- `/code-review` — get expert feedback on your implementation
- `/challenge` — take on an open-ended challenge that combines multiple components

## Guidelines

- Let the learner do the actual coding — guide, do not just provide the answer
- If they get stuck, give increasingly specific hints rather than the solution
- Celebrate working code — even simple implementations are achievements
- Point out common pitfalls specific to each component (e.g., chunk overlap calculations, embedding dimension mismatches)
- Use real-world data examples when possible, not just "lorem ipsum"
