---
name: triage
description: "Not sure where to start or what's wrong? Get routed to the right agent or skill."
---

# Triage: Find the Right Help

> **When to use this:** You're stuck, confused, or not sure which `/command` to run next. Triage asks a few quick questions and points you in the right direction.

## Step 1: Understand the Learner's Situation

Ask one question to categorize their need:

**"What best describes where you are right now?"**

1. **"I'm brand new to RAG"** → Suggest `/start` to begin their learning journey
2. **"I'm learning and want to study a topic"** → Go to Step 2 (Learning Path)
3. **"I'm building something and need help"** → Go to Step 3 (Building Path)
4. **"Something is broken / not working well"** → Go to Step 4 (Debugging Path)
5. **"I want to review or improve what I have"** → Go to Step 5 (Review Path)

## Step 2: Learning Path

Ask: **"What would you like to do?"**

| Goal | Recommended |
|------|-------------|
| Learn a concept step by step | `/lesson` |
| Get a quick definition | `/glossary [term]` |
| Understand something deeply | `/explain [concept]` |
| Test what I know | `/quiz [topic]` |
| See my progress | `/roadmap` |
| Read a research paper | `/paper-review` |
| Compare two approaches | `/compare` |

## Step 3: Building Path

Ask: **"What stage are you at?"**

| Stage | Recommended |
|-------|-------------|
| I haven't started building yet | `/build` — guided component construction |
| I need to design my system first | `/architecture` — design your RAG architecture |
| I want a real-world challenge | `/challenge` — open-ended project |
| I need help choosing between approaches | `/compare` — side-by-side comparison |

## Step 4: Debugging Path

Ask: **"What's the symptom?"**

| Symptom | Recommended |
|---------|-------------|
| Retrieved documents aren't relevant | `/debug-rag` → retrieval diagnosis |
| The LLM makes things up / hallucinates | `/debug-rag` → generation diagnosis |
| Results are slow or expensive | `/benchmark` → performance profiling |
| I'm not sure what's wrong, quality just feels off | `/evaluate` → measure with metrics first |
| I'm getting errors in my code | `/code-review` → get expert feedback |

## Step 5: Review Path

Ask: **"What would you like to review?"**

| Goal | Recommended |
|------|-------------|
| Get feedback on my code | `/code-review` |
| Measure my pipeline's quality | `/evaluate` |
| Check performance / speed / cost | `/benchmark` |
| See what to learn next | `/roadmap` |

## Step 6: Route and Hand Off

Once you've identified the right skill:

1. Briefly explain WHY you're suggesting that skill ("Based on what you described, `/debug-rag` is the best fit because it has a structured diagnostic process for retrieval issues.")
2. Ask if they'd like to proceed or if they had something else in mind.
3. If they confirm, tell them to run the suggested `/command`.

If none of the options fit, ask the learner to describe their situation in their own words and use your judgment to route them — you can also suggest they talk directly to a specific agent (e.g., "You might want to ask the chunking-strategist about that").

Suggest 2-3 relevant next steps:

- `/start` — if they haven't begun their learning journey yet
- `/roadmap` — to see their overall progress and recommended path
- The specific skill identified through triage
