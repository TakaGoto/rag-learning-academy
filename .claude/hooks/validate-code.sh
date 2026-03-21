#!/usr/bin/env bash
# validate-code.sh — Check Python files for common RAG anti-patterns
# Runs as a PreToolUse hook on Bash commands. Reads tool input from stdin.

set -euo pipefail

# Read the hook input (JSON with tool_input)
INPUT=$(cat)

# Extract the command being run from the tool input
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null || true)

# Only validate commands that write Python files
if [ -z "$COMMAND" ]; then
    exit 0
fi

# Check if this is a command that creates/writes Python content
# Look for Python file creation patterns (cat >, tee, writing .py files)
if ! echo "$COMMAND" | grep -qE '\.(py)\b'; then
    exit 0
fi

WARNINGS=""
SQ="'"

# 1. Check for hardcoded API keys
if echo "$COMMAND" | grep -qiE "(api_key|api[-_]?secret|openai_key|anthropic_key)\s*=\s*[\"${SQ}][A-Za-z0-9_-]{10,}"; then
    WARNINGS="${WARNINGS}
  [WARNING] Hardcoded API key detected.
           Use environment variables: os.environ.get('API_KEY') or load from .env"
fi

# Also catch common key patterns (sk-..., key-..., etc.)
if echo "$COMMAND" | grep -qE "[\"${SQ}](sk-[A-Za-z0-9]{20,}|key-[A-Za-z0-9]{20,})[\"${SQ}]"; then
    WARNINGS="${WARNINGS}
  [WARNING] Possible API key string literal found.
           Never hardcode secrets. Use environment variables or a secrets manager."
fi

# 2. Check for API calls without error handling
# Look for requests/httpx/openai calls not wrapped in try/except
if echo "$COMMAND" | grep -qE '(requests\.(get|post|put)|openai\.|httpx\.|client\.(chat|embeddings|completions))' ; then
    if ! echo "$COMMAND" | grep -qE '(try:|except|raise_for_status|\.status_code)'; then
        WARNINGS="${WARNINGS}
  [WARNING] API call without visible error handling.
           Wrap API calls in try/except and handle rate limits, timeouts, and HTTP errors."
    fi
fi

# 3. Check for chunk sizes that are too large (>2000 tokens)
if echo "$COMMAND" | grep -qiE 'chunk.?size\s*=\s*[0-9]{4,}'; then
    # Extract the number
    SIZE=$(echo "$COMMAND" | grep -oiE 'chunk.?size\s*=\s*[0-9]+' | grep -oE '[0-9]+' | head -1)
    if [ -n "$SIZE" ] && [ "$SIZE" -gt 2000 ] 2>/dev/null; then
        WARNINGS="${WARNINGS}
  [WARNING] Chunk size ${SIZE} exceeds recommended maximum of 2000 tokens.
           Large chunks reduce retrieval precision and waste context window space."
    fi
fi

# Also check for token/size constants >2000 in chunk-related code
if echo "$COMMAND" | grep -qiE '(max_chunk|token_limit|CHUNK_SIZE)\s*=\s*[0-9]{4,}'; then
    SIZE=$(echo "$COMMAND" | grep -oiE '(max_chunk|token_limit|CHUNK_SIZE)\s*=\s*[0-9]+' | grep -oE '[0-9]+' | head -1)
    if [ -n "$SIZE" ] && [ "$SIZE" -gt 2000 ] 2>/dev/null; then
        WARNINGS="${WARNINGS}
  [WARNING] Token/chunk limit of ${SIZE} is above the recommended 2000 threshold.
           Consider smaller chunks for better retrieval quality."
    fi
fi

# Print warnings if any were found
if [ -n "$WARNINGS" ]; then
    echo ""
    echo "  ---- RAG Code Validator ----"
    echo "$WARNINGS"
    echo ""
    echo "  These are warnings, not errors. Review and fix if applicable."
    echo "  ----------------------------"
    echo ""
fi

# Always exit 0 — these are warnings, not blockers
exit 0
