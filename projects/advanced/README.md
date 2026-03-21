# Advanced Project: Agentic RAG with Self-Correction

Build an agentic RAG system that routes queries, uses tools, and self-corrects its retrieval.

## Goal
Create a production-grade RAG system that can:
1. Classify and route queries to specialized retrievers
2. Decompose complex queries into sub-queries
3. Self-evaluate retrieval quality and retry if insufficient
4. Use tool calls for structured data (SQL, API lookups)
5. Implement CRAG (Corrective RAG) patterns
6. Monitor and log all pipeline stages

## Prerequisites
- Modules 1-8 completed
- Intermediate project completed
- Familiarity with Claude tool use / function calling

## Structure
```
advanced/
├── README.md              # This file
├── router/                # Query routing
│   ├── classifier.py      # Intent classification
│   └── router.py          # Route to appropriate retriever
├── query/                 # Query processing
│   ├── decomposer.py      # Multi-hop query decomposition
│   └── expander.py        # Query expansion (HyDE)
├── retrieval/             # Multi-strategy retrieval
│   ├── retriever_pool.py  # Manages multiple retrievers
│   ├── self_evaluator.py  # Grades retrieval quality
│   └── corrective.py      # CRAG — retry/web fallback
├── tools/                 # Tool integrations
│   ├── sql_tool.py        # Structured data queries
│   └── api_tool.py        # External API lookups
├── generation/            # Agentic generation
│   ├── agent.py           # Main agent loop
│   └── grader.py          # Answer quality grading
├── monitoring/            # Observability
│   ├── logger.py          # Structured logging
│   └── metrics.py         # Pipeline metrics
├── pipeline.py            # Orchestrator
├── evaluate.py            # End-to-end evaluation
└── config.yaml            # Configuration
```

## Steps
1. Build the query router and classifier
2. Implement query decomposition for multi-hop questions
3. Create a retriever pool with self-evaluation
4. Add CRAG pattern (evaluate → correct → retry)
5. Integrate tool calling for structured data
6. Build the agent loop with grading
7. Add monitoring and logging
8. Evaluate end-to-end with complex queries

## Success Criteria
- [ ] Routes queries to correct retriever >90% of the time
- [ ] Decomposes multi-hop queries into valid sub-queries
- [ ] Self-correction improves answer quality on 30%+ of queries
- [ ] Tool calls return accurate structured data
- [ ] Full observability — can trace any query through the pipeline
- [ ] RAGAS scores: faithfulness >0.85, relevancy >0.80

## Hints
Use `/architecture` to design your system before coding. Use `/challenge advanced` for additional scenarios to test against.
