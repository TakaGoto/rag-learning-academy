# Intermediate Project: Multi-Source Hybrid RAG

Build a hybrid RAG system that combines dense and sparse retrieval across multiple document types.

## Goal
Create a RAG system that can:
1. Parse multiple document formats (PDF, markdown, HTML)
2. Use semantic chunking with metadata preservation
3. Implement hybrid search (BM25 + dense embeddings)
4. Rerank results with a cross-encoder
5. Generate cited answers with source attribution

## Prerequisites
- Modules 1-5 completed
- Module 6 (at least lesson 6.1-6.3)
- Starter project completed

## Structure
```
intermediate/
├── README.md              # This file
├── parsers/               # Document format parsers
│   ├── pdf_parser.py
│   ├── html_parser.py
│   └── markdown_parser.py
├── chunking/              # Semantic chunking
│   └── semantic_chunker.py
├── retrieval/             # Hybrid retrieval
│   ├── dense_retriever.py
│   ├── sparse_retriever.py
│   ├── hybrid_retriever.py
│   └── reranker.py
├── generation/            # Cited generation
│   └── cited_generator.py
├── pipeline.py            # End-to-end pipeline
├── evaluate.py            # Evaluation script
└── config.yaml            # Configuration
```

## Steps
1. Build parsers for each document format
2. Implement semantic chunking with overlap
3. Set up dual retrieval (dense + BM25)
4. Add reciprocal rank fusion
5. Integrate cross-encoder reranking
6. Build cited generation with source references
7. Evaluate with RAGAS

## Success Criteria
- [ ] Handles PDF, markdown, and HTML inputs
- [ ] Hybrid search outperforms dense-only on test queries
- [ ] Reranking improves precision@5
- [ ] Generated answers include [Source: filename] citations
- [ ] RAGAS faithfulness score > 0.8

## Hints
Use `/compare dense vs hybrid` to understand the trade-offs. Use `/evaluate` to run metrics.
