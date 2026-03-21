#!/usr/bin/env bash
# check-references.sh — Scan for known-deprecated patterns in content and code
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
WARNINGS=()

# Check for deprecated model IDs
DEPRECATED_MODELS="gpt-3.5-turbo|text-embedding-ada-002|claude-2[^-]|claude-instant"
HITS=$(grep -rlE "$DEPRECATED_MODELS" "$PROJECT_ROOT/.claude/" "$PROJECT_ROOT/src/" "$PROJECT_ROOT/data/" 2>/dev/null || true)
if [ -n "$HITS" ]; then
    WARNINGS+=("  Deprecated model IDs found in: $(echo "$HITS" | xargs -I{} basename {} | tr '\n' ', ')")
fi

# Check for old-style LangChain imports in src/
OLD_LC=$(grep -rl "from langchain import\|from langchain\." "$PROJECT_ROOT/src/" 2>/dev/null | grep -v "langchain_core\|langchain_community" || true)
if [ -n "$OLD_LC" ]; then
    WARNINGS+=("  Old-style 'from langchain' imports found. Use langchain-core or langchain-community.")
fi

if [ ${#WARNINGS[@]} -gt 0 ]; then
    echo ""
    echo "  Reference Check:"
    printf '%s\n' "${WARNINGS[@]}"
    echo ""
fi

exit 0
