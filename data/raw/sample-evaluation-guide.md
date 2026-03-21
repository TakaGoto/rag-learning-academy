# Evaluating RAG Systems

## Why Evaluation is Hard

RAG evaluation is uniquely challenging because you need to assess multiple components:
1. Did the retriever find the right documents? (Retrieval quality)
2. Did the generator use the retrieved context faithfully? (Faithfulness)
3. Is the final answer actually correct? (Correctness)
4. Is the answer relevant to the question? (Relevancy)

A system can retrieve perfectly but generate poorly, or generate beautifully from the wrong context.

## Retrieval Metrics

### Precision@K
Of the top K retrieved documents, how many are actually relevant?

`Precision@K = (Relevant docs in top K) / K`

### Recall@K
Of all relevant documents, how many appear in the top K results?

`Recall@K = (Relevant docs in top K) / (Total relevant docs)`

### Mean Reciprocal Rank (MRR)
How high is the first relevant result ranked?

`MRR = 1 / (rank of first relevant result)`

### Normalized Discounted Cumulative Gain (NDCG)
Measures ranking quality, giving more credit to relevant results ranked higher.

## Generation Metrics

### Faithfulness
Does the answer only contain information from the retrieved context? A faithfulness score of 1.0 means every claim in the answer is supported by the retrieved documents.

### Answer Relevancy
Is the generated answer actually addressing the user's question? Measures semantic similarity between the question and the answer.

### Answer Correctness
Is the answer factually correct? Compared against a ground truth reference answer.

## The RAGAS Framework

RAGAS (Retrieval Augmented Generation Assessment) is the standard framework for RAG evaluation. It provides:

- **Faithfulness**: Claims in answer vs. claims supported by context
- **Answer Relevancy**: Synthetic question generation from answer, compared to original
- **Context Precision**: Ranking quality of retrieved context
- **Context Recall**: Coverage of ground truth by retrieved context

### Using RAGAS

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
)
```

## Building an Evaluation Dataset

A good evaluation dataset contains:
- **Questions**: Representative queries your system should handle
- **Ground truth answers**: Correct reference answers
- **Ground truth contexts**: The actual relevant documents/passages

### Tips for Evaluation Datasets
1. Include diverse question types (factual, analytical, comparison)
2. Include edge cases (no-answer questions, ambiguous queries)
3. Aim for 50-100 question-answer pairs minimum
4. Have domain experts validate ground truth
5. Update the dataset as your knowledge base changes

## Common Failure Modes

| Symptom | Likely Cause | Metric to Check |
|---------|-------------|-----------------|
| Hallucinated facts | Poor grounding | Faithfulness |
| Off-topic answers | Bad retrieval | Context Precision |
| Missing information | Incomplete retrieval | Context Recall |
| Generic answers | Ignoring context | Answer Relevancy |
| Wrong answers | Multiple issues | Answer Correctness |

## Continuous Evaluation

In production, implement:
- **Automated regression testing**: Run evaluation suite on every pipeline change
- **User feedback loops**: Thumbs up/down on answers
- **Retrieval logging**: Track what's being retrieved for manual review
- **A/B testing**: Compare pipeline changes with controlled experiments
