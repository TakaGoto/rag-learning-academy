# Contributing to RAG Learning Academy

Thanks for your interest in contributing! Whether you're fixing a typo, adding an exercise, or improving an agent, your help makes this academy better for everyone learning RAG.

## Reporting Issues

- **Bug report** — [open one here](https://github.com/TakaGoto/rag-learning-academy/issues/new?template=bug_report.md). Include the slash command you ran, what you expected, and what happened.
- **Feature request** — [open one here](https://github.com/TakaGoto/rag-learning-academy/issues/new?template=feature_request.md). Describe the use case and why it would help learners.
- **Outdated content** — [open one here](https://github.com/TakaGoto/rag-learning-academy/issues/new?template=content_update.md). Flag deprecated models, changed APIs, or stale references. You can also run `/audit-content` in Claude Code to scan for issues.

## Development Setup

```bash
git clone https://github.com/TakaGoto/rag-learning-academy.git
cd rag-learning-academy
make install    # Install dependencies + dev tools (ruff, pytest, pyyaml)
make test       # Run 616 structural/content tests
make ci         # Full check: lint + shellcheck + tests
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b my-feature`)
3. Make your changes
4. Run `make ci` to verify everything passes (lint + shellcheck + 616 tests)
5. Open a pull request against `main`

The PR template will guide you through the checklist.

## What Makes a Good Contribution

- **Content updates** — fixing outdated info, improving explanations, adding references
- **New exercises** — hands-on tasks that reinforce curriculum concepts
- **Bug fixes** — broken commands, incorrect examples, test failures
- **Agent and skill improvements** — better prompts, clearer instructions, new diagnostic flows
- **New sample data** — realistic documents for chunking/retrieval practice
- **Test improvements** — new structural or content validation tests

## Content Guidelines

### Structure

- **Agents** must include all required sections: Role Overview, Core Philosophy, Key Responsibilities, Teaching Approach, Level Calibration, Common Misconceptions, When to Use This Agent, Delegation Rules
- **Skills** with overlapping scope must include a `> **Scope:**` blockquote (see `/evaluate` ↔ `/benchmark` for the pattern)
- **Curriculum lessons** must be tagged `core` or `optional` in the heading (e.g., `### 3.2 Choosing an Embedding Model — \`core\``)
- **New content files** must include `last_reviewed` frontmatter:
  ```yaml
  ---
  last_reviewed: 2026-03-21
  review_cycle: quarterly    # monthly, quarterly, or semi-annually
  staleness_risk: medium     # high, medium, or low
  ---
  ```

### Voice & Tone

The academy has a defined voice (see CLAUDE.md). Key points:

- Write like you're explaining to a smart friend, not writing a textbook
- Use "you" and "we", not "the learner" or "one should"
- Use contractions (you'll, it's, don't)
- Have opinions — "honestly, you probably don't need this yet" is better than "this may or may not be applicable"
- Keep encouragement real, not cheesy — no "Amazing job!" after every step
- Use everyday analogies before CS jargon
- It's okay to say "this part is boring but important"

### Milestones & Proficiency Levels

If you add or restructure curriculum content, check whether the [milestones](.claude/docs/reference/milestones.md) need updating. Milestones map to module completion and proficiency levels (RAG Explorer → Practitioner → Engineer → Architect).

## Code Style

- **Python:** Formatted and linted with [ruff](https://docs.astral.sh/ruff/) (`make lint`)
- **Shell scripts / hooks:** Checked with [shellcheck](https://www.shellcheck.net/) (`make shellcheck`)

## Available Make Commands

| Command | What It Does |
|---------|-------------|
| `make install` | Install dependencies + dev tools |
| `make test` | Run 616 academy infrastructure tests |
| `make test-all` | Run all tests including learner exercise tests |
| `make lint` | Check Python with ruff |
| `make format` | Auto-format Python with ruff |
| `make shellcheck` | Check hook scripts |
| `make ci` | Full check: lint + shellcheck + tests |
| `make dashboard` | Generate HTML progress dashboard |
| `make knowledge-check` | Run weekly knowledge check locally |
| `make clean` | Remove __pycache__ and .pyc files |

## Questions?

Open an issue or start a discussion. Happy to help you get started.
