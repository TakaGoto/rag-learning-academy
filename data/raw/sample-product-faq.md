# AcmeSearch Product FAQ

Frequently asked questions about AcmeSearch, a fictional RAG-as-a-Service platform. Use this document to practice metadata filtering by section.

---

## Pricing

**Q: What plans are available?**
A: AcmeSearch offers three tiers: Free (1,000 queries/month, 10 MB storage), Pro ($49/month, 50,000 queries, 1 GB storage), and Enterprise (custom pricing, unlimited queries, dedicated infrastructure).

**Q: Is there a free trial for Pro?**
A: Yes. Every new account starts with a 14-day Pro trial. No credit card required.

**Q: How is query usage counted?**
A: Each call to the `/search` or `/ask` endpoint counts as one query. Indexing operations do not count toward the query limit.

## Features

**Q: Which embedding models are supported?**
A: We support OpenAI text-embedding-3-small, text-embedding-3-large, Cohere embed-v3, and any Sentence Transformers model via ONNX import.

**Q: Can I use hybrid search?**
A: Yes. Pro and Enterprise plans include BM25 + dense hybrid retrieval with configurable fusion weights.

**Q: Does AcmeSearch support metadata filtering?**
A: Yes. You can attach arbitrary key-value metadata to documents and filter on it at query time using a JSON filter expression.

## Setup

**Q: How do I create an index?**
A: Send a POST request to `/v1/indexes` with a name and embedding dimension. Example: `{"name": "docs", "dimension": 1536}`.

**Q: How do I upload documents?**
A: Use the `/v1/indexes/{name}/documents` endpoint with a JSON body containing `text` and optional `metadata` fields. Batch uploads accept up to 100 documents per request.

**Q: What file formats can I ingest directly?**
A: PDF, Markdown, plain text, and HTML. Other formats should be converted to text before ingestion.

## Troubleshooting

**Q: Why are my search results irrelevant?**
A: Common causes: (1) chunk size too large -- try 300-500 tokens, (2) wrong embedding model -- ensure query and document embeddings use the same model, (3) missing metadata filters for scoped queries.

**Q: Why is indexing slow?**
A: Large batch sizes or high-dimensional embeddings increase indexing time. Try reducing batch size to 50 and verify your embedding dimensions match the index configuration.

**Q: I get a 429 error. What does it mean?**
A: HTTP 429 means you have exceeded your plan's rate limit. Wait and retry with exponential backoff, or upgrade your plan for higher limits.
