---
name: benchmark
description: "Benchmark your RAG pipeline's performance"
---

# Benchmark: Measure Your RAG Pipeline's Performance

> **Scope:** This skill focuses on **operational performance** (latency, throughput, token costs, memory). For answer quality metrics (faithfulness, relevancy, correctness), use `/evaluate`.

Set up and run comprehensive benchmarks on the learner's RAG pipeline to identify bottlenecks and establish performance baselines.

## Step 1: Identify the Pipeline

- Locate the learner's RAG pipeline in `projects/`. If multiple exist, ask which to benchmark.
- If no pipeline exists, explain the requirement and suggest `/build` first.
- Catalog the pipeline components: loader, chunker, embedder, vector store, retriever, generator.

## Step 2: Define Benchmark Scope

Ask the learner what they want to measure, or suggest a comprehensive benchmark covering:

### Latency Metrics
- **End-to-end latency**: Total time from query to answer
- **Retrieval latency**: Time to embed the query and fetch results from the vector store
- **Generation latency**: Time for the LLM to produce the answer
- **Embedding latency**: Time to embed a single query or a batch of documents

### Throughput Metrics
- **Queries per second**: How many queries can the pipeline handle?
- **Indexing throughput**: How fast can documents be chunked, embedded, and stored?

### Quality Metrics
- **Retrieval accuracy**: Precision@k, Recall@k, MRR (Mean Reciprocal Rank)
- **Answer quality**: Faithfulness, relevancy (via RAGAS or custom evaluators)

### Resource Metrics
- **Token usage**: Tokens consumed per query (embedding + generation)
- **Memory footprint**: RAM usage of the vector store and pipeline components
- **Cost estimate**: Approximate cost per query for paid APIs

## Step 3: Prepare the Benchmark Suite

Help the learner set up the benchmarking infrastructure:

1. **Create a test query set**: 20-50 queries of varying complexity, representative of real usage.
2. **Establish ground truth** (for quality metrics): Expected answers and relevant source documents.
3. **Set up timing instrumentation**: Wrap each pipeline stage with timing code.
4. **Configure warm-up runs**: Run 5-10 queries before measuring to avoid cold-start effects.

Provide reusable benchmark code that the learner can save and run again later.

## Step 4: Run the Benchmarks

Execute the benchmarks and collect data:

1. Run the full query set through the pipeline
2. Record all metrics for each query
3. Compute statistics: mean, median, p95, p99 for latency; averages for quality

Display a progress indicator as benchmarks run.

## Step 5: Present Results

Display results in clear tables:

```
Performance Benchmark Report
============================
Pipeline: [name]
Queries: [N]
Date: [today]

Latency (ms):
  Stage            Mean    Median    P95     P99
  Retrieval        [...]   [...]     [...]   [...]
  Generation       [...]   [...]     [...]   [...]
  End-to-end       [...]   [...]     [...]   [...]

Quality:
  Precision@5:     [score]
  Recall@5:        [score]
  MRR:             [score]
  Faithfulness:    [score]

Resources:
  Avg tokens/query: [N]
  Est. cost/query:  $[X]
```

## Step 6: Identify Bottlenecks

Analyze the results and highlight:
- Which stage is the biggest latency contributor?
- Are there any outlier queries that are much slower?
- Where is quality weakest?
- Is cost per query sustainable at target scale?

## Step 7: Optimization Suggestions

Provide prioritized recommendations:
1. **Quick wins**: Changes that take < 30 minutes and yield measurable improvement
2. **Medium effort**: Changes that require refactoring but have significant impact
3. **Architectural changes**: Bigger changes for when the pipeline needs to scale

Examples: add caching, batch embeddings, switch to a faster embedding model, add a re-ranker, optimize chunk size.

## Step 8: Save the Report

Save the benchmark report to `projects/[pipeline-name]/eval/benchmarks/report-[date].md`. Encourage the learner to re-run after optimizations to measure improvement.
