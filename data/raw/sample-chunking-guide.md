---
last_reviewed: 2026-03-21
review_cycle: semi-annually
staleness_risk: low
---

# Chunking Strategies for RAG

## Why Chunking Matters

Chunking is one of the most impactful decisions in a RAG pipeline. The way you split documents directly affects:
- **Retrieval precision**: Can the system find the right information?
- **Context quality**: Does the retrieved chunk contain enough context?
- **Token efficiency**: Are you using your LLM's context window wisely?

## Strategy 1: Fixed-Size Chunking

The simplest approach — split text into chunks of a fixed number of characters or tokens.

**Parameters:**
- `chunk_size`: Number of characters/tokens per chunk (typical: 500-1000 tokens)
- `chunk_overlap`: Number of overlapping characters/tokens (typical: 50-200 tokens)

**Pros:** Simple, predictable, fast
**Cons:** May split mid-sentence or mid-thought, ignores document structure

**Best for:** Uniform text documents, quick prototypes

## Strategy 2: Recursive Character Splitting

Splits text using a hierarchy of separators, trying the largest separator first and falling back to smaller ones.

**Separator hierarchy:** `\n\n` → `\n` → `. ` → ` ` → ``

**Pros:** Respects paragraph and sentence boundaries
**Cons:** Chunk sizes vary, may still miss semantic boundaries

**Best for:** Articles, documentation, general-purpose text

## Strategy 3: Semantic Chunking

Uses embeddings to detect topic boundaries. Computes embedding similarity between consecutive sentences/paragraphs and splits where similarity drops below a threshold.

**Pros:** Chunks are semantically coherent
**Cons:** Slower (requires embedding computation), harder to tune

**Best for:** Documents with varying topics, research papers, long-form content

## Strategy 4: Document-Aware Chunking

Leverages document structure — headers, sections, lists, code blocks — to create natural chunk boundaries.

**Pros:** Preserves document hierarchy, natural boundaries
**Cons:** Requires structured input (markdown, HTML with headers)

**Best for:** Technical documentation, wikis, structured reports

## Strategy 5: Agentic Chunking

Uses an LLM to determine optimal chunk boundaries based on content understanding.

**Pros:** Highest quality boundaries
**Cons:** Expensive, slow, not scalable for large corpora

**Best for:** High-value documents where quality matters most

## Choosing a Chunk Size

| Chunk Size | Pros | Cons |
|-----------|------|------|
| Small (100-300 tokens) | Precise retrieval | May lack context |
| Medium (300-800 tokens) | Good balance | General purpose |
| Large (800-1500 tokens) | Rich context | May include noise |

## Overlap Strategy

Overlap helps preserve context that spans chunk boundaries:
- **No overlap**: Fastest, but risks losing boundary context
- **10-20% overlap**: Good default for most use cases
- **Sliding window**: Maximum continuity, but increases storage

## Metadata Preservation

Always attach metadata to chunks:
- Source document name/path
- Chunk index within document
- Section header (if available)
- Page number (for PDFs)
- Creation/modification date

This enables filtered retrieval and source attribution in generated answers.
