---
name: code-review
description: "Get expert feedback on your RAG code"
---

# Code Review: Expert Feedback on Your RAG Implementation

Review the learner's RAG code with the eye of an experienced RAG engineer, providing actionable feedback that improves correctness, performance, and robustness.

## Step 1: Identify the Code to Review

- If the user specifies a file or directory (e.g., `/code-review projects/my-rag/retriever.py`), review that.
- If no argument is given, look in `projects/` for the learner's most recent work.
- If multiple files exist, ask which component they want reviewed, or offer to review the full pipeline.

## Step 2: Read and Understand the Code

Before giving feedback, thoroughly understand what the code does:
- Read all relevant files
- Trace the data flow from input to output
- Identify the overall architecture and design pattern
- Note which libraries and models are being used

## Step 3: Review Dimensions

Evaluate the code across these dimensions, providing specific feedback for each:

### Correctness
- Does the code produce correct results?
- Are there logic errors, off-by-one errors, or incorrect API usage?
- Are edge cases handled (empty input, very large documents, special characters)?
- Are embeddings and vector operations mathematically correct?

### RAG-Specific Best Practices
- **Chunk size and overlap**: Are they appropriate for the document type and use case?
- **Embedding dimensions**: Do all components agree on the embedding dimension?
- **Prompt engineering**: Is the RAG prompt well-structured? Does it instruct the model to use only the provided context?
- **Context window management**: Could the context exceed the model's token limit?
- **Metadata handling**: Is useful metadata preserved through the pipeline?
- **Error handling**: What happens when the retriever returns no results? When the API is down?

### Security and Safety
- **Prompt injection**: Can user queries manipulate the system prompt?
- **Data leakage**: Could sensitive information from one user leak to another?
- **API key handling**: Are keys hardcoded or properly managed via environment variables?
- **Input validation**: Is user input sanitized before processing?

### Performance
- **Batching**: Are embeddings computed in batches or one at a time?
- **Caching**: Are repeated queries or embeddings cached?
- **Unnecessary computation**: Is any work being done that could be avoided?
- **Memory usage**: Are large documents loaded entirely into memory unnecessarily?

### Code Quality
- **Readability**: Is the code clear and well-organized?
- **Documentation**: Are functions documented with docstrings?
- **Type hints**: Are type annotations used consistently?
- **Configuration**: Are magic numbers extracted into configuration?
- **Testing**: Are there tests? What is the coverage?

## Step 4: Deliver Feedback

Structure the feedback clearly with priority levels:

### Critical Issues (fix these first)
Items that cause incorrect results, security vulnerabilities, or data loss.

### Important Improvements (fix these soon)
Items that significantly affect quality, performance, or maintainability.

### Suggestions (nice to have)
Minor improvements, style tweaks, and optimizations.

For each item:
1. **What**: Describe the issue clearly
2. **Where**: Point to the specific line or section
3. **Why**: Explain why this matters
4. **How**: Suggest a concrete fix with a code snippet

## Step 5: Highlight Strengths

Always note what the learner did well. Positive reinforcement is important:
- Good design decisions
- Clean code patterns
- Thoughtful error handling
- Well-chosen libraries or approaches

## Step 6: Summary and Next Steps

Provide a brief overall assessment:
- Overall quality rating: Needs Work / Solid Foundation / Production-Ready
- Top 3 priorities for improvement
- Suggested next steps (e.g., "Add error handling, then run `/evaluate` to measure quality")

## Guidelines

- Be constructive, not critical — the goal is to help the learner improve
- Explain the "why" behind every suggestion so the learner learns the principle
- Prioritize feedback that has the most impact on the RAG pipeline's quality
- Recognize that learner code will not be perfect — meet them where they are
- If the code is good, say so — do not manufacture issues
