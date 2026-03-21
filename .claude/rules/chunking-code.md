---
path: src/chunking/**
---

# Chunking Code Rules

## 1. Preserve document metadata through chunking

Every chunk must carry forward the metadata from its parent document.

```python
# Correct
@dataclass
class Chunk:
    text: str
    metadata: dict       # inherited from parent document
    source_doc_id: str
    chunk_index: int

def chunk_document(doc: Document, chunk_size: int) -> list[Chunk]:
    chunks = split_text(doc.text, chunk_size)
    return [
        Chunk(
            text=c,
            metadata={**doc.metadata, "chunk_index": i},
            source_doc_id=doc.id,
            chunk_index=i,
        )
        for i, c in enumerate(chunks)
    ]

# Incorrect - metadata lost
def chunk_document(doc: Document, chunk_size: int) -> list[str]:
    return split_text(doc.text, chunk_size)  # just raw strings
```

## 2. Include source document reference in every chunk

```python
# Correct - every chunk knows where it came from
chunk.source_doc_id = doc.id
chunk.source_file = doc.metadata.get("filename")
chunk.page_number = doc.metadata.get("page")

# Incorrect - orphaned chunks with no provenance
chunks = [Chunk(text=t) for t in split_text(doc.text)]
```

## 3. Validate chunk sizes against model context limits

```python
# Correct
MAX_CHUNK_TOKENS = 512

def validate_chunk(chunk: Chunk, tokenizer) -> bool:
    token_count = len(tokenizer.encode(chunk.text))
    if token_count > MAX_CHUNK_TOKENS:
        raise ValueError(f"Chunk has {token_count} tokens, max is {MAX_CHUNK_TOKENS}")
    return True

# Incorrect - no validation, chunks can silently exceed limits
```

## 4. Support configurable overlap

Overlap prevents information loss at chunk boundaries.

```python
# Correct
def split_text(text: str, chunk_size: int = 512, overlap: int = 50) -> list[str]:
    assert overlap < chunk_size, "overlap must be less than chunk_size"
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start = max(start + 1, end - overlap)  # always advance at least 1
    return chunks

# Incorrect - hardcoded zero overlap
def split_text(text: str, chunk_size: int = 512) -> list[str]:
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
```

## 5. Never split mid-sentence for text content

```python
# Correct
import re

def split_at_sentence_boundary(text: str, max_size: int) -> list[str]:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) + len(sentence) > max_size and current:
            chunks.append(current.strip())
            current = sentence
        elif current:
            current += " " + sentence
        else:
            current = sentence  # avoid leading space on first sentence
    if current.strip():
        chunks.append(current.strip())
    return chunks

# Incorrect - hard character split
chunks = [text[i:i+500] for i in range(0, len(text), 500)]  # splits mid-word/sentence
```
