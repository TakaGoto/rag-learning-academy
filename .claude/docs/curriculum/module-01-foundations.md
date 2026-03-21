---
last_reviewed: 2026-03-21
review_cycle: semi-annually
staleness_risk: low
---

# Module 01: RAG Foundations

## Module Objectives

By the end of this module, learners will be able to:

- Define Retrieval-Augmented Generation and explain its purpose
- Compare RAG with fine-tuning and prompt engineering approaches
- Identify all stages of the RAG pipeline and their responsibilities
- Build a minimal end-to-end RAG system from scratch
- Articulate when RAG is the right approach for a given problem

## Prerequisites

- Basic Python proficiency (functions, classes, file I/O)
- Familiarity with LLM APIs (OpenAI, Anthropic, or similar)
- A working Python 3.10+ environment with pip or uv

## Lessons

### 1.1 What is RAG

**Description:** Introduces the core idea of augmenting LLM generation with external knowledge retrieval. Covers the motivation behind RAG — LLMs have knowledge cutoffs, can hallucinate, and lack access to private data. RAG solves these problems by grounding generation in retrieved evidence.

**Key concepts:** Knowledge grounding, parametric vs non-parametric knowledge, the original RAG paper (Lewis et al., 2020), the retrieve-then-read paradigm.

**Duration:** 30 minutes

### 1.2 When to Use RAG

**Description:** Decision framework for choosing between RAG, fine-tuning, prompt engineering, and combinations. Covers scenarios where RAG excels (dynamic knowledge, private data, citation requirements) and where it may not be the best fit (pure reasoning tasks, latency-critical systems with no caching). Also covers where RAG falls short: mathematical computations (RAG retrieves text, it cannot calculate), large-scale summarization (retrieving top-k chunks cannot represent an entire corpus), cross-document comparisons in a single query, and stale indexes that require incremental re-indexing. Includes a decision tree learners can reference.

**Key concepts:** Build-vs-buy matrix, cost/latency/accuracy trade-offs, decision tree for approach selection, RAG + fine-tuning hybrid strategies.

**Duration:** 30 minutes

### 1.3 RAG Architecture Overview

**Description:** Walks through the complete RAG pipeline step by step: document ingestion, chunking, embedding, indexing in a vector store, retrieval at query time, context assembly, and LLM generation. Introduces the two-phase model: offline indexing and online query serving. Diagrams each phase with data flow annotations.

**Key concepts:** Indexing pipeline, query pipeline, retriever, generator, context window, pipeline orchestration, offline vs online phases.

**Duration:** 45 minutes

### 1.4 Your First RAG Pipeline (Hello World)

**Description:** Hands-on lesson building a minimal RAG system. Load a text file, chunk it naively by paragraphs, embed with OpenAI, store in ChromaDB, retrieve top-k results for a query, and generate an answer. No frameworks — raw Python to understand every step. Includes debugging tips for common first-timer issues.

**Key concepts:** End-to-end implementation, top-k retrieval, prompt construction with context, manual pipeline wiring.

**Duration:** 60 minutes

## Hands-On Exercises

1. **Concept Map:** Draw the RAG pipeline from document to answer, labeling each component and the data format at each stage (text, vectors, ranked list, prompt, response). Use a diagramming tool or pen and paper.

2. **Comparison Matrix:** Build a table comparing RAG, fine-tuning, and prompt engineering across 5 dimensions: cost, latency, accuracy, freshness, and implementation effort. Add a row for "RAG + fine-tuning" as a hybrid approach.

3. **Hello World RAG:** Implement a complete RAG pipeline over a single Wikipedia article using only `openai`, `chromadb`, and standard library modules. Answer 5 factual questions and evaluate correctness manually. Deliverable: a single Python script under 100 lines.

4. **Break It On Purpose:** Remove one pipeline stage at a time (skip chunking, use random vectors instead of embeddings, reduce top-k to 1, etc.) and observe how output quality degrades. Document your findings in a table mapping each degradation to its effect on answer quality.

5. **Architecture Sketch:** Given a scenario (e.g., "internal knowledge base for a 50-person company"), sketch the RAG architecture you would build, identifying specific tools for each stage. Justify your choices.

## Key Takeaways

- RAG bridges the gap between an LLM's static training data and the dynamic, private knowledge your application needs.
- The pipeline has clear stages (ingest, chunk, embed, index, retrieve, generate), each with its own failure modes — understanding every stage is essential for debugging.
- RAG is not a silver bullet; it trades latency and complexity for grounding and freshness. The decision to use RAG should be deliberate.
- A minimal RAG system can be built in under 50 lines of Python, making it an accessible starting point before introducing frameworks.
- The two-phase architecture (offline indexing, online serving) is fundamental — optimizations in later modules build on this structure.

## Suggested Reading

- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (2020)
- Anthropic's documentation on grounding and RAG best practices
- LangChain RAG tutorial (for framework comparison after building from scratch)

---

**Next:** [Module 02 — Document Processing](module-02-document-processing.md) →
