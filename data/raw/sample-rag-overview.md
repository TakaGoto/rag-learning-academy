# Retrieval-Augmented Generation: An Overview

## What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that enhances Large Language Models (LLMs) by providing them with relevant external information at inference time. Instead of relying solely on the knowledge encoded in the model's weights during training, RAG systems retrieve relevant documents from a knowledge base and include them in the prompt context.

## The RAG Pipeline

A typical RAG pipeline consists of two main phases:

### Indexing Phase (Offline)
1. **Document Loading**: Ingest documents from various sources (PDFs, web pages, databases)
2. **Chunking**: Split documents into smaller, semantically meaningful pieces
3. **Embedding**: Convert text chunks into numerical vector representations
4. **Indexing**: Store vectors in a vector database for efficient similarity search

### Query Phase (Online)
1. **Query Embedding**: Convert the user's question into a vector
2. **Retrieval**: Find the most similar document chunks in the vector database
3. **Augmentation**: Insert retrieved chunks into the LLM's prompt as context
4. **Generation**: The LLM generates an answer grounded in the retrieved context

## Why RAG?

RAG addresses several limitations of standalone LLMs:

- **Knowledge Cutoff**: LLMs have a training data cutoff. RAG provides access to current information.
- **Hallucination**: By grounding responses in retrieved documents, RAG reduces fabricated answers.
- **Domain Specificity**: RAG enables LLMs to answer questions about private or specialized data.
- **Transparency**: Retrieved sources can be cited, making answers verifiable.
- **Cost**: Updating a knowledge base is cheaper than retraining or fine-tuning a model.

## RAG vs Fine-Tuning

| Aspect | RAG | Fine-Tuning |
|--------|-----|-------------|
| Knowledge updates | Instant (update docs) | Requires retraining |
| Cost | Lower (no GPU training) | Higher (compute intensive) |
| Transparency | Can cite sources | Black box |
| Best for | Factual Q&A, search | Style, format, behavior |

## Key Components

### Embedding Models
Embedding models convert text into dense vectors that capture semantic meaning. Popular choices include OpenAI's text-embedding-3-small, Cohere's embed-v3, and open-source models like BGE and E5.

### Vector Databases
Specialized databases optimized for similarity search over high-dimensional vectors. Examples include ChromaDB, Pinecone, Weaviate, Qdrant, and pgvector.

### Chunking Strategies
How documents are split significantly impacts retrieval quality:
- **Fixed-size**: Split by character/token count with overlap
- **Recursive**: Split by separators (paragraphs, sentences, words)
- **Semantic**: Split based on embedding similarity between sections
- **Document-aware**: Respect document structure (headers, sections)

### Retrieval Methods
- **Dense Retrieval**: Semantic similarity using embeddings
- **Sparse Retrieval**: Keyword matching (BM25, TF-IDF)
- **Hybrid**: Combine dense and sparse for best of both worlds
- **Reranking**: Use a cross-encoder to re-score initial results

## Common Challenges

1. **Chunk size trade-off**: Too small = missing context, too large = noise
2. **Embedding quality**: Wrong model or dimensions = poor retrieval
3. **Lost in the middle**: LLMs may ignore context in the middle of long prompts
4. **Multi-hop reasoning**: Questions requiring information from multiple sources
5. **Structured data**: Tables, charts, and code need special handling

## Evaluation

RAG evaluation measures quality across the pipeline:
- **Retrieval**: Precision, Recall, MRR, NDCG
- **Generation**: Faithfulness, Answer Relevancy, Correctness
- **End-to-end**: RAGAS framework combines multiple metrics
