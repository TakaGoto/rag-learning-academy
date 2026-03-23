# Language Support Guide

## Reading the Learner's Language Preference

Before generating any code, read `progress/learner-profile.md` and check the **Language** field. If no language is set or no profile exists, default to Python.

## Code Generation Rules

1. **Generate all code examples, skeletons, and solutions in the learner's chosen language.** Don't show Python to a TypeScript learner unless explicitly comparing languages.

2. **Use idiomatic patterns.** Don't transliterate Python line-by-line. Use the language's native idioms, error handling, project structure, and conventions.

3. **Adapt environment setup per language:**
   - **Python:** `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
   - **TypeScript:** `npm init -y && npm install <packages>` (or `pnpm`)
   - **Go:** `go mod init rag-project && go get <packages>`
   - **Rust:** `cargo init rag-project && cargo add <crates>`

4. **Use file extensions appropriate to the language:** `.py`, `.ts`, `.go`, `.rs`

5. **When reviewing learner code,** apply the coding standards for their language, not Python standards.

## Library Mapping

| Concept | Python | TypeScript | Go | Rust |
|---------|--------|------------|-----|------|
| RAG framework | LangChain, LlamaIndex | LangChain.js | (manual — build from API calls) | (manual — build from API calls) |
| Vector DB (local) | chromadb | chromadb | chromem-go, qdrant-client | qdrant-client |
| Vector DB (hosted) | pinecone-client, qdrant-client | @pinecone-database/pinecone, @qdrant/js-client-rest | qdrant-client | qdrant-client |
| Embeddings (local) | sentence-transformers | @xenova/transformers | (API only) | (API only) |
| Embeddings (API) | openai | openai | sashabaranov/go-openai | async-openai |
| LLM client | anthropic, openai | @anthropic-ai/sdk, openai | anthropic SDK, go-openai | anthropic / async-openai |
| HTTP client | requests, httpx | fetch (built-in), axios | net/http | reqwest |
| Testing | pytest | vitest, jest | testing (stdlib) | cargo test |
| Async | asyncio | native async/await | goroutines + channels | tokio |
| Config from env | pydantic-settings, python-dotenv | dotenv, zod | os.Getenv, envconfig | dotenvy, config |
| Document parsing | unstructured, pypdf, pdfplumber | pdf-parse, mammoth | (limited — call APIs) | (limited — call APIs) |
| BM25 / sparse | rank-bm25 | (manual implementation) | (manual implementation) | (manual implementation) |
| Evaluation | ragas | (manual — see ecosystem gaps) | (manual) | (manual) |

## Ecosystem Gap Handling

When an exercise requires a library that doesn't exist in the learner's language, use one of these strategies:

### Tier A — Use Python as a tool alongside your pipeline
For evaluation (RAGAS) and document parsing, it's common in production to have polyglot toolchains. The learner's pipeline can be in TypeScript, but they run `python eval.py` to score it. Frame this as a real-world pattern:

> "Most production RAG systems are polyglot. Your pipeline is in [language], but your evaluation harness can be Python — that's normal. RAGAS takes your pipeline's outputs (queries, contexts, answers) as JSON, so the languages don't need to match."

### Tier B — Implement the core algorithm manually
For metrics like faithfulness, MRR, or precision@k, have the learner implement it themselves. This is often *better* pedagogy than calling a library:

> "Instead of using [library] (Python-only), you'll implement [metric] yourself. Here's the algorithm: ..."

### Tier C — Mark as Python-only, offer alternatives
For exercises deeply tied to a Python library with no workaround (e.g., sentence-transformers fine-tuning):

> "**Python-only exercise.** [Library] requires Python. You can: (a) switch to Python for this exercise only, (b) skip it and move on, or (c) use the API-based alternative if available."

## Ecosystem Gaps by Language

### TypeScript
- **RAGAS:** Use Tier A (Python RAGAS on pipeline JSON output) or Tier B (implement metrics manually)
- **sentence-transformers fine-tuning:** Python-only (Tier C)
- **LlamaIndex:** No TS version — use LangChain.js instead
- **Document parsing:** pdf-parse and mammoth cover basics; Unstructured has no TS equivalent
- **BM25:** No mature library — implement from scratch (good learning exercise)

### Go
- **LangChain/LlamaIndex:** No equivalent. Build from raw API calls (teaches internals deeply)
- **RAGAS:** Tier A or Tier B
- **Local embeddings:** API-only (no sentence-transformers equivalent)
- **ChromaDB:** Use chromem-go or call the Chroma HTTP API
- **Document parsing:** Very limited — use API-based parsing or call Python

### Rust
- **LangChain/LlamaIndex:** No equivalent. Build from raw API calls
- **RAGAS:** Tier A or Tier B
- **Local embeddings:** API-only
- **Vector DB:** qdrant-client is well-supported; Chroma requires HTTP API
- **Document parsing:** Very limited — use API-based parsing or call Python
