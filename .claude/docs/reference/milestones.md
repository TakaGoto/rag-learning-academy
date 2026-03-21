---
last_reviewed: 2026-03-21
review_cycle: semi-annually
staleness_risk: low
---

# Milestones

The curriculum is long — milestones break it into satisfying checkpoints so you can see real progress along the way. Each milestone represents a meaningful capability, not just a box checked.

## How Milestones Work

- Complete the requirements listed under each milestone
- When you finish, `/roadmap` will show your milestone achievements
- Milestones unlock in order within your track but you can work ahead
- Each milestone ends with a concrete deliverable — something you built, not just read about

---

## Milestone 1: First Light

> *You built a working RAG system from scratch.*

**Requirements:**
- [ ] Complete Module 01 (all 4 lessons)
- [ ] Pass the Module 01 quiz with 70%+
- [ ] Complete the "Hello World RAG" exercise (a working pipeline in <100 lines)

**You can now:** Explain what RAG is, when to use it, and build a minimal pipeline end-to-end.

**Deliverable:** A Python script that answers questions about a document using retrieval.

---

## Milestone 2: Data Wrangler

> *You can turn any document into retrieval-ready chunks.*

**Requirements:**
- [ ] Complete Module 02 (all 5 lessons)
- [ ] Complete the "Multi-Format Parser" exercise
- [ ] Complete the "Chunking Comparison" exercise (compare 3+ strategies with metrics)

**You can now:** Parse PDFs, HTML, and markdown; choose the right chunking strategy; preserve metadata through the pipeline.

**Deliverable:** A document processing pipeline that handles multiple formats and outputs clean, metadata-rich chunks.

---

## Milestone 3: Vector Navigator

> *You understand embeddings and can store/search them effectively.*

**Requirements:**
- [ ] Complete Module 03 (all 5 lessons)
- [ ] Complete Module 04 (all 5 lessons)
- [ ] Complete the "Model Shootout" exercise (compare 3+ embedding models)
- [ ] Complete the "ChromaDB CRUD" exercise
- [ ] Pass a quiz on embeddings OR vector databases with 70%+

**You can now:** Choose an embedding model, explain cosine similarity, set up a vector database, and run similarity searches with metadata filtering.

**Deliverable:** A vector store loaded with embedded documents, queryable with filters.

---

## Milestone 4: Retrieval Engineer

> *You can find the right information for any query.*

**Requirements:**
- [ ] Complete Module 05 (all 5 lessons)
- [ ] Complete the "Hybrid Retriever" exercise (BM25 + dense retrieval)
- [ ] Complete 1 intermediate challenge (challenges 4-7)

**You can now:** Implement dense, sparse, and hybrid retrieval; add reranking; use MMR for diversity; optimize query handling.

**Deliverable:** A hybrid retrieval pipeline with reranking that demonstrably outperforms naive dense search.

---

## Milestone 5: Prompt Architect

> *Your RAG system generates grounded, cited answers.*

**Requirements:**
- [ ] Complete Module 06 (all 5 lessons)
- [ ] Complete the "Citation System" exercise
- [ ] Complete the "Edge Case Suite" exercise

**You can now:** Design effective RAG prompts, manage context windows, enforce source attribution, and handle edge cases (no relevant context, contradictory sources, ambiguous queries).

**Deliverable:** A generation layer with citation support and graceful handling of out-of-scope questions.

---

## Milestone 6: Quality Guardian

> *You measure everything and improve with data.*

**Requirements:**
- [ ] Complete Module 07 (all 5 lessons)
- [ ] Complete the "Metrics from Scratch" exercise
- [ ] Complete the "RAGAS Evaluation" exercise
- [ ] Run `/evaluate` on your pipeline with a test set of 20+ questions

**You can now:** Compute retrieval and generation metrics, build evaluation datasets, identify failure modes, and run regression tests.

**Deliverable:** An evaluation report showing retrieval precision/recall and generation faithfulness/relevancy scores.

---

## Milestone 7: Pattern Master

> *You know when and how to go beyond basic RAG.*

**Requirements:**
- [ ] Complete Module 08 (all 5 lessons)
- [ ] Complete 1 advanced challenge (challenges 8-11)
- [ ] Complete the "Self-RAG Prototype" or "Mini Graph RAG" exercise

**You can now:** Implement agentic RAG routing, knowledge graph integration, self-correction loops, and multi-modal retrieval. More importantly, you know when NOT to use these patterns.

**Deliverable:** A working implementation of at least one advanced RAG pattern with evaluation showing measurable improvement over your baseline.

---

## Milestone 8: Production Ready

> *You can deploy, monitor, and scale a RAG system.*

**Requirements:**
- [ ] Complete Module 09 (all 5 lessons)
- [ ] Complete the "Production API" exercise (FastAPI service)
- [ ] Complete the "Monitoring Dashboard" exercise
- [ ] Complete the "Cost Model" exercise

**You can now:** Deploy a RAG system behind an API, add caching for performance, monitor quality in production, estimate and optimize costs, and scale to handle real traffic.

**Deliverable:** A deployed RAG API with caching, monitoring, and a cost projection.

---

## Proficiency Levels

Proficiency levels are earned by completing milestones. They answer the question: *"How good am I at RAG now?"*

When you earn a new level, `/roadmap` will celebrate it. These are cumulative — each level builds on the previous one.

### RAG Explorer

> *You understand RAG and can build a working system.*

**Earned when:** Milestones 1 + 2 complete

You can explain what RAG is, when to use it, process documents into retrieval-ready chunks, and build a basic pipeline end-to-end. You're ready to go deeper.

### RAG Practitioner

> *You can design and build real retrieval systems.*

**Earned when:** Milestones 3 + 4 + 5 complete

You can choose embedding models, set up vector databases, implement hybrid retrieval with reranking, and build generation layers with citations and grounding. Your systems return relevant, sourced answers.

### RAG Engineer

> *You build systems that improve with data, not guesses.*

**Earned when:** Milestones 6 + 7 complete

You can evaluate every component of your pipeline with metrics, identify failure modes, and apply advanced patterns (agentic RAG, Graph RAG, self-correction) when the data justifies the complexity. You make decisions based on measurement.

### RAG Architect

> *You can ship RAG to production and keep it running.*

**Earned when:** Milestone 8 + at least 1 bonus milestone (Reviewer, Debugger, or Completionist)

You can deploy, cache, monitor, and scale RAG systems. You've also gone beyond the curriculum — engaging with research, building diagnostic instincts, or completing the full academy. You can design RAG systems for real-world use cases and mentor others.

---

## Track Milestones

Not everyone does all 8. Here's which milestones and levels each track covers:

| Track | Milestones | Level Earned | Estimated Hours |
|-------|-----------|--------------|-----------------|
| **Beginner** (Modules 1-4) | 1 → 2 → 3 | RAG Explorer | 15-25 hours |
| **Intermediate** (Modules 3-7) | 3 → 4 → 5 → 6 | RAG Practitioner | 25-40 hours |
| **Advanced** (Modules 6-9) | 5 → 6 → 7 → 8 | RAG Engineer | 30-45 hours |
| **Full curriculum** (Modules 1-9) | 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 | RAG Architect* | 60-90 hours |

*\*RAG Architect requires completing at least 1 bonus milestone in addition to all 8 core milestones.*

Milestones overlap across tracks intentionally — an intermediate learner picking up at Milestone 3 already has the skills from Milestones 1-2.

---

## Bonus Milestones

These are optional achievements for learners who go beyond the curriculum:

### Reviewer
> *You've engaged with RAG research.*

- [ ] Complete 3 paper reviews via `/paper-review`
- [ ] Identify 1 technique from a paper and implement it

### Debugger
> *You've developed strong diagnostic instincts.*

- [ ] Complete 5 debugging sessions via `/debug-rag`
- [ ] Document 3 failure modes and their fixes

### Completionist
> *You've done everything.*

- [ ] All 8 core milestones complete
- [ ] All 11 challenges completed
- [ ] All 9 module quizzes passed with 80%+
- [ ] At least 3 paper reviews
- [ ] Run `/audit-content` and submitted a content update
