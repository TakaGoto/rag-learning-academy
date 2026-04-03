---
name: lesson
description: "Start or continue a curriculum lesson"
---

# Lesson: Learn a RAG Concept Step by Step

> **Scope:** This skill **teaches new concepts** through structured lessons with explanations and exercises. To test what you already know, use `/quiz`.

This skill delivers structured curriculum lessons. Each lesson follows a consistent flow that builds understanding through explanation, examples, and hands-on practice.

> **Language awareness:** See `.claude/LANGUAGE_AWARENESS.md`.

## Step 1: Determine Which Lesson to Load

- If the user provides a module number and lesson name (e.g., `/lesson 3 chunking-strategies`), load that specific lesson.
- If no argument is given, read `progress/learner-profile.md` and `progress/module-tracker.md` to find the next incomplete lesson in the learner's track.
- If no profile exists, suggest running `/start` first.

**Resuming an incomplete lesson:** If the next incomplete lesson is the same one the learner's `module-tracker.md` shows as their current lesson (i.e., they started it before but it's not marked complete), ask:

> "Looks like you started **[lesson name]** last time but didn't finish. Want to **pick up where you left off** (I'll give you a quick recap and jump ahead), or **start fresh**?"

- If they want to resume: give a 2-3 sentence recap of the key points covered so far, then jump to the next undelivered section.
- If they want to start fresh: begin the lesson from the top as normal.

## Step 2: Load Lesson Content

Look for the lesson content in `.claude/docs/curriculum/`. The curriculum is organized as flat module files:
- `module-01-foundations.md`, `module-02-document-processing.md`, etc.
- Each module file contains multiple lesson sections within it.

Load the module file (e.g., `.claude/docs/curriculum/module-01-foundations.md`) and navigate to the specific lesson section within it. If the module file exists, use it as the primary source. If it does not exist yet, generate the lesson content based on the module topic and RAG curriculum structure.

## Pacing: Section-by-Section Delivery

**Do NOT deliver the entire lesson in one message.** Break it into sections and pause between each one. This prevents wall-of-text overload and lets the learner absorb each piece before moving on.

After each section below, **stop and wait** for the learner to say "next", "continue", "got it", or similar before proceeding to the next section. If they ask a question or seem confused, address it before moving on.

At the start of the lesson, tell the learner:
> "I'll walk you through this lesson one section at a time. Say **next** when you're ready to continue, or ask questions anytime."

## Step 3: Section 1 — Opening (Why This Matters)

Note the lesson's classification and estimated time from the curriculum file heading (e.g., `### 3.2 Choosing an Embedding Model — \`core\``). Display it at the top:

- For core lessons: "This is a **core** lesson (~45 min) — essential for building a working RAG system."
- For optional lessons: "This is an **optional** lesson (~45 min) — a deeper dive that builds on the core path. You can skip it and come back later."

Start with a real-world scenario or problem that this concept solves. Make it concrete and relatable. Keep it short — 3-5 sentences max.

**Then stop and wait for the learner.**

## Step 4: Section 2 — Core Explanation

Explain the concept clearly. Use analogies where helpful. Break complex ideas into digestible pieces. Include diagrams in ASCII where they add clarity.

If the explanation is long (more than ~15 lines), split it into two messages with a pause between them.

End with a quick gut-check: "Make sense so far?" or "Any questions before we look at code?"

**Then stop and wait for the learner.**

## Step 5: Section 3 — Code Example

Provide a working code example in the learner's chosen language that demonstrates the concept. Use comments to explain each section. Keep dependencies minimal — use common RAG libraries for the learner's language (see `language-support.md` for mappings).

**First hands-on lesson check:** If this is the first lesson that requires running code, check if the learner's environment is set up. Guide them through the setup for their chosen language (see `language-support.md` for setup commands per language) before showing the code.

Walk through the code briefly after showing it — highlight the key lines and explain what they do.

**Then stop and wait for the learner.**

## Step 6: Section 4 — Key Takeaways

Summarize the 3-5 most important points from the lesson in a bulleted list.

**Then stop and wait for the learner.**

## Step 7: Section 5 — Hands-On Exercise

Present a practical exercise that reinforces the lesson:
- Clearly state the objective
- Provide starter code or a template
- Define what "done" looks like
- Offer hints if the learner asks

**Then wait for the learner to share their solution.** Review it when they do — what they did well, what could be improved, and why. If they need more time, that's fine. If they want to skip the exercise, let them.

## Step 8: Section 6 — Check Understanding

Ask 2-3 quick comprehension questions to verify the learner grasped the key ideas. These should be conversational, not quiz-style. Correct any misconceptions gently.

## Step 9: Track Progress

Update `progress/module-tracker.md` to mark this lesson as complete. Add the completion date.

### Streak Update

Read `progress/streaks.md`. If it exists, update the last activity date to today. If today is the day after the last activity, increment the streak. If there's a gap, reset to 1. If the file doesn't exist, create it with streak: 1.

### Module Checkpoint Quiz

If this lesson completes a module (all lessons in the module are now marked done):

1. Congratulate the learner: "Module [N] complete! Before you move on, let's do a quick checkpoint."
2. Ask 3 short questions covering the module's key concepts. Mix types: one conceptual, one scenario, one true/false.
3. Grade gently. If they get 2-3 right: "Solid. You're ready for the next module."  If 0-1: "A couple gaps — no problem. Want to revisit anything before moving on, or push forward and come back later?"
4. Don't block progression. This is a temperature check, not a gate.

If the lesson does NOT complete a module, skip the checkpoint and suggest next steps normally.

Suggest 2-3 relevant next steps using slash commands:

- `/quiz` — test your understanding of the concepts from this lesson
- `/build` — apply what you learned by building a hands-on component
- `/lesson` — continue to the next lesson in your track

## Tone and Style

- Be encouraging but not patronizing
- Prefer concrete examples over abstract theory
- If the learner seems confused, offer a simpler explanation before moving on
- Celebrate progress — each lesson completed is a step forward
- **Respect the learner's pace** — never rush through sections or skip the pauses
