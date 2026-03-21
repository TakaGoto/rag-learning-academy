---
last_reviewed: 2026-03-21
review_cycle: quarterly
staleness_risk: medium
---

# Module 07: Evaluation

## Module Objectives

By the end of this module, learners will be able to:

- Explain why RAG evaluation requires specialized approaches beyond standard NLP metrics
- Compute retrieval metrics from scratch: precision@k, recall@k, MRR, NDCG
- Compute generation metrics: faithfulness, answer relevancy, answer correctness
- Use the RAGAS framework for automated, reproducible RAG evaluation
- Build and maintain gold-standard evaluation datasets for continuous quality monitoring

## Prerequisites

- Module 05: Retrieval Strategies (completed)
- Module 06: Generation (completed)
- Basic statistics (mean, median, standard deviation, distributions)

### Before You Begin

Verify you're comfortable with these concepts from prior modules:

- [ ] Dense, sparse, and hybrid retrieval strategies and when each excels (Module 05)
- [ ] Prompt design for grounding LLM responses in retrieved context (Module 06)
- [ ] Citation and source attribution in generated answers (Module 06)
- [ ] The difference between retrieval quality and generation quality (Module 05, Module 06)

## Lessons

### 7.1 Evaluation Fundamentals — `core`

**Description:** Why RAG evaluation is uniquely challenging. Two independent stages (retrieval and generation) can each fail in different ways, and failures compound. A correct answer derived from wrong sources is still a reliability problem. Covers the evaluation taxonomy: component-level vs end-to-end, automatic vs human, reference-based vs reference-free. Introduces the concept of evaluation-driven development: measure first, improve second.

**Key concepts:** Component vs end-to-end evaluation, automatic vs human evaluation, reference-based vs reference-free metrics, evaluation taxonomy, compounding error, evaluation-driven development.

**Duration:** 30 minutes

### 7.2 Retrieval Metrics — `core`

**Description:** Measuring how well the retriever finds relevant documents. Precision@k: fraction of top-k results that are relevant. Recall@k: fraction of all relevant documents appearing in top-k. Mean Reciprocal Rank (MRR): average of 1/rank for the first relevant result across queries. NDCG: ranking quality metric that accounts for graded relevance (not just binary). Covers practical computation, interpretation of scores, and setting meaningful thresholds.

**Key concepts:** Precision@k, Recall@k, MRR, NDCG, hit rate, context precision (RAGAS), context recall (RAGAS), binary vs graded relevance, relevance judgment creation.

**Duration:** 45 minutes

### 7.3 Generation Metrics — `optional`

**Description:** Measuring the quality of LLM-generated answers in the RAG context. Faithfulness: is every claim in the answer supported by the retrieved context (detecting hallucination)? Answer Relevancy: does the answer address the user's question directly? Answer Correctness: is the answer factually right when compared to a reference? Covers both LLM-as-judge approaches (GPT-4/Claude evaluating answers) and traditional NLP metrics (BLEU, ROUGE, BERTScore) and why traditional metrics are insufficient for RAG.

**Key concepts:** Faithfulness scoring, relevancy scoring, correctness scoring, LLM-as-judge methodology, BLEU, ROUGE, BERTScore, semantic similarity scoring, limitations of n-gram metrics.

**Duration:** 45 minutes

### 7.4 RAGAS Deep Dive — `optional`

**Description:** Comprehensive coverage of the RAGAS evaluation framework. The four core metrics: faithfulness (claim decomposition + NLI verification), answer relevancy (question generation from answer + similarity), context precision (relevant chunks ranked higher), context recall (ground truth coverage in context). How to install and run RAGAS, interpret score distributions, set alert thresholds, and integrate into CI/CD pipelines for regression detection.

**Key concepts:** RAGAS library installation and usage, metric computation internals, test set generation with ragas.testset, score interpretation guidelines, threshold setting, regression detection, CI/CD integration.

**Duration:** 60 minutes

### 7.5 Building Evaluation Datasets — `optional`

**Description:** Creating and maintaining gold-standard evaluation sets — the foundation of all RAG evaluation. Covers synthetic test generation (using LLMs to generate question-answer pairs from your documents), human annotation workflows (guidelines, inter-annotator agreement), question type taxonomy (factoid, multi-hop, comparison, aggregation, yes/no, unanswerable), and dataset maintenance as source documents evolve over time.

**Key concepts:** Gold standard dataset creation, synthetic Q&A generation, question type taxonomy, annotation guidelines, inter-annotator agreement (Cohen's kappa), dataset versioning, test set contamination risks, living evaluation sets.

**Duration:** 45 minutes

## Hands-On Exercises

1. **Retrieval Metrics Calculator:** Implement precision@k, recall@k, MRR, and NDCG from scratch (no evaluation libraries). Write unit tests that validate your implementations against hand-computed expected values on a small dataset with 5 queries and known relevant documents.

2. **RAGAS Evaluation Run:** Run a full RAGAS evaluation on the RAG pipeline you built in previous modules. Use at least 30 test questions. Generate a structured report with all four core metrics (faithfulness, answer relevancy, context precision, context recall). Identify the weakest component and propose a specific fix.

3. **Evaluation Dataset Builder:** Use Claude or GPT-4 to generate 50 question-answer pairs from your document corpus, stratified by question type (10 factoid, 10 multi-hop, 10 comparison, 10 aggregation, 10 yes/no). Manually review and correct at least 20 of them. Compute an LLM quality score by checking what percentage of auto-generated Q&A pairs are correct.

4. **Regression Test Suite:** Set up an automated evaluation script that: (1) loads a fixed evaluation dataset, (2) runs all four RAGAS metrics, (3) compares against stored baseline scores, (4) prints a PASS/FAIL summary with delta for each metric, (5) saves results to a JSON file with timestamps. Run it after making a pipeline change to detect regressions.

## Key Takeaways

- You cannot improve what you cannot measure — evaluation is not optional, it is the foundation of iterative RAG improvement.
- Always evaluate retrieval and generation separately; end-to-end metrics alone hide the root cause of failures. A bad answer might be a retrieval problem, a generation problem, or both.
- RAGAS provides a practical, automated evaluation framework that can run in CI/CD without human annotation for every test. It is the current community standard.
- Evaluation datasets are living artifacts that must evolve with your document corpus and query patterns. Budget time for ongoing dataset maintenance.
- LLM-as-judge metrics are imperfect but practical; calibrate them against human judgments periodically to ensure they correlate with actual quality.

## Suggested Reading

- Es et al., "RAGAS: Automated Evaluation of Retrieval Augmented Generation" (2023)
- RAGAS documentation and quickstart guide
- Zheng et al., "Judging LLM-as-a-Judge" (2023)

---

← **Previous:** [Module 06 — Generation](module-06-generation.md) | **Next:** [Module 08 — Advanced Patterns](module-08-advanced-patterns.md) →
