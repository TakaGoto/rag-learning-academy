---
name: architecture
description: "Design a RAG architecture for a specific use case"
---

# Architecture: Design a RAG System for Your Use Case

Guide the learner through the process of designing a complete RAG architecture tailored to a specific use case. This skill builds system design thinking.

## Step 1: Understand the Use Case

Ask the learner to describe their use case. If they do not have one, offer example scenarios:

- Customer support chatbot over product documentation
- Legal document Q&A for a law firm
- Internal knowledge base for a software team
- Research paper search and synthesis
- Multilingual FAQ system for an e-commerce platform
- Code documentation assistant

For their use case, gather the following requirements:
1. **Document types**: What kinds of documents? (PDFs, HTML, code, structured data)
2. **Corpus size**: How many documents? Total size?
3. **Query patterns**: What kinds of questions will users ask?
4. **Accuracy requirements**: How critical is correctness? (casual chatbot vs. medical advice)
5. **Latency requirements**: What response time is acceptable?
6. **Scale**: How many queries per day? How often does the corpus update?
7. **Budget constraints**: Open-source only, or can you use paid APIs?

## Step 2: Walk Through Architecture Decisions

For each component, explain the options and help the learner choose:

### Document Processing
- File format handling and extraction
- Cleaning and preprocessing steps
- Metadata extraction strategy

### Chunking Strategy
- Fixed-size, semantic, document-structure, or hybrid
- Chunk size and overlap recommendations for their document types
- Metadata to attach to each chunk

### Embedding Model
- Open-source vs. API-based
- Model size vs. quality trade-off
- Domain-specific considerations (e.g., code embeddings, multilingual)

### Vector Database
- In-memory (FAISS, Chroma) vs. hosted (Pinecone, Weaviate) vs. self-hosted (Qdrant, Milvus)
- Filtering and metadata requirements
- Scale and cost considerations

### Retrieval Strategy
- Dense, sparse, or hybrid search
- Top-k selection and re-ranking
- Multi-stage retrieval if needed

### Generation Model
- Model selection (GPT-4, Claude, open-source)
- Prompt design for their use case
- Output format and guardrails

## Step 3: Produce the Architecture Diagram

Create an ASCII architecture diagram showing the full pipeline:

```
  Documents          Ingestion Pipeline          Query Pipeline
  ---------          ------------------          --------------
  [PDFs]  --->  [ Loader ] --> [ Chunker ]       [ User Query ]
  [HTML]  --->  [ Cleaner ] -> [ Embedder ]          |
  [Docs]  --->  [ Metadata ]      |              [ Embedder ]
                                  v                  |
                            [ Vector DB ] <--- [ Retriever ]
                                                     |
                                               [ Re-ranker ]
                                                     |
                                               [ Generator ]
                                                     |
                                                [ Answer ]
```

Customize the diagram to match their specific architecture decisions.

## Step 4: Create the Decision Document

Generate a structured architecture decision document saved to `projects/[project-name]/architecture.md`:

```markdown
# RAG Architecture: [Use Case Name]

## Requirements Summary
[bulleted list from Step 1]

## Architecture Decisions
[for each component: choice, rationale, alternatives considered]

## Architecture Diagram
[ASCII diagram from Step 3]

## Implementation Plan
[ordered list of components to build, with estimated effort]

## Risks and Mitigations
[key risks and how to address them]
```

## Step 5: Implementation Roadmap

Break the architecture into buildable stages:
1. **MVP**: Minimum viable pipeline (basic chunking + embeddings + simple retrieval)
2. **V1**: Add proper chunking, metadata, and prompt engineering
3. **V2**: Add evaluation, re-ranking, and hybrid search
4. **Production**: Add caching, monitoring, error handling, and scaling

For each stage, suggest which `/build` exercises to complete.

## Step 6: Review and Iterate

Ask the learner if anything does not feel right or if they have concerns. Architecture is iterative — encourage them to revisit this document as they build and learn. Update `progress/module-tracker.md` to note the architecture exercise.

Suggest 2-3 relevant next steps using slash commands:

- `/build` — start building the MVP stage of your architecture
- `/challenge` — take on a real-world challenge that puts your architecture to the test
- `/compare` — compare alternative approaches for any component you are uncertain about

## Guidelines

- There is no single correct architecture — help the learner understand trade-offs
- Start simple and add complexity only when needed
- Always consider cost, maintainability, and the learner's current skill level
- Connect architecture decisions back to curriculum concepts
