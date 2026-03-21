#!/usr/bin/env bash
# session-stop.sh — Save a session summary when the session ends

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SESSIONS_DIR="$PROJECT_ROOT/progress/sessions"

# Create sessions directory if needed
mkdir -p "$SESSIONS_DIR"

TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
SESSION_FILE="$SESSIONS_DIR/session_${TIMESTAMP}.md"

# Determine topics covered by checking recently modified files
TOPICS=""
MODIFIED_FILES=""

if command -v git &>/dev/null && git -C "$PROJECT_ROOT" rev-parse --is-inside-work-tree &>/dev/null 2>&1; then
    # Get files modified in this session (last 4 hours as a reasonable window)
    MODIFIED_FILES=$(git -C "$PROJECT_ROOT" diff --name-only HEAD 2>/dev/null || true)
    if [ -z "$MODIFIED_FILES" ]; then
        MODIFIED_FILES=$(git -C "$PROJECT_ROOT" diff --name-only 2>/dev/null || true)
    fi
else
    # Fallback: find files modified in the last 4 hours
    MODIFIED_FILES=$(find "$PROJECT_ROOT/src" -name "*.py" -mmin -240 2>/dev/null | sed "s|$PROJECT_ROOT/||" || true)
fi

NL=$'\n'

# Categorize topics based on modified file paths
if echo "$MODIFIED_FILES" | grep -q "chunking"; then
    TOPICS="${TOPICS}- Document Chunking${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "embedding"; then
    TOPICS="${TOPICS}- Embeddings${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "vector_db"; then
    TOPICS="${TOPICS}- Vector Databases${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "retrieval"; then
    TOPICS="${TOPICS}- Retrieval Strategies${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "generation"; then
    TOPICS="${TOPICS}- Prompt Engineering / Generation${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "evaluation"; then
    TOPICS="${TOPICS}- Evaluation & Metrics${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "pipeline"; then
    TOPICS="${TOPICS}- End-to-End Pipelines${NL}"
fi
if echo "$MODIFIED_FILES" | grep -q "test"; then
    TOPICS="${TOPICS}- Testing${NL}"
fi

if [ -z "$TOPICS" ]; then
    TOPICS="- General exploration${NL}"
fi

# Count files modified
FILE_COUNT=$(echo "$MODIFIED_FILES" | grep -c '.' 2>/dev/null || echo "0")

# Calculate approximate session duration from recent file modification times
SESSION_END=$(date '+%s')
# Try to find the earliest modification in the last 4 hours
EARLIEST_MOD=""
if [ -n "$MODIFIED_FILES" ]; then
    while IFS= read -r f; do
        FULL_PATH="$PROJECT_ROOT/$f"
        if [ -f "$FULL_PATH" ]; then
            MOD_TIME=$(stat -f '%m' "$FULL_PATH" 2>/dev/null || stat -c '%Y' "$FULL_PATH" 2>/dev/null || true)
            if [ -n "$MOD_TIME" ]; then
                if [ -z "$EARLIEST_MOD" ] || [ "$MOD_TIME" -lt "$EARLIEST_MOD" ]; then
                    EARLIEST_MOD="$MOD_TIME"
                fi
            fi
        fi
    done <<< "$MODIFIED_FILES"
fi

DURATION="Unknown"
if [ -n "$EARLIEST_MOD" ]; then
    ELAPSED=$(( SESSION_END - EARLIEST_MOD ))
    if [ "$ELAPSED" -gt 0 ] && [ "$ELAPSED" -lt 14400 ]; then
        MINUTES=$(( ELAPSED / 60 ))
        if [ "$MINUTES" -lt 1 ]; then
            DURATION="< 1 minute"
        elif [ "$MINUTES" -lt 60 ]; then
            DURATION="${MINUTES} minutes"
        else
            HOURS=$(( MINUTES / 60 ))
            REMAINING_MINS=$(( MINUTES % 60 ))
            DURATION="${HOURS}h ${REMAINING_MINS}m"
        fi
    fi
fi

# Write session summary
cat > "$SESSION_FILE" << SESSION_MD
# Session Summary

**Date:** $(date '+%Y-%m-%d %H:%M:%S')
**Duration:** $DURATION
**Files Modified:** $FILE_COUNT

## Topics Covered

${TOPICS}
## Files Changed

$(if [ -n "$MODIFIED_FILES" ]; then echo "$MODIFIED_FILES" | sed 's/^/- /'; else echo "- No files changed"; fi)
SESSION_MD

echo ""
echo "  Session summary saved to: progress/sessions/session_${TIMESTAMP}.md"
echo ""
