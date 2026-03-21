# Module 08: Advanced Patterns

## Module Objectives

By the end of this module, learners will be able to:

- Design agentic RAG systems with intelligent routing, iterative retrieval, and tool use
- Implement Graph RAG using knowledge graphs for structured multi-hop relationships
- Apply self-correcting retrieval patterns (Self-RAG, CRAG) to improve reliability
- Extend RAG to multi-modal data (images, tables, code snippets)
- Use advanced query strategies (HyDE, step-back prompting, query decomposition) to improve retrieval

## Prerequisites

- Modules 01-07 (completed) — this module builds on all prior material
- Familiarity with LLM function calling / tool use APIs
- Basic understanding of graph data structures (nodes, edges, traversal)

## Lessons

### 8.1 Agentic RAG

**Description:** Moving beyond single-shot retrieve-and-generate to agentic workflows where the LLM controls the retrieval process. The LLM decides when to retrieve, what to retrieve, and whether the retrieved context is sufficient — or whether to try again with a different strategy. Covers query routing (directing queries to specialized retrievers based on intent classification), iterative retrieval (retrieve-reflect-retrieve again until satisfied), and tool-augmented RAG (calculator, code execution, API calls alongside document retrieval).

**Key concepts:** Agent loop, query routing and intent classification, tool use alongside retrieval (calculator, code execution, API calls), structured data routing (directing "how many customers?" to SQL while "refund policy?" goes to vector search), iterative retrieval with reflection, LangGraph agent patterns, CrewAI patterns, retrieval as a tool.

**Duration:** 60 minutes

### 8.2 Graph RAG

**Description:** Combining knowledge graphs with vector retrieval to capture structured relationships that embedding similarity alone cannot represent. Extract entities and relationships from documents using LLMs, build a knowledge graph, then traverse the graph to retrieve context for multi-hop questions. Covers entity and relation extraction prompts, graph construction with NetworkX, graph traversal strategies (BFS, shortest path, subgraph extraction), and community detection for hierarchical summarization (Microsoft GraphRAG approach).

**Key concepts:** Knowledge graph construction, entity extraction, relation extraction, graph traversal (BFS, DFS), community detection (Leiden algorithm), hierarchical summarization, Neo4j, NetworkX, Microsoft GraphRAG pipeline.

**Duration:** 60 minutes

### 8.3 Self-RAG and CRAG

**Description:** Self-correcting retrieval-augmented generation patterns that add reflection loops for higher reliability. Self-RAG: the model generates special reflection tokens to (1) decide whether retrieval is needed, (2) evaluate retrieved passages for relevance, and (3) critique its own generation for faithfulness. CRAG (Corrective RAG): evaluates retrieval confidence and takes corrective action — web search fallback, query rewriting, or knowledge refinement — when the initial vector retrieval is insufficient.

**Key concepts:** Self-reflection loops, retrieval gate (retrieve or not), relevance scoring of retrieved passages, generation critique for faithfulness, corrective retrieval, web search fallback, query rewriting on failure, confidence calibration.

**Duration:** 45 minutes

### 8.4 Multi-Modal RAG

**Description:** Extending RAG beyond text to handle images, tables, and code. Image RAG: embed images with CLIP or SigLIP, retrieve relevant images alongside text. Table RAG: parse tables from documents, embed table descriptions or individual rows, query with natural language. Code RAG: embed code snippets with code-specific models, retrieve relevant functions or examples. ColPali: a recent approach that embeds document page images directly, bypassing OCR entirely.

**Key concepts:** Multi-modal embeddings, CLIP/SigLIP for image retrieval, vision-language models for image understanding, table parsing and embedding, code-specific embedding models, ColPali document understanding, mixed-modality retrieval pipelines.

**Duration:** 45 minutes

### 8.5 Advanced Query Strategies (HyDE, Step-Back)

**Description:** Sophisticated query transformation techniques that address the fundamental mismatch between how users phrase questions and how documents are written. HyDE: have the LLM generate a hypothetical answer, embed that answer (which reads like a document), and use it for retrieval. Step-back prompting: ask the LLM to identify the broader concept behind a specific query, then retrieve on the abstraction. Multi-query: generate multiple query variations and union or intersect results. Query decomposition: break complex questions into sub-questions and retrieve for each.

**Key concepts:** HyDE (Hypothetical Document Embeddings), step-back prompting, multi-query generation, query decomposition into sub-questions, query planning with LLMs, fusion of multi-query results.

**Duration:** 45 minutes

## Hands-On Exercises

1. **Agentic RAG Router:** Build a system with 3 specialized retrievers (technical documentation, FAQ, changelog). Implement an LLM-based router that classifies query intent and selects the appropriate retriever. Add a fallback path for ambiguous queries that searches all retrievers and merges results. Test with 20 queries spanning all categories.

2. **Mini Graph RAG:** Extract entities and relationships from 10 documents using an LLM with structured output (JSON). Build a knowledge graph with NetworkX. Implement a hybrid retriever that (1) identifies entities in the query, (2) traverses the graph for related entities and relationships, (3) combines graph context with vector-retrieved chunks. Test on 5 multi-hop questions that require connecting information across documents.

3. **Self-RAG Prototype:** Implement the Self-RAG decision flow: (1) decide whether retrieval is needed for this query, (2) if yes, retrieve and score each passage for relevance, (3) generate an answer using only relevant passages, (4) critique the generated response for faithfulness. Compare answer quality and faithfulness scores against standard (non-self-correcting) RAG on 15 test queries.

4. **HyDE Experiment:** Implement HyDE and evaluate it against standard query embedding on 30 test queries. Categorize queries by type (factoid, conceptual, procedural) and report retrieval precision@5 for each category with and without HyDE. Identify the query types where HyDE helps most and where it may actually hurt.

## Key Takeaways

- Advanced patterns add significant complexity; only adopt them when you have measured evidence that basic RAG (Modules 01-07) is insufficient for your specific use case and failure mode.
- Agentic RAG gives the LLM control over the retrieval process, enabling dynamic multi-step information gathering. It is the most impactful advanced pattern for general-purpose applications.
- Graph RAG excels at multi-hop reasoning over structured relationships (entity A relates to entity B which relates to entity C) that vector similarity search fundamentally cannot capture.
- Self-correcting patterns (Self-RAG, CRAG) improve reliability by adding reflection loops, at the cost of 2-3x more LLM calls and corresponding latency. Worth it for high-stakes applications.
- Query transformation (HyDE, step-back, multi-query) addresses the fundamental mismatch between question-style queries and document-style text. HyDE helps most for conceptual queries and least for factoid lookups.

## Suggested Reading

- Asai et al., "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection" (2023)
- Yan et al., "Corrective Retrieval Augmented Generation" (CRAG, 2024)
- Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" (Microsoft, 2024)
- Gao et al., "Precise Zero-Shot Dense Retrieval without Relevance Labels" (HyDE, 2022)
