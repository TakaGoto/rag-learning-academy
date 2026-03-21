---
name: lesson
description: "Start or continue a curriculum lesson"
---

# Lesson: Learn a RAG Concept Step by Step

> **Scope:** This skill **teaches new concepts** through structured lessons with explanations and exercises. To test what you already know, use `/quiz`.

This skill delivers structured curriculum lessons. Each lesson follows a consistent flow that builds understanding through explanation, examples, and hands-on practice.

## Step 1: Determine Which Lesson to Load

- If the user provides a module number and lesson name (e.g., `/lesson 3 chunking-strategies`), load that specific lesson.
- If no argument is given, read `progress/learner-profile.md` and `progress/module-tracker.md` to find the next incomplete lesson in the learner's track.
- If no profile exists, suggest running `/start` first.

## Step 2: Load Lesson Content

Look for the lesson content in `.claude/docs/curriculum/`. The curriculum is organized as flat module files:
- `module-01-foundations.md`, `module-02-document-processing.md`, etc.
- Each module file contains multiple lesson sections within it.

Load the module file (e.g., `.claude/docs/curriculum/module-01-foundations.md`) and navigate to the specific lesson section within it. If the module file exists, use it as the primary source. If it does not exist yet, generate the lesson content based on the module topic and RAG curriculum structure.

## Step 3: Present the Concept

Structure the lesson delivery as follows:

### Opening (Why This Matters)
Start with a real-world scenario or problem that this concept solves. Make it concrete and relatable.

### Core Explanation
Explain the concept clearly. Use analogies where helpful. Break complex ideas into digestible pieces. Include diagrams in ASCII where they add clarity.

### Code Example
Provide a working Python code example that demonstrates the concept. Use comments to explain each section. Keep dependencies minimal (prefer standard library + common packages like `langchain`, `chromadb`, `sentence-transformers`).

```python
# Example: Code demonstration during a lesson
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("What is RAG?")
print(f"Dimensions: {len(embedding)}")  # 384
```

### Key Takeaways
Summarize the 3-5 most important points from the lesson in a bulleted list.

## Step 4: Hands-On Exercise

Present a practical exercise that reinforces the lesson:
- Clearly state the objective
- Provide starter code or a template
- Define what "done" looks like
- Offer hints if the learner asks

Review the learner's solution when they share it. Provide constructive feedback — what they did well, what could be improved, and why.

## Step 5: Check Understanding

Ask 2-3 quick comprehension questions to verify the learner grasped the key ideas. These should be conversational, not quiz-style. Correct any misconceptions gently.

## Step 6: Track Progress

Update `progress/module-tracker.md` to mark this lesson as complete. Add the completion date. If all lessons in a module are complete, congratulate the learner.

Suggest 2-3 relevant next steps using slash commands:

- `/quiz` — test your understanding of the concepts from this lesson
- `/build` — apply what you learned by building a hands-on component
- `/lesson` — continue to the next lesson in your track

## Tone and Style

- Be encouraging but not patronizing
- Prefer concrete examples over abstract theory
- If the learner seems confused, offer a simpler explanation before moving on
- Celebrate progress — each lesson completed is a step forward
