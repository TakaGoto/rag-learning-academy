---
name: quiz
description: "Test your understanding of a RAG concept"
---

# Quiz: Test Your RAG Knowledge

> **Scope:** This skill **tests your understanding** with questions and scoring. For guided teaching of new concepts, use `/lesson`.

Generate and administer a quiz on a specific RAG topic to help learners assess their understanding. Quizzes reinforce learning and surface gaps.

## Step 1: Determine the Topic

- If the user specifies a topic (e.g., `/quiz chunking`), use that topic.
- If no topic is given, read `progress/module-tracker.md` to find the most recently completed lesson and quiz on that.
- If no progress exists, suggest running `/start` or `/lesson` first.

## Step 2: Generate Questions

Create 5-10 questions that mix the following types:

### Conceptual Questions (2-3)
Test understanding of "why" and "how" things work. Example: "Why might fixed-size chunking lose important context at chunk boundaries?"

### Code Reading Questions (2-3)
Show a code snippet and ask what it does, what is wrong with it, or what the output would be. Example: Show a retrieval function and ask why it might return irrelevant results.

### Scenario-Based Questions (2-3)
Present a real-world situation and ask the learner to choose the best approach. Example: "You have a corpus of legal contracts averaging 50 pages each. Which chunking strategy would you start with and why?"

### True/False with Justification (1-2)
A statement the learner must evaluate and explain. Example: "Larger chunk sizes always improve retrieval quality. True or false? Explain."

## Step 3: Administer the Quiz

Present questions one at a time. Wait for the learner's answer before moving to the next question. Do not reveal the correct answer until the learner has responded.

For each question:
1. Present the question clearly
2. Wait for the learner's response
3. Evaluate the response — is it correct, partially correct, or incorrect?
4. Provide the correct answer with a clear explanation
5. If incorrect, explain the misconception and link it back to the relevant concept

## Step 4: Score and Review

After all questions are answered, present a summary:

```
Quiz Results: [Topic]
Score: [X]/[Total] ([percentage]%)
---
Strengths: [areas where the learner did well]
Gaps: [areas that need review]
Recommendation: [what to study next]
```

## Step 5: Track Results

Save the quiz results to `progress/quiz-results.md` with the date, topic, score, and any identified gaps. Append to the file if it already exists.

## Step 6: Suggest Next Steps

Based on the score, suggest 2-3 relevant next steps using slash commands:

- **90-100%**: Congratulate them.
  - `/challenge` — put your mastery to the test with a real-world challenge
  - `/build` — apply your knowledge by building a hands-on component
  - `/lesson` — continue to the next lesson in your track
- **70-89%**: Good progress. Recommend reviewing the specific gaps.
  - `/build` — reinforce your understanding by building what you just learned
  - `/lesson` — continue to the next lesson or revisit a weak area
  - `/explain` — get a deeper explanation of any concepts that felt shaky
- **Below 70%**: Encourage them.
  - `/lesson` — revisit the lesson to strengthen your foundations
  - `/explain` — get a deep-dive explanation on the weak areas
  - `/glossary` — review key terms you may have missed

## Guidelines

- Questions should be practical and relevant, not trivia
- Accept reasonable alternative answers — RAG is a field with multiple valid approaches
- Be encouraging even when answers are wrong — mistakes are how we learn
- Vary difficulty within the quiz (start easier, build up)
