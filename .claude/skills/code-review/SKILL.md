---
name: code-review
description: "Get expert feedback on your RAG code"
---

# Code Review: Expert Feedback on Your RAG Implementation

Review the learner's RAG code with the eye of an experienced RAG engineer, providing actionable feedback that improves correctness, performance, and robustness.

> **Language awareness:** Before generating code, read the learner's language from `progress/learner-profile.md`. Generate all code examples, skeletons, and setup instructions in that language. See `.claude/docs/reference/language-support.md` for library mappings and ecosystem gap handling. Default to Python if no language is set.

## Step 1: Identify the Code to Review

Welcome! Let's take a close look at your RAG code together.

First, determine what code is available for review:
- If the user specifies a file or directory (e.g., `/code-review projects/my-rag/retriever`), review that.
- If no argument is given, check for a learner profile at `progress/learner-profile.md` and look for code in `src/` and `projects/`.
- If **no RAG code exists** anywhere in `projects/` or `src/` (and no file was specified), guide them warmly:
  > "It looks like you haven't written any RAG code yet — that's the perfect place to start! Run `/build` to create your first RAG component, and then come back here for expert feedback on what you've built. I'll be ready to help you level it up!"

  Stop here — do not continue to Step 2.
- If code is found and multiple files exist, ask which component they want reviewed, or offer to review the full pipeline.

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

Generate review annotations with code examples in the learner's chosen language. For example, flag issues like missing error handling for API failures and show the suggested fix using idiomatic patterns for their language.

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

Suggest 2-3 relevant next steps using slash commands:

- `/build` — implement the improvements identified in this review
- `/evaluate` — measure your pipeline's quality with RAG metrics after making fixes
- `/debug-rag` — diagnose any specific failure modes flagged during the review

## Guidelines

- Be constructive, not critical — the goal is to help the learner improve
- Explain the "why" behind every suggestion so the learner learns the principle
- Prioritize feedback that has the most impact on the RAG pipeline's quality
- Recognize that learner code will not be perfect — meet them where they are
- If the code is good, say so — do not manufacture issues
