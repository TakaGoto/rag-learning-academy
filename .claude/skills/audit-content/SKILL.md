---
name: audit-content
description: "Audit academy materials for outdated references, deprecated patterns, and stale content"
---

# Audit Content: Keep the Academy Current

> **Purpose:** Systematically check all academy materials for outdated information — deprecated models, changed APIs, superseded techniques, and stale references. Produces an actionable update report.

## Step 1: Determine Audit Scope

If the user specifies a scope (e.g., `/audit-content embeddings` or `/audit-content module 3`), audit only that area. Otherwise, run a full audit across all content.

**Full audit covers:**
- Curriculum modules (`.claude/docs/curriculum/`)
- Agent definitions (`.claude/agents/`)
- Reference docs (`.claude/docs/reference/`)
- Code rules (`.claude/rules/`)
- Sample data (`data/raw/`)
- Templates (`.claude/docs/templates/`)

## Step 2: Check Model References

Scan all content files for embedding and LLM model references. Verify each against current state:

| Model Reference | What to Check |
|----------------|---------------|
| `text-embedding-3-small` | Still recommended? Check OpenAI docs and MTEB leaderboard |
| `all-MiniLM-L6-v2` | Still a good free default? Check Sentence Transformers releases |
| `nomic-embed-text` | Still maintained and competitive? |
| `bge-base-en-v1.5` | Check if newer BGE versions exist |
| Claude model IDs | Verify against current Anthropic model IDs |
| GPT model IDs | Verify against current OpenAI model IDs |

Use `WebSearch` to check the MTEB leaderboard and model provider documentation for current recommendations.

## Step 3: Check Library and Framework References

Scan for library references and verify versions and API patterns:

| Library | What to Check |
|---------|---------------|
| `langchain` | Import patterns — should use `langchain-core`, `langchain-community`, or `langgraph` |
| `chromadb` | API compatibility — check for breaking changes |
| `ragas` | Current version and metric names |
| `sentence-transformers` | Current version and API |
| `llama-index` | Package rename or API changes |
| `pydantic` | v1 vs v2 patterns |

Use `WebSearch` to check changelogs and migration guides.

## Step 4: Check Paper and Technique References

Scan for research paper citations. Flag:
- Papers described as "recent" or "new" that are 2+ years old
- Techniques that have been superseded by newer approaches
- Benchmarks that have been replaced

Key papers to verify:
- Self-RAG, CRAG, HyDE, ColBERT, RAPTOR, GraphRAG
- Check if major new RAG techniques have emerged that aren't covered

Use `WebSearch` to check paper citation counts and newer follow-up work.

## Step 5: Check for Deprecated Patterns

Scan code examples and rules for deprecated patterns:
- Old-style LangChain imports (`from langchain import` instead of `from langchain_core`)
- Deprecated API parameters or function signatures
- Outdated best practices

## Step 6: Check Content Age

For each content file, check the git log to find when it was last updated. Flag files older than 90 days. Categorize by staleness risk:

| Risk Level | Review Cycle | Content Types |
|------------|-------------|---------------|
| **High** | Monthly | Model recommendations, library versions, MTEB references |
| **Medium** | Quarterly | Framework patterns, API examples, production tooling |
| **Low** | Semi-annually | Foundational concepts, algorithms, evaluation theory |

## Step 7: Generate Audit Report

Produce a structured report:

```markdown
# Content Audit Report — [Date]

## Summary
- Files audited: N
- Issues found: N (X critical, Y warnings, Z info)

## Critical (requires immediate update)
- [ ] Issue description — file path — suggested fix

## Warnings (review within 30 days)
- [ ] Issue description — file path — suggested fix

## Informational (consider updating)
- [ ] Issue description — file path — suggested fix

## Verified Current
- List of items confirmed as up-to-date

## Recommendations
- Prioritized list of updates to make
```

Save the report to `progress/audit-report-[date].md` if the user wants to track it.

Suggest 2-3 relevant next steps:

- `/lesson` — to update specific curriculum content based on findings
- `/explain` — to deep-dive into any new techniques discovered during the audit
- `/roadmap` — to see if the learning path needs adjustment based on ecosystem changes
