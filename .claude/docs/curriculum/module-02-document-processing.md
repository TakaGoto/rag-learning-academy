# Module 02: Document Processing

## Module Objectives

By the end of this module, learners will be able to:

- Parse documents from PDF, HTML, Markdown, DOCX, and plain text formats
- Apply text cleaning and normalization pipelines appropriate for RAG
- Implement and compare multiple chunking strategies (fixed, recursive, semantic)
- Extract and attach metadata to chunks for downstream filtering
- Evaluate chunking quality and its downstream impact on retrieval

## Prerequisites

- Module 01: RAG Foundations (completed)
- Module 03: Embeddings (required for Lesson 2.5 — semantic chunking needs embeddings)
- Familiarity with regular expressions
- Understanding of basic NLP concepts (tokens, sentences, paragraphs)

## Lessons

### 2.1 Document Parsing

**Description:** Covers extraction of raw text from multiple file formats. Introduces libraries like PyMuPDF, pdfplumber, python-docx, BeautifulSoup, and Unstructured. Discusses real-world challenges: OCR for scanned PDFs, table extraction, handling images and figures, multi-column layouts, and encoding issues. Emphasizes building a unified parser interface.

**Key concepts:** Format-specific parsers, layout detection, OCR pipelines (Tesseract), the Unstructured library, document loaders, unified parsing interfaces.

**Duration:** 45 minutes

### 2.2 Text Preprocessing

**Description:** Cleaning raw extracted text for embedding quality. Covers whitespace normalization, Unicode handling, removing headers/footers/boilerplate, deduplication, language detection, and encoding issues. Emphasizes that garbage-in-garbage-out applies strongly to RAG — embedding quality depends directly on text quality.

**Key concepts:** Text normalization, stopword handling, tokenization awareness, cleaning pipelines, boilerplate detection, deduplication strategies.

**Duration:** 30 minutes

### 2.3 Fixed-Size Chunking

**Description:** The simplest chunking approach: split text into fixed-length segments by character count or token count with configurable overlap. Covers choosing chunk size (256-1024 tokens, or equivalently 200-800 words), overlap ratios (10-20%), and the impact of these parameters on retrieval quality. Demonstrates using tiktoken for accurate token counting. Note: chunk sizes are commonly expressed in either words or tokens (~1 word ≈ 1.3 tokens). This curriculum uses token counts for precision with LLM context budgets.

**Key concepts:** Chunk size, overlap, token counting (tiktoken), boundary alignment, the chunk size vs retrieval quality curve.

**Duration:** 30 minutes

### 2.4 Recursive Chunking

**Description:** LangChain-style recursive splitting that respects document structure. Splits on paragraph boundaries first, then sentences, then words, then characters. Produces more semantically coherent chunks than fixed-size. Covers custom separator hierarchies for different document types (Markdown headers, HTML tags, code blocks).

**Key concepts:** Separator hierarchy, recursive text splitter, structure-aware splitting, markdown-aware chunking, HTML-aware chunking, code-aware chunking.

**Duration:** 45 minutes

### 2.5 Semantic Chunking

**Description:** Advanced chunking using embedding similarity to determine split points. Compute embeddings for individual sentences, measure similarity between adjacent sentences, and split where similarity drops below a threshold. Produces chunks that align with topic boundaries rather than arbitrary positions.

**Key concepts:** Embedding-based segmentation, similarity thresholds, breakpoint detection, topic coherence, percentile-based thresholds, gradient-based splitting.

**Duration:** 45 minutes

## Hands-On Exercises

1. **Multi-Format Parser:** Write a unified `parse_document(path: str) -> ParsedDocument` function that accepts PDF, Markdown, HTML, and plain text files and returns clean text with metadata (source filename, page number, format, character count). Handle at least one edge case per format.

2. **Chunking Comparison:** Take a 10-page technical document and chunk it using all three strategies (fixed at 512 tokens, recursive with markdown separators, semantic with cosine threshold). Compare: chunk count, average chunk size, size variance, and qualitative coherence (read 5 random chunks from each).

3. **Metadata Enrichment:** Extend the chunking pipeline to attach metadata to each chunk: source file, page number, section heading (extracted from document structure), chunk index, character offset start/end, and word count. Store as a list of dictionaries.

4. **Quality Audit:** Build a `ChunkQualityChecker` that flags chunks that are: too short (<50 characters), too long (>2000 characters), contain mostly boilerplate (headers, footers, page numbers), have high Unicode-to-ASCII ratio (potential encoding issues), or are near-duplicates of other chunks.

5. **Parameter Sweep:** For fixed-size chunking, sweep chunk size from 128 to 2048 tokens (in powers of 2) and overlap from 0% to 25%. For each configuration, measure the number of chunks and run 10 test queries through your Module 01 RAG pipeline. Plot retrieval quality vs chunk size.

## Key Takeaways

- Document quality directly determines RAG quality — invest heavily in parsing and cleaning before worrying about embeddings or retrieval.
- There is no universally best chunking strategy; the right choice depends on document structure, query patterns, and embedding model context limits.
- Overlap between chunks prevents information loss at boundaries but increases storage and embedding costs. A 10-15% overlap is a reasonable starting point.
- Metadata attached during processing enables powerful filtering at retrieval time, dramatically improving precision for multi-tenant or categorized data.
- Semantic chunking produces the most coherent chunks but is slower and more expensive than rule-based approaches. Use it when document quality and retrieval quality are paramount.

## Suggested Reading

- Unstructured library documentation
- LangChain text splitters source code (for recursive chunking implementation details)
- Greg Kamradt's "5 Levels of Text Splitting" (visual guide to chunking strategies)
