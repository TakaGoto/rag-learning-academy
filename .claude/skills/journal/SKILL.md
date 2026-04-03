---
name: journal
description: "Write a quick note about what you learned or what confused you"
---

# Journal: Capture Your Thoughts

A lightweight way for learners to jot down what clicked, what confused them, or what they want to revisit. These notes feed back into the curriculum director's recommendations.

## Step 1: Get the Entry

If the learner provides text with the command (e.g., `/journal embeddings finally make sense — it's just coordinates in meaning space`), use that directly.

If no text is provided, prompt: "What's on your mind? Could be something that clicked, something confusing, a question for later, or just a note to yourself."

## Step 2: Categorize

Tag the entry with one of these categories based on content:

- **insight** — something that clicked or a connection they made
- **confusion** — something they don't understand yet
- **question** — something they want to explore later
- **idea** — a project idea or experiment they want to try
- **note** — general observation

## Step 3: Save the Entry

Append to `progress/journal.md`. Create the file if it doesn't exist.

Format:

```markdown
### [date] — [category]
[their entry text]
```

Keep their original words. Don't rewrite or polish — this is their voice, their notes.

## Step 4: Brief Response

Keep it short. Respond based on the category:

- **insight**: Acknowledge it. "Solid mental model. That analogy will serve you well when things get more complex."
- **confusion**: Normalize it and offer help. "That's a common sticking point. Want me to `/explain [topic]` from a different angle?"
- **question**: Acknowledge and bookmark. "Good question. We'll hit that in [relevant module]. Or run `/explain [topic]` now if you're curious."
- **idea**: Encourage it. "That's worth trying. When you're ready, `/sandbox` can help you prototype it."
- **note**: Just confirm. "Noted."

Don't turn this into a teaching moment unless they ask. The journal is for *them*, not for the system.
