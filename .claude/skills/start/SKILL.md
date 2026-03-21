---
name: start
description: "Begin your RAG learning journey — assess your level and pick a learning path"
---

# Onboarding: Start Your RAG Learning Journey

Welcome the learner and explain that this short assessment will help tailor the curriculum to their experience level.

## Step 1: Background Assessment

Ask the following questions one at a time. Wait for each answer before proceeding.

1. **Python experience**: "How comfortable are you with Python? (beginner / intermediate / advanced)"
2. **ML knowledge**: "Have you worked with machine learning concepts like training, inference, or model evaluation? (none / some exposure / hands-on experience)"
3. **LLM familiarity**: "Have you used large language models (ChatGPT, Claude, open-source models) in code — not just chat UIs? (never / a few times / regularly)"
4. **Embeddings awareness**: "Do you know what vector embeddings are and how they represent text? (no idea / heard of them / have used them)"
5. **Search/IR background**: "Any experience with search engines, information retrieval, or databases? (none / basic SQL or search / built search systems)"

## Step 2: Score and Classify

Assign points to each answer (0 for lowest, 2 for highest). Sum the total.

| Score Range | Track        | Modules |
|-------------|--------------|---------|
| 0-3         | Beginner     | 1-4     |
| 4-6         | Intermediate | 3-7     |
| 7-10        | Advanced     | 6-9     |

## Step 3: Recommend a Learning Path

Present the recommended track with a brief overview of what it covers:

- **Beginner**: Foundations of RAG, text processing, embeddings basics, your first retrieval pipeline.
- **Intermediate**: Chunking strategies, vector databases, retrieval tuning, prompt engineering for RAG.
- **Advanced**: Hybrid search, re-ranking, evaluation frameworks, production deployment, advanced architectures.

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

Tell the learner:
- Their profile has been saved
- Suggest running `/lesson` to start their first lesson
- Mention `/roadmap` to check progress at any time
- Encourage them — learning RAG is a practical skill and they will build real systems

Keep the tone warm, encouraging, and practical throughout.
