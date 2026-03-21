---
name: evaluate
description: "Evaluate your RAG pipeline with metrics"
---

# Evaluate: Measure Your RAG Pipeline's Quality

> **Scope:** This skill focuses on **answer quality metrics** (faithfulness, relevancy, correctness) against a labeled test set. For operational performance metrics (latency, throughput, cost), use `/benchmark`.

Run a structured evaluation of the learner's RAG pipeline using established metrics. This skill teaches evaluation methodology while generating actionable results.

## Step 1: Identify the Pipeline

Welcome! Let's see how your RAG pipeline is performing.

First, check whether the learner has existing work to evaluate:
- Look for a learner profile at `progress/learner-profile.md` and for code in `src/` and `projects/`.
- If pipeline code exists in `projects/`, great — proceed. If multiple pipelines exist, ask which one to evaluate.
- If **no pipeline or RAG code exists** anywhere in `projects/` or `src/`, guide them warmly:
  > "It looks like you haven't built a pipeline yet — that's totally fine! Let's get you set up first. Run `/build` to create your first RAG pipeline, and then come back here to see how it scores. It only takes a few minutes to get something running!"

  Stop here — do not continue to Step 2.
- If a pipeline is found, verify it has the minimum components: a retriever and a generator.

## Step 2: Explain the Evaluation Framework

Before running metrics, teach the learner what they are measuring and why:

### Core RAG Metrics
- **Faithfulness**: Does the generated answer stick to the retrieved context? (measures hallucination)
- **Answer Relevancy**: Is the answer actually relevant to the question asked?
- **Context Precision**: Are the retrieved documents relevant to the question?
- **Context Recall**: Did the retriever find all the relevant information?

### Additional Metrics (if applicable)
- **Answer Correctness**: How close is the answer to a ground truth answer?
- **Latency**: How long does each pipeline stage take?
- **Token Usage**: How many tokens are consumed per query?

Explain each metric with a simple analogy so the learner builds intuition.

## Step 3: Prepare Test Data

Help the learner create or use evaluation data:

1. **Generate test queries**: Create 10-20 representative questions for their corpus.
2. **Create ground truth** (if needed): For each question, write the ideal answer and list the relevant source documents.
3. **Save the test set** to `projects/[pipeline-name]/eval/test-set.json`.

If they already have a test set, load and validate it.

## Step 4: Run the Evaluation

Walk through running the evaluation step by step:

1. Set up the evaluation framework (RAGAS, custom, or both).
2. Run each test query through the pipeline, capturing: the query, retrieved contexts, generated answer, and latency.
3. Compute metrics for each query.
4. Aggregate results.

Provide code snippets the learner can run. Explain what each part does.

## Step 5: Present Results

Display results in a clear, readable format:

```
RAG Pipeline Evaluation Report
==============================
Pipeline: [name]
Test queries: [N]
Date: [today]

Overall Scores:
  Faithfulness:      [score] / 1.0
  Answer Relevancy:  [score] / 1.0
  Context Precision:  [score] / 1.0
  Context Recall:     [score] / 1.0

Avg Latency: [X]ms (retrieval: [Y]ms, generation: [Z]ms)
```

Highlight the weakest metric and explain what it means practically.

## Step 6: Improvement Recommendations

Based on the results, provide specific, actionable suggestions:

- Low faithfulness -> check prompt template, add grounding instructions, consider smaller chunks
- Low context precision -> revisit chunking strategy, try re-ranking, tune embedding model
- Low context recall -> check chunk coverage, try hybrid search, increase top-k
- High latency -> profile each stage, consider caching, batch embeddings

Prioritize the top 2-3 improvements that would have the biggest impact.

## Step 7: Save and Track

Save the evaluation report to `projects/[pipeline-name]/eval/reports/report-[date].md`. Update `progress/module-tracker.md` to note the evaluation was completed. Encourage the learner to re-evaluate after making improvements to see their progress.

Suggest 2-3 relevant next steps using slash commands:

- `/benchmark` — measure operational performance (latency, throughput, cost) alongside quality
- `/debug-rag` — diagnose and fix the weakest areas identified in your evaluation
- `/build` — implement the improvements suggested above and re-evaluate
