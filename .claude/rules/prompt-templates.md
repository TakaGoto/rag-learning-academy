---
path: src/generation/**
last_reviewed: 2026-03-21
review_cycle: monthly
staleness_risk: high
---

# Prompt Template Rules

## 1. Use template variables, never string concatenation for prompts

Templates are readable, auditable, and less error-prone.

```python
# Correct
from string import Template

RAG_PROMPT = Template("""Answer the question based on the provided context.

Context:
${context}

Question: ${question}

Answer:""")

prompt = RAG_PROMPT.substitute(context=context_text, question=user_query)

# Incorrect - fragile string concatenation
prompt = "Answer this: " + question + "\n\nContext: " + context  # hard to read, easy to break
```

## 2. Include system instructions for grounding/citation

Instruct the model to stay grounded in the retrieved context.

```python
# Correct
SYSTEM_PROMPT = """You are a helpful assistant that answers questions using ONLY 
the provided context. If the context does not contain enough information to answer, 
say "I don't have enough information to answer this question."

Rules:
- Cite the source document for each claim using [Source: document_name]
- Do not use information outside the provided context
- If uncertain, state your uncertainty"""

# Incorrect - no grounding instructions
SYSTEM_PROMPT = "You are a helpful assistant."
```

## 3. Set maximum context length per model

Prevent context overflow that truncates important content.

```python
# Correct
MODEL_CONTEXT_LIMITS = {
    "gpt-4o": 128_000,
    "gpt-4o-mini": 128_000,
    "claude-sonnet-4-6-20250514": 200_000,  # Check Anthropic docs for current model IDs
}

def build_prompt(query: str, context: str, model: str) -> str:
    max_context = MODEL_CONTEXT_LIMITS.get(model, 4_000) - 1_000  # reserve for query + response
    truncated_context = tokenizer.truncate(context, max_tokens=max_context)
    return RAG_PROMPT.substitute(context=truncated_context, question=query)

# Incorrect - no limit, context can overflow
def build_prompt(query, context):
    return f"Context: {context}\n\nQuestion: {query}"  # context could be 500K tokens
```

## 4. Always include source attribution in generated responses

```python
# Correct
def format_context(results: list[RetrievalResult]) -> str:
    sections = []
    for i, r in enumerate(results, 1):
        source = r.document.metadata.get("source", "unknown")
        sections.append(f"[Source {i}: {source}]\n{r.document.text}")
    return "\n\n".join(sections)

PROMPT_SUFFIX = """
Cite sources using [Source N] notation for each claim in your answer."""

# Incorrect - context with no source info
context = "\n".join(r.document.text for r in results)  # no way to cite
```

## 5. Separate retrieval context from user query in prompt structure

Keep them in distinct, labeled sections for clarity.

```python
# Correct
RAG_PROMPT = Template("""${system_instructions}

--- Retrieved Context ---
${context}
--- End Context ---

--- User Question ---
${question}
--- End Question ---

Provide your answer below, citing sources:""")

# Incorrect - query and context mixed together
prompt = f"{question} {context} Answer:"  # model can't distinguish query from context
```
