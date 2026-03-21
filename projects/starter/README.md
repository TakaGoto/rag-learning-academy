# Starter Project: Simple Q&A Over Documents

Build a basic RAG pipeline that answers questions about a set of documents.

## Goal
Create a working RAG system that can:
1. Load and chunk a set of markdown/text documents
2. Generate embeddings and store them in ChromaDB
3. Retrieve relevant chunks for a user query
4. Generate an answer using Claude with retrieved context

## Prerequisites
- Module 1: Foundations (completed)
- Module 2: Document Processing (at least lesson 2.1-2.3)
- Module 3: Embeddings (at least lesson 3.1-3.2)

## Structure
```
starter/
├── README.md          # This file
├── ingest.py          # Document loading and chunking
├── embed.py           # Embedding generation and storage
├── retrieve.py        # Query and retrieval
├── generate.py        # Answer generation with LLM
├── pipeline.py        # End-to-end pipeline
├── config.py          # Configuration
└── docs/              # Sample documents to query
```

## Steps
1. Start with `config.py` — set up your embedding model and chunk size
2. Build `ingest.py` — load documents and split into chunks
3. Build `embed.py` — generate embeddings and store in Chroma
4. Build `retrieve.py` — implement similarity search
5. Build `generate.py` — create a RAG prompt and call Claude
6. Wire it all together in `pipeline.py`

## Success Criteria
- [ ] Can ingest at least 5 documents
- [ ] Retrieves relevant chunks (top-3 are on-topic)
- [ ] Generates accurate, grounded answers
- [ ] No hallucinated information in responses

## Hints
Use `/build` to get step-by-step guidance. Use `/debug-rag` if your pipeline isn't working as expected.
