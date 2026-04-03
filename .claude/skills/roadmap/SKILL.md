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

Present a clear summary with module badges and time estimates:

```
RAG Learning Academy — Your Progress
=====================================
Track: [Beginner/Intermediate/Advanced]
Started: [date] | Days active: [N] | Streak: [N]d

Module Progress:
  [===========-------] 58% (21/36 lessons)

  Module 1: Foundations              [####] Complete        ~2h done
  Module 2: Document Processing      [####] Complete        ~3h done
  Module 3: Embeddings               [##--] 2/4 lessons    ~1.5h left
  Module 4: Vector Databases         [----] Not started     ~3h est.
  ...

  Time remaining on your track: ~8.5 hours
```

### Module Completion Badges

When a module is complete, show a badge next to it:

```
  Module 1: Foundations              [####] Complete   [FOUNDATIONS]
  Module 2: Document Processing      [####] Complete   [DATA WRANGLER]
  Module 3: Embeddings               [####] Complete   [VECTOR NAVIGATOR]
```

Badge names by module:
| Module | Badge |
|--------|-------|
| 1 | FOUNDATIONS |
| 2 | DATA WRANGLER |
| 3 | VECTOR NAVIGATOR |
| 4 | DB ARCHITECT |
| 5 | RETRIEVAL ENGINEER |
| 6 | PROMPT CRAFTER |
| 7 | QUALITY GUARDIAN |
| 8 | PATTERN MASTER |
| 9 | PRODUCTION READY |

### Time Estimates

Estimate time per module based on lesson count and type (core ~45min, optional ~30min). Show:
- Time spent (completed lessons)
- Time remaining (incomplete lessons in track)
- Total track estimate

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
- Module badges earned (list them)
- Current streak (read from `progress/streaks.md`)
- Longest streak
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

## Step 8: GitHub Badge Export

If the learner asks for a badge (e.g., says "badge" or "readme badge"), generate a shields.io markdown badge they can add to their README:

```markdown
![RAG Academy Progress](https://img.shields.io/badge/RAG_Academy-Module_5%2F9-8B5CF6?style=flat-square&logo=data:image/svg+xml;base64,...)
```

Generate the badge URL dynamically based on their actual progress:
- Color: `8B5CF6` (academy purple) for in-progress, `22C55E` (green) for complete
- Label: `RAG Academy`
- Message: `Module X/9` or `Complete` if all modules done
- Style: `flat-square`

Show them the markdown to copy-paste into their project's README.

## Step 9: Motivational Close

End with a brief, genuine note based on their progress. Follow the project's voice & tone — real encouragement, not cheerleading:

- If early: "You're just getting started but you've already got the foundation down. The pieces start clicking fast from here."
- If mid-track: "You're past the basics. The stuff you're learning now is what separates 'I followed a tutorial' from 'I actually understand RAG.'"
- If near completion: "You're close. The advanced stuff is where RAG gets genuinely interesting — and where most people never get to."
- If complete: "You've done the whole thing. You know more about RAG than most engineers building it in production. Seriously. Go build something real, or help improve these materials for the next person."

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
