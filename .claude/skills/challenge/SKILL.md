---
name: challenge
description: "Take on a hands-on RAG challenge"
---

# Challenge: Real-World RAG Challenges

> **Scope:** This skill presents **open-ended, multi-component challenges** that require design decisions. For step-by-step guided construction of individual components, use `/build`.

Present the learner with a realistic RAG challenge that tests their skills across multiple components. Challenges are more open-ended than `/build` exercises — they require design decisions, not just implementation.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Select a Challenge

If the user specifies a difficulty or topic (e.g., `/challenge advanced` or `/challenge multilingual`), filter accordingly. Otherwise, recommend a challenge based on their progress.

### Beginner Challenges
1. **FAQ Bot**: Build a RAG system that answers questions from a FAQ document (provided). Must handle exact and paraphrased questions.
2. **Recipe Finder**: Index a collection of recipes and build a retriever that finds recipes by ingredients, cuisine, or dietary restrictions.
3. **Book Q&A**: Load a public-domain book, chunk it, and build a system that can answer questions about characters, plot, and themes.

### Intermediate Challenges
4. **Multi-Document Synthesis**: Build a RAG system that can answer questions requiring information from multiple documents. Test with a set of related articles.
5. **Conversational RAG**: Add conversation history to a RAG pipeline so follow-up questions work correctly (e.g., "What about the second one?").
6. **Metadata-Filtered Search**: Build a RAG system for product documentation where users can filter by product version, category, and date.
7. **Citation Generator**: Build a RAG system that not only answers questions but provides exact source citations with page/paragraph references.

### Advanced Challenges
8. **Multilingual RAG**: Build a system that handles documents in multiple languages and queries in any of those languages.
9. **Legal Document Analyst**: Build a RAG system for legal contracts that can answer questions about specific clauses, compare terms across contracts, and flag potential issues.
10. **Code Documentation Assistant**: Build a RAG system over a codebase that can answer questions about architecture, find relevant functions, and explain code patterns.
11. **Real-Time RAG**: Build a system that handles a continuously updating corpus (e.g., news articles) with minimal re-indexing latency.

## Step 2: Present the Challenge

For the selected challenge, provide:

### Challenge Brief
- **Objective**: What the learner needs to build (1-2 sentences)
- **Requirements**: Specific functional requirements (bulleted list)
- **Constraints**: Any limitations (e.g., must use open-source models, latency under 2 seconds)
- **Evaluation criteria**: How the solution will be judged

### Provided Resources
- Sample data or instructions for obtaining data
- Suggested directory structure
- Test queries and expected behavior

Show a deliverable example in the learner's chosen language with proper types, documentation, and structure.

### Hints (available on request)
Prepare a set of progressive hints — do not reveal them unless the learner asks. Start with high-level guidance and get more specific.

## Step 3: Support During the Challenge

While the learner works, be available to:
- Answer clarifying questions about the requirements
- Provide hints if they get stuck (but encourage them to try first)
- Help debug specific technical issues
- Discuss design trade-offs when they face a decision

Do not build the solution for them. Guide them to find the answer.

## Step 4: Evaluate the Solution

When the learner says they are done, evaluate their solution:

### Functionality Check
- Does it meet all the stated requirements?
- Run the test queries and check the results

### Design Review
- Is the architecture well-suited to the challenge?
- Were chunking, embedding, and retrieval choices appropriate?
- Is the prompt template effective?

### Quality Assessment
Rate the solution on:
- **Correctness**: Does it produce accurate answers? (1-5)
- **Robustness**: Does it handle edge cases? (1-5)
- **Code quality**: Is the code clean and well-organized? (1-5)
- **Design decisions**: Were trade-offs made thoughtfully? (1-5)

### Feedback
Provide specific feedback on what was done well and what could be improved. Suggest one stretch goal for extra credit.

## Step 5: Track and Celebrate

Save the challenge completion to `progress/challenges.md` with the date, challenge name, difficulty, and score. If this is their first challenge at a given difficulty level, acknowledge the milestone.

Suggest 2-3 relevant next steps using slash commands:

- `/code-review` — get expert feedback on the solution you just built
- `/evaluate` — measure the quality of your challenge solution with RAG metrics
- `/roadmap` — check your overall progress and see what to tackle next

## Guidelines

- Challenges should feel achievable but require real thought and effort
- The learner should make design decisions, not just follow steps
- Accept multiple valid approaches — there is rarely one right answer
- Be encouraging throughout — challenges are meant to stretch, not discourage
- Keep time expectations reasonable: beginner (1-2 hours), intermediate (2-4 hours), advanced (4-8 hours)
