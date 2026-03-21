---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# Module 06: Generation

## Module Objectives

By the end of this module, learners will be able to:

- Design effective prompts that ground LLM responses in retrieved context
- Manage context window budgets across multiple retrieved passages and conversation history
- Implement citation and attribution systems that enable user verification
- Handle edge cases gracefully: no relevant results, contradictory sources, unanswerable questions
- Evaluate generation quality independently from retrieval quality

## Prerequisites

- Module 01: RAG Foundations (completed)
- Module 05: Retrieval Strategies (recommended)
- Experience with LLM API calls (chat completions, system/user/assistant messages)

### Before You Begin

Verify you're comfortable with these concepts from prior modules:

- [ ] How top-k retrieval returns ranked documents with relevance scores (Module 05)
- [ ] The retrieve-then-read paradigm and pipeline orchestration (Module 01)
- [ ] How metadata and source attribution are preserved through chunking (Module 02)
- [ ] Why hybrid search and reranking improve retrieval precision (Module 05)

## Lessons

### 6.1 RAG Prompt Design — `core`

**Description:** Crafting system and user prompts that effectively leverage retrieved context. Covers the anatomy of a RAG prompt: system instructions (role, behavior rules, output format), context block (retrieved chunks with source labels), user query, and output constraints. Explores template patterns: stuff-all-context (simplest), map-reduce (for large context), and refine (iterative improvement). Includes guidance on few-shot examples within RAG prompts and persona design.

**Key concepts:** System prompt design, context injection patterns, stuff/map-reduce/refine chains, few-shot examples in RAG, output format specification, temperature selection for RAG (start with 0 or 0.1 for factual answers — note: low temperature reduces randomness but does not prevent hallucination; grounding instructions matter more).

**Duration:** 60 minutes

### 6.2 Context Window Management — `optional`

**Description:** Practical strategies for fitting retrieved content into finite context windows. Covers token counting with tiktoken, budget allocation across components (system prompt: ~500 tokens, conversation history: ~1000 tokens, retrieved context: remainder minus generation budget), truncation strategies when context overflows, and selecting the optimal number of chunks. Discusses the lost-in-the-middle phenomenon and ordering strategies to mitigate it.

**Key concepts:** Token budget allocation, context window limits by model, chunk ordering (most relevant first vs edges), lost-in-the-middle effect, long-context models (100K+ tokens) and their trade-offs, adaptive chunk selection.

**Duration:** 45 minutes

### 6.3 Grounding Techniques — `core`

**Description:** Ensuring the LLM answers from the provided context rather than its parametric (trained) knowledge. Covers instruction-based grounding ("Answer ONLY based on the provided context"), chain-of-thought with evidence extraction ("First, identify relevant passages, then answer"), verification prompts ("Check if your answer is supported by the context"), and the grounding-creativity spectrum (strict factual vs exploratory synthesis).

**Key concepts:** Grounding instructions, parametric vs retrieved knowledge, faithfulness enforcement, hallucination prevention, evidence-based answering, chain-of-thought grounding.

**Duration:** 30 minutes

### 6.4 Citation and Attribution — `optional`

**Description:** Building systems that cite their sources, enabling user trust and fact-checking. Covers inline citation formats ([1], [Source: doc.pdf, p.3]), footnote-style attribution with full source details, structured JSON output with source references, and post-processing to verify citations (does the cited passage actually support the claim?). Discusses the UX of citations and how they affect user trust.

**Key concepts:** Inline citations, source attribution, citation verification, structured output with provenance, numbered source blocks, post-processing validation, citation accuracy metrics.

**Duration:** 45 minutes

### 6.5 Handling Edge Cases — `optional`

**Description:** Designing for when retrieval fails or context is ambiguous — the situations that separate demos from production systems. Covers: no relevant documents found (graceful "I don't have enough information to answer that"), contradictory sources (present both perspectives with citations), partial information (qualify the answer and note gaps), out-of-scope queries (polite redirect), and adversarial inputs (safety guardrails and input validation).

**Key concepts:** Abstention ("I don't know" responses), confidence signaling, contradiction resolution, partial answer qualification, scope boundaries, guardrails, input validation, fallback to general knowledge (when appropriate).

**Duration:** 45 minutes

## Hands-On Exercises

1. **Prompt Engineering Lab:** Write 5 different RAG prompt templates (stuff with citations, map-reduce, refine, chain-of-thought with evidence, structured JSON output). Test each template on the same 10 queries with the same retrieved context. Score each answer 1-5 on faithfulness, completeness, and readability. Identify the best template for different query types.

2. **Context Budget Calculator:** Build a `ContextBudget` class that takes a model's context limit, a system prompt, optional conversation history, and a list of chunks ranked by relevance. It returns the maximum number of chunks that fit within budget, respecting a generation reserve (default 1024 tokens). Test with 3 different models (4K, 16K, 128K context).

3. **Citation System:** Implement an end-to-end citation pipeline: (1) number each source chunk in the prompt, (2) instruct the LLM to cite by number, (3) parse the response to extract citation references, (4) verify each citation two ways — exact match (does [Source N] correspond to an actual retrieved chunk?) and semantic match (embed the claim and cited chunk, verify cosine similarity > 0.7). Report citation accuracy rate.

4. **Edge Case Test Suite:** Create 20 adversarial test cases across 5 categories: unanswerable questions (4), contradictory context (4), empty retrieval results (4), off-topic queries (4), and ambiguous questions (4). Run each through your RAG pipeline and evaluate whether the system handles each case gracefully. Document failures and implement fixes.

## Key Takeaways

- The generation prompt is the last mile of RAG — a poorly designed prompt can waste excellent retrieval results, while a great prompt can extract value even from imperfect retrieval.
- Context window management is a budget allocation problem: every token spent on one chunk is unavailable for another. Budget wisely and measure.
- Grounding instructions significantly reduce hallucination but cannot eliminate it entirely — always verify critical outputs and design for graceful failure.
- Citation systems build user trust and enable fact-checking; they should be a default feature, not an afterthought. Users who can verify answers trust the system more.
- Graceful handling of edge cases separates production-quality RAG from demos. Design for the failure path first — it is the path users will encounter most.

## Suggested Reading

- Anthropic's prompt engineering guide
- Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (2023)
- OpenAI Cookbook: RAG best practices

---

← **Previous:** [Module 05 — Retrieval Strategies](module-05-retrieval.md) | **Next:** [Module 07 — Evaluation](module-07-evaluation.md) →
