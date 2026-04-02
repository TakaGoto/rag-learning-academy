# Token Usage Estimates

Estimated token counts for each component, useful for context window planning. Total project content: **~98k tokens**.

### Curriculum Modules (~15k tokens total)

| Module | Topic | Est. Tokens |
|--------|-------|-------------|
| Module 01 | Foundations | ~1,200 |
| Module 02 | Document Processing | ~1,500 |
| Module 03 | Embeddings | ~1,550 |
| Module 04 | Vector Databases | ~1,650 |
| Module 05 | Retrieval Strategies | ~1,700 |
| Module 06 | Generation | ~1,700 |
| Module 07 | Evaluation | ~1,670 |
| Module 08 | Advanced Patterns | ~1,950 |
| Module 09 | Production | ~2,040 |

### Agents (~35k tokens total)

| Tier | Agents | Avg. Tokens | Total |
|------|--------|-------------|-------|
| Directors (3) | curriculum, architecture, research | ~1,570 | ~4,720 |
| Leads (5) | embedding, retrieval, indexing, evaluation, integration | ~1,630 | ~8,150 |
| Specialists (12) | chunking, vector-db, reranking, prompt, hybrid-search, document-parser, metadata, query, deployment, evaluation, graph-rag, multimodal | ~1,820 | ~21,860 |

### Skills / Slash Commands (~17k tokens total)

| Skill | Est. Tokens | | Skill | Est. Tokens |
|-------|-------------|---|-------|-------------|
| `/start` | ~720 | | `/architecture` | ~1,190 |
| `/lesson` | ~760 | | `/paper-review` | ~1,050 |
| `/quiz` | ~770 | | `/code-review` | ~1,080 |
| `/build` | ~860 | | `/glossary` | ~950 |
| `/evaluate` | ~870 | | `/challenge` | ~1,210 |
| `/debug-rag` | ~1,090 | | `/explain` | ~1,120 |
| `/compare` | ~900 | | `/roadmap` | ~1,200 |
| `/benchmark` | ~970 | | `/triage` | ~850 |
| `/audit-content` | ~1,100 | | | |

### Reference Docs (~13k tokens total)

| Document | Est. Tokens |
|----------|-------------|
| Agent Roster | ~3,050 |
| Coordination Rules | ~3,490 |
| Glossary (60+ terms) | ~3,170 |
| Coding Standards | ~2,070 |
| Quick Start | ~1,160 |

### Rules (~5k tokens total)

| Rule File | Scope | Est. Tokens |
|-----------|-------|-------------|
| pipeline-code | `src/pipelines/**` | ~910 |
| vector-db-code | `src/vector_db/**` | ~860 |
| evaluation-code | `src/evaluation/**` | ~740 |
| prompt-templates | `src/generation/**` | ~770 |
| chunking-code | `src/chunking/**` | ~710 |
| retrieval-code | `src/retrieval/**` | ~600 |
| embedding-code | `src/embeddings/**` | ~530 |

### Templates (~4.5k tokens total)

| Template | Est. Tokens |
|----------|-------------|
| Project Brief | ~1,600 |
| Evaluation Report | ~1,530 |
| RAG Architecture | ~1,350 |

### Sample Data (~2.6k tokens total)

| File | Est. Tokens |
|------|-------------|
| RAG Overview | ~930 |
| Evaluation Guide | ~880 |
| Chunking Guide | ~770 |

### Context Window Usage Per Session

A typical learning session loads:

| What's Loaded | Est. Tokens | Notes |
|---------------|-------------|-------|
| CLAUDE.md | ~1,800 | Always loaded |
| settings.json | ~270 | Always loaded |
| 1 agent definition | ~1,500-2,100 | Per active agent |
| 1 skill prompt | ~700-1,200 | Per slash command |
| 1 curriculum module | ~1,200-2,000 | Per lesson |
| 1-2 rule files | ~500-900 | Path-scoped, auto-loaded |
| **Typical session total** | **~6,000-8,300** | Fits easily in any model's context |

> **Note:** Token estimates use the ~4 chars/token approximation. Actual counts vary by tokenizer. The full project (~98k tokens) fits within Claude's 200k context window, but in practice only relevant files are loaded per session.
