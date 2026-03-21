# Contributing to RAG Learning Academy

Thanks for your interest in contributing! Whether you're fixing a typo, adding an exercise, or improving an agent, your help makes this academy better for everyone learning RAG.

## Reporting Bugs

Found something broken? [Open a bug report](https://github.com/TakaGoto/rag-learning-academy/issues/new?template=bug_report.md) on GitHub Issues. Include the slash command you ran, what you expected, and what actually happened.

## Suggesting Features

Have an idea for a new skill, exercise, or improvement? [Open a feature request](https://github.com/TakaGoto/rag-learning-academy/issues/new?template=feature_request.md) on GitHub Issues. Describe the use case and why it would help learners.

## Development Setup

```bash
git clone https://github.com/TakaGoto/rag-learning-academy.git
cd rag-learning-academy
make install
make test
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b my-feature`)
3. Make your changes
4. Run `make ci` to verify everything passes
5. Open a pull request against `main`

## What Makes a Good Contribution

- **Content updates** -- fixing outdated information, improving explanations, adding references
- **New exercises** -- hands-on tasks that reinforce curriculum concepts
- **Bug fixes** -- broken commands, incorrect examples, test failures
- **Agent and skill improvements** -- better prompts, clearer instructions, new diagnostic flows

## Testing Requirements

All changes must pass the full test suite before merging:

```bash
make test
```

All 604 tests must pass. If you add new content (agents, skills, curriculum modules), new tests will be generated automatically -- make sure those pass too.

## Content Guidelines

- **Follow existing section patterns.** Look at similar files for structure and tone.
- **Agents must include all required sections:** Role Overview, Common Misconceptions, Level Calibration, Collaboration Framework, and any domain-specific sections.
- **Skills with overlapping scope** must include a scope blockquote explaining when to use this skill vs. the similar one.
- **New content files** should include `last_reviewed` frontmatter with the current date.

## Code Style

- **Python:** Formatted and linted with [ruff](https://docs.astral.sh/ruff/)
- **Shell scripts / hooks:** Checked with [shellcheck](https://www.shellcheck.net/)

Run `make lint` to check both before submitting.

## Questions?

Open an issue or start a discussion. We're happy to help you get started.
