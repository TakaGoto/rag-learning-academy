# RAG Evaluation Report

> Use this template to document the results of a RAG pipeline evaluation run.

---

## Report Metadata

| Field | Value |
|---|---|
| **Project** | _[Project name]_ |
| **Date** | _[YYYY-MM-DD]_ |
| **Evaluator** | _[Your name]_ |
| **Pipeline Version** | _[Git commit hash or version tag]_ |
| **Purpose** | _[e.g., Baseline measurement, post-optimization, regression check]_ |

---

## 1. Evaluation Dataset

### Dataset Description

| Property | Value |
|---|---|
| Dataset name | _[e.g., product-docs-eval-v2]_ |
| Total questions | _[e.g., 100]_ |
| Source documents | _[e.g., 500 product documentation pages]_ |
| Question types | _[e.g., 40 factoid, 25 multi-hop, 20 comparison, 15 aggregation]_ |
| Creation method | _[e.g., LLM-generated + human-reviewed]_ |
| Ground truth | _[e.g., Human-annotated reference answers and relevant passages]_ |

### Dataset Quality Notes
_Any known limitations, biases, or gaps in the evaluation dataset._



### Question Type Distribution

| Type | Count | Description |
|---|---|---|
| Factoid | _XX_ | Single-fact lookup questions |
| Multi-hop | _XX_ | Require combining information from multiple chunks |
| Comparison | _XX_ | Compare two or more entities or concepts |
| Aggregation | _XX_ | Summarize or count across multiple documents |
| Yes/No | _XX_ | Binary answer questions |
| Unanswerable | _XX_ | Answer is not in the corpus (tests abstention) |

---

## 2. Pipeline Configuration

_Document the exact configuration of the pipeline being evaluated._

| Component | Configuration |
|---|---|
| Embedding model | _[e.g., text-embedding-3-small, 1536d]_ |
| Chunk size | _[e.g., 512 tokens, 50 token overlap]_ |
| Chunking strategy | _[e.g., Recursive]_ |
| Vector database | _[e.g., ChromaDB, HNSW]_ |
| Retrieval strategy | _[e.g., Hybrid (dense + BM25, RRF alpha=0.5)]_ |
| Top-k retrieved | _[e.g., 10]_ |
| Reranker | _[e.g., Cohere rerank-v3, top 5 after reranking]_ |
| LLM | _[e.g., Claude 3.5 Sonnet]_ |
| Prompt template | _[e.g., Stuff with citations, system prompt v3]_ |

---

## 3. Retrieval Metrics

| Metric | Score | Target | Status |
|---|---|---|---|
| Context Precision@5 | _X.XX_ | _>0.80_ | _Pass/Fail_ |
| Context Recall@5 | _X.XX_ | _>0.85_ | _Pass/Fail_ |
| MRR | _X.XX_ | _>0.70_ | _Pass/Fail_ |
| NDCG@5 | _X.XX_ | _>0.75_ | _Pass/Fail_ |
| Hit Rate@5 | _X.XX_ | _>0.90_ | _Pass/Fail_ |

### Retrieval Performance by Question Type

| Question Type | Precision@5 | Recall@5 | MRR | Notes |
|---|---|---|---|---|
| Factoid | _X.XX_ | _X.XX_ | _X.XX_ | |
| Multi-hop | _X.XX_ | _X.XX_ | _X.XX_ | |
| Comparison | _X.XX_ | _X.XX_ | _X.XX_ | |
| Aggregation | _X.XX_ | _X.XX_ | _X.XX_ | |

### Retrieval Failure Analysis
_Identify the top 5 retrieval failures and their root causes._

| # | Query | Expected Chunk | Retrieved Rank | Root Cause |
|---|---|---|---|---|
| 1 | _[Query text]_ | _[Expected chunk ID]_ | _[Rank or "Not found"]_ | _[e.g., vocabulary mismatch]_ |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## 4. Generation Metrics

| Metric | Score | Target | Status |
|---|---|---|---|
| Faithfulness | _X.XX_ | _>0.90_ | _Pass/Fail_ |
| Answer Relevancy | _X.XX_ | _>0.85_ | _Pass/Fail_ |
| Answer Correctness | _X.XX_ | _>0.80_ | _Pass/Fail_ |

### Generation Performance by Question Type

| Question Type | Faithfulness | Relevancy | Correctness | Notes |
|---|---|---|---|---|
| Factoid | _X.XX_ | _X.XX_ | _X.XX_ | |
| Multi-hop | _X.XX_ | _X.XX_ | _X.XX_ | |
| Comparison | _X.XX_ | _X.XX_ | _X.XX_ | |
| Aggregation | _X.XX_ | _X.XX_ | _X.XX_ | |
| Unanswerable | _N/A_ | _N/A_ | _X.XX_ | _Abstention rate: XX%_ |

### Hallucination Analysis
_Identify instances where the model generated unfaithful content._

| # | Query | Hallucinated Claim | Retrieved Context Supported? | Severity |
|---|---|---|---|---|
| 1 | _[Query]_ | _[Claim]_ | _No_ | _High/Medium/Low_ |
| 2 | | | | |
| 3 | | | | |

---

## 5. End-to-End Metrics

| Metric | Value |
|---|---|
| Overall RAGAS score | _X.XX_ |
| Average latency (P50) | _X.XX seconds_ |
| Average latency (P95) | _X.XX seconds_ |
| Average cost per query | _$X.XXXX_ |
| Total evaluation cost | _$X.XX_ |

### Latency Breakdown

| Stage | P50 (ms) | P95 (ms) | % of Total |
|---|---|---|---|
| Query embedding | _XX_ | _XX_ | _XX%_ |
| Vector retrieval | _XX_ | _XX_ | _XX%_ |
| Reranking | _XX_ | _XX_ | _XX%_ |
| LLM generation | _XX_ | _XX_ | _XX%_ |
| **Total** | **XX** | **XX** | **100%** |

---

## 6. Comparison with Previous Evaluation

_If this is not the first evaluation, compare with the most recent prior run._

| Metric | Previous | Current | Delta | Significant? |
|---|---|---|---|---|
| Context Recall@5 | _X.XX_ | _X.XX_ | _+/-X.XX_ | _Yes/No_ |
| Faithfulness | _X.XX_ | _X.XX_ | _+/-X.XX_ | _Yes/No_ |
| Answer Correctness | _X.XX_ | _X.XX_ | _+/-X.XX_ | _Yes/No_ |
| P95 Latency | _X.XX s_ | _X.XX s_ | _+/-X.XX_ | _Yes/No_ |

### What Changed Between Evaluations
_List the pipeline changes made since the last evaluation._

1.
2.
3.

---

## 7. Analysis and Findings

### Strengths
_What is working well?_

1.
2.
3.

### Weaknesses
_What needs improvement?_

1.
2.
3.

### Root Cause Analysis
_For the weakest metric, what is the root cause?_



---

## 8. Recommendations

### Immediate Actions (This Sprint)

| # | Action | Expected Impact | Effort |
|---|---|---|---|
| 1 | _[e.g., Add BM25 hybrid search]_ | _+5% recall_ | _2 hours_ |
| 2 | | | |
| 3 | | | |

### Near-Term Improvements (Next 2-4 Weeks)

| # | Action | Expected Impact | Effort |
|---|---|---|---|
| 1 | _[e.g., Fine-tune embedding model on domain data]_ | _+8% precision_ | _1 week_ |
| 2 | | | |
| 3 | | | |

### Long-Term Considerations

_Strategic improvements that require significant investment._

1.
2.

---

## 9. Raw Data and Artifacts

| Artifact | Location |
|---|---|
| Full evaluation results (JSON/CSV) | _[file path or URL]_ |
| Evaluation dataset | _[file path or URL]_ |
| Pipeline configuration | _[file path or commit hash]_ |
| Evaluation script | _[file path]_ |
| Trace logs | _[Langfuse/LangSmith URL]_ |
