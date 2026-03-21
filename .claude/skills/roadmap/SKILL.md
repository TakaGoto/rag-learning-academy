---
name: roadmap
description: "View your learning progress and recommended next steps"
---

# Roadmap: Track Your Progress and Plan Ahead

Read the learner's progress data and present a clear picture of where they are, what they have accomplished, and what to do next.

## Step 1: Load Progress Data

Read the following files from the `progress/` directory:
- `learner-profile.md` — track assignment, start date, background
- `module-tracker.md` — lesson completion status
- `quiz-results.md` — quiz scores and identified gaps
- `challenges.md` — completed challenges and scores
- `debug-log.md` — debugging sessions
- `papers-reviewed.md` — papers studied

If `progress/learner-profile.md` does not exist, the learner has not started yet. Suggest running `/start` to begin their journey.

## Step 2: Display Progress Overview

Present a clear summary:

```
RAG Learning Academy — Your Progress
=====================================
Track: [Beginner/Intermediate/Advanced]
Started: [date]
Days active: [N]

Module Progress:
  [===========-------] 58% (21/36 lessons)

  Module 1: Foundations              [####] Complete
  Module 2: Document Processing      [####] Complete
  Module 3: Embeddings               [##--] 2/4 lessons
  Module 4: Vector Databases         [----] Not started
  Module 5: Retrieval Strategies     [----] Not started
  Module 6: Generation               [----] Not started
  Module 7: Evaluation               [----] Not started
  Module 8: Advanced Patterns        [----] Not started
  Module 9: Production               [----] Not started
```

Use visual progress bars built from ASCII characters. Make the progress feel tangible and motivating.

## Step 3: Show Milestone Progress

Read `.claude/docs/reference/milestones.md` to load the milestone definitions. Based on the learner's track and progress, display their milestone status:

```
Milestones
==========
  ✓ Milestone 1: First Light         — You built a working RAG system
  ✓ Milestone 2: Data Wrangler       — You can process any document
  ◐ Milestone 3: Vector Navigator    — 3/5 requirements done
  ○ Milestone 4: Retrieval Engineer   — Not started
```

Use ✓ for complete, ◐ for in-progress (show fraction), ○ for not started. Only show milestones relevant to the learner's track (e.g., Beginner track shows milestones 1-3).

For the current in-progress milestone, show which requirements remain:
```
  Next up for Milestone 3 — Vector Navigator:
  - [ ] Complete the "Model Shootout" exercise
  - [ ] Pass a quiz on embeddings or vector databases
```

Celebrate completed milestones warmly. For the current milestone, make the remaining items feel achievable.

**Proficiency level display:** Also check which proficiency level the learner has earned based on completed milestones (see the "Proficiency Levels" section of milestones.md):

```
Proficiency Level: RAG Practitioner
  ✓ RAG Explorer        (Milestones 1-2)
  ✓ RAG Practitioner    (Milestones 3-5)    ← CURRENT LEVEL
  ◐ RAG Engineer        (Milestones 6-7)    ← 1 milestone away
  ○ RAG Architect       (Milestone 8 + bonus)
```

When a learner earns a new level, celebrate it prominently: "Congratulations — you've earned the **RAG Practitioner** level! You can now design and build real retrieval systems."

## Step 4: Highlight Achievements

Call out what the learner has accomplished:
- Total lessons completed
- Milestones earned
- Quizzes passed (and average score)
- Challenges completed (with difficulty levels)
- Components built via `/build`
- Papers reviewed
- Debugging sessions completed

If there are notable achievements, celebrate them: "You have completed all beginner challenges — that is a solid foundation."

Also mention bonus milestones (Reviewer, Debugger, Completionist) if the learner is making progress toward them.

## Step 5: Identify Knowledge Gaps

Analyze quiz results and challenge scores to find areas where the learner may need more practice:

- Topics with quiz scores below 70%
- Challenge areas where they scored low on specific dimensions
- Modules they skipped or partially completed
- Concepts flagged during debugging sessions

Present these as opportunities, not failures: "You might benefit from revisiting chunking strategies — your quiz score suggests some concepts did not fully click yet."

## Step 6: Recommend Next Steps

Based on the progress data, suggest 3-5 specific next actions, prioritized by impact:

1. **Continue your current module**: If a module is in progress, suggest the next lesson.
2. **Fill a knowledge gap**: If quiz results show a weak area, suggest `/explain` or `/lesson` for that topic.
3. **Take a challenge**: If they have completed several lessons without a challenge, suggest one at their level.
4. **Evaluate their pipeline**: If they have built components but not evaluated, suggest `/evaluate`.
5. **Level up**: If they have completed their track, suggest moving to the next difficulty level.

Each suggestion should include the specific slash command to run.

## Step 7: Show the Full Curriculum Map

Display the complete curriculum with the learner's position marked. Indicate core vs optional lessons and show estimated time:

```
Module 1: RAG Foundations
  [x] 1.1 What is RAG? (core, 30m)
  [x] 1.2 When to Use RAG (core, 30m)
  [x] 1.3 RAG Architecture Overview (core, 45m)
  [x] 1.4 Hello World RAG (core, 60m)

Module 2: Document Processing
  [x] 2.1 Document Parsing (core, 45m)
  [ ] 2.2 Text Preprocessing (optional, 30m)
  [x] 2.3 Fixed-Size Chunking (core, 30m)
  [ ] 2.4 Recursive Chunking (optional, 45m)     <-- YOU ARE HERE
  [ ] 2.5 Semantic Chunking (optional, 45m)
  ...
```

Show a summary at the top: "Core path: ~11 hours | Full curriculum: ~35 hours | Your track: ~X hours remaining"

If the learner is short on time, suggest focusing on core lessons first: "You can skip optional lessons and come back to them later — the core path gives you everything you need to build a working RAG system."

This gives the learner a birds-eye view of the entire journey.

## Step 8: Motivational Close

End with an encouraging note based on their progress:
- If early: "You have taken the first steps — the concepts will start connecting soon."
- If mid-track: "You are building real skills. The pieces are coming together."
- If near completion: "You are close to the finish line. The advanced concepts are where RAG gets really powerful."
- If complete: "You have completed the curriculum. Consider building a production RAG system or contributing to the learning materials."

Suggest 2-3 relevant next steps using slash commands, tailored to the specific next action identified in the progress analysis above. For example:

- `/lesson [next lesson]` — continue where you left off in your current module
- `/quiz [weak topic]` — strengthen an area where your quiz scores were low
- `/challenge [appropriate level]` — put your skills to the test with a real-world challenge

## Guidelines

- Always be encouraging — progress tracking should motivate, not discourage
- If the learner has been inactive for a while, gently welcome them back without guilt
- Keep the display clean and scannable — learners should get the picture in seconds
- If data files are missing or incomplete, work with what is available and note what is missing
- Suggest variety in next steps — mix lessons, challenges, and hands-on building
