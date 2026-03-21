---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# RAG Architecture Decision Document

> Use this template to document the architecture decisions for a RAG system. Fill in each section with your specific choices and rationale.

---

## Project Name

_[Your RAG project name]_

## Date

_[YYYY-MM-DD]_

## Author

_[Your name]_

## Status

_[Draft | In Review | Approved | Superseded by ___]_

---

## 1. Use Case

### Problem Statement
_What problem does this RAG system solve? What question(s) will it answer?_



### Target Users
_Who will use this system? Technical users, end customers, internal teams?_



### Query Patterns
_What types of questions will users ask? Provide 5-10 representative examples._

1.
2.
3.
4.
5.

### Success Criteria
_How will you know the system is working well? Define measurable targets._

| Metric | Target |
|---|---|
| Answer accuracy | _e.g., >90% on test set_ |
| Retrieval recall@5 | _e.g., >85%_ |
| Latency (P95) | _e.g., <3 seconds_ |
| Cost per query | _e.g., <$0.02_ |

---

## 2. Data Sources

### Document Inventory

| Source | Format | Volume | Update Frequency | Access Method |
|---|---|---|---|---|
| _e.g., Product docs_ | _Markdown_ | _500 pages_ | _Weekly_ | _Git repo_ |
| | | | | |
| | | | | |

### Data Characteristics
- **Languages:** _[e.g., English only, multilingual]_
- **Content types:** _[e.g., text, tables, images, code]_
- **Average document length:** _[e.g., 2000 words]_
- **Total corpus size:** _[e.g., 10,000 documents, ~50MB text]_

---

## 3. Architecture Components

### Document Processing

| Decision | Choice | Rationale |
|---|---|---|
| Parser | _e.g., Unstructured_ | _[Why this parser]_ |
| Chunking strategy | _e.g., Recursive, 512 tokens, 50 overlap_ | _[Why this strategy and size]_ |
| Text preprocessing | _e.g., Normalize whitespace, remove headers_ | _[What cleaning steps and why]_ |
| Metadata extracted | _e.g., Source, page, section, date_ | _[What metadata and why]_ |

### Embeddings

| Decision | Choice | Rationale |
|---|---|---|
| Embedding model | _e.g., text-embedding-3-small_ | _[Why this model]_ |
| Dimensions | _e.g., 1536_ | _[Why this dimensionality]_ |
| Batch size | _e.g., 100_ | _[Throughput vs rate limit balance]_ |
| Caching | _e.g., SQLite embedding cache_ | _[Caching strategy]_ |

### Vector Storage

| Decision | Choice | Rationale |
|---|---|---|
| Vector database | _e.g., ChromaDB_ | _[Why this database]_ |
| Index type | _e.g., HNSW, M=16, ef=200_ | _[Why these parameters]_ |
| Hosting | _e.g., Embedded / Self-hosted / Managed_ | _[Deployment model]_ |
| Backup strategy | _e.g., Daily snapshot to S3_ | _[Data protection]_ |

### Retrieval

| Decision | Choice | Rationale |
|---|---|---|
| Retrieval strategy | _e.g., Hybrid (dense + BM25, RRF)_ | _[Why hybrid]_ |
| Top-k | _e.g., 10 retrieve, rerank to 5_ | _[Why these numbers]_ |
| Reranker | _e.g., Cohere rerank-v3_ | _[Why this reranker]_ |
| Metadata filters | _e.g., Filter by source type, date range_ | _[What filters and why]_ |

### Generation

| Decision | Choice | Rationale |
|---|---|---|
| LLM | _e.g., Claude 3.5 Sonnet_ | _[Why this model]_ |
| Prompt strategy | _e.g., Stuff with citation instructions_ | _[Why this approach]_ |
| Max context tokens | _e.g., 4000 tokens for retrieved context_ | _[Budget allocation]_ |
| Citation format | _e.g., Inline [1], [2] with source list_ | _[Citation approach]_ |
| No-answer handling | _e.g., "I don't have enough information..."_ | _[Abstention strategy]_ |

---

## 4. Trade-Offs Considered

### Alternatives Evaluated

| Component | Option A | Option B | Chosen | Why |
|---|---|---|---|---|
| _e.g., Vector DB_ | _ChromaDB_ | _Pinecone_ | _ChromaDB_ | _Simpler ops, sufficient scale_ |
| | | | | |
| | | | | |

### Key Trade-Offs

_Document the major trade-offs you are making and why._

1. **[Trade-off 1]:** _e.g., Chose smaller embedding model (lower quality) for faster indexing and lower cost, acceptable given the homogeneous document corpus._
2. **[Trade-off 2]:**
3. **[Trade-off 3]:**

---

## 5. Infrastructure

### Deployment Model
_[Describe how the system will be deployed: serverless, containerized, VM-based, etc.]_



### Estimated Costs

| Component | Monthly Cost | Assumptions |
|---|---|---|
| Embedding API | _$XX_ | _X documents/month, Y tokens/doc_ |
| LLM API | _$XX_ | _X queries/month, Y tokens/query_ |
| Vector database | _$XX_ | _X vectors, Y queries/month_ |
| Infrastructure | _$XX_ | _Compute, storage, networking_ |
| **Total** | **$XX** | |

### Scaling Plan
_How will each component scale as usage grows? Identify the likely bottleneck._



---

## 6. Evaluation Plan

### Evaluation Dataset
_How will you create and maintain a test dataset?_



### Metrics and Targets

| Metric | Target | Measurement Frequency |
|---|---|---|
| Context Recall | _>0.85_ | _Weekly_ |
| Context Precision | _>0.80_ | _Weekly_ |
| Faithfulness | _>0.90_ | _Weekly_ |
| Answer Relevancy | _>0.85_ | _Weekly_ |
| End-to-end latency (P95) | _<3s_ | _Continuous_ |

### Monitoring
_What will you monitor in production and how?_



---

## 7. Open Questions and Risks

| Question / Risk | Impact | Mitigation |
|---|---|---|
| _e.g., Documents contain many tables_ | _Poor chunking quality_ | _Evaluate table-aware parsing_ |
| | | |
| | | |

---

## Approval

| Role | Name | Date | Decision |
|---|---|---|---|
| Technical Lead | | | _Approved / Rejected_ |
| Product Owner | | | _Approved / Rejected_ |
