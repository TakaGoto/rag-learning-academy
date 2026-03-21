---
path: src/evaluation/**
---

# Evaluation Code Rules

## 1. Every metric function must return a value between 0 and 1

Consistent scales make metrics comparable and aggregatable.

```python
# Correct
def precision_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    retrieved_k = retrieved[:k]
    hits = len(set(retrieved_k) & set(relevant))
    score = hits / k if k > 0 else 0.0
    assert 0.0 <= score <= 1.0
    return score

# Incorrect - returning unbounded or non-normalized values
def relevance_score(results):
    return sum(r.score for r in results)  # could be any magnitude
```

## 2. Include confidence intervals where applicable

Point estimates hide uncertainty. Report bounds when computing on samples.

```python
# Correct
import numpy as np

def metric_with_95ci(scores: list[float]) -> dict:
    """Returns mean with 95% confidence interval. For other levels, use scipy.stats.norm.ppf."""
    mean = np.mean(scores)
    std_err = np.std(scores, ddof=1) / np.sqrt(len(scores))
    z = 1.96  # 95% CI (fixed)
    return {
        "mean": float(mean),
        "ci_lower": float(mean - z * std_err),
        "ci_upper": float(mean + z * std_err),
        "n_samples": len(scores),
    }

# Incorrect - bare mean with no indication of variance
return np.mean(scores)
```

## 3. Log all evaluation runs with parameters for reproducibility

```python
# Correct
import json, logging
logger = logging.getLogger(__name__)

def run_evaluation(config: dict, test_set: list) -> dict:
    logger.info("eval_start config=%s test_size=%d", json.dumps(config), len(test_set))
    results = evaluate(config, test_set)
    logger.info("eval_end metrics=%s", json.dumps(results))
    return results

# Incorrect - no record of what was evaluated or how
def run_evaluation(test_set):
    return evaluate(test_set)
```

## 4. Separate retrieval metrics from generation metrics

Mixing them makes it impossible to diagnose which stage failed.

```python
# Correct
@dataclass
class EvalResults:
    retrieval: dict   # precision@k, recall@k, MRR, NDCG
    generation: dict  # faithfulness, answer relevancy, BLEU/ROUGE

def evaluate_pipeline(queries, ground_truth):
    retrieval_metrics = evaluate_retrieval(queries, ground_truth)
    generation_metrics = evaluate_generation(queries, ground_truth)
    return EvalResults(retrieval=retrieval_metrics, generation=generation_metrics)

# Incorrect - one big metric soup
def evaluate(queries):
    return {"score": compute_everything(queries)}
```

## 5. Always evaluate on a held-out test set

Never evaluate on the same data used for building the index or tuning retrieval.

```python
# Correct
def prepare_eval_data(dataset: list, test_ratio: float = 0.2) -> tuple:
    split = int(len(dataset) * (1 - test_ratio))
    train_set = dataset[:split]
    test_set = dataset[split:]  # held out, never used during indexing
    return train_set, test_set

# Incorrect - evaluating on indexed data
index.add(all_documents)
metrics = evaluate(all_documents)  # data leakage
```
