#!/usr/bin/env bash
# session-start.sh — Compact welcome for RAG Learning Academy

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PROGRESS_DIR="$PROJECT_ROOT/progress"
PROFILE_FILE="$PROGRESS_DIR/learner-profile.md"
TRACKER_FILE="$PROGRESS_DIR/module-tracker.md"

echo ""
echo "  RAG Learning Academy"
echo ""

if [ -f "$PROFILE_FILE" ] && [ -f "$TRACKER_FILE" ]; then
    CURRENT_MODULE=$(grep -i 'current module' "$PROFILE_FILE" 2>/dev/null | head -1 | sed 's/.*: *//' || echo "")
    COMPLETED=$(grep -c '\[x\]' "$TRACKER_FILE" 2>/dev/null || echo "0")
    TOTAL=$(grep -c '\[.\]' "$TRACKER_FILE" 2>/dev/null || echo "?")
    [ -n "$CURRENT_MODULE" ] && echo "  Current: $CURRENT_MODULE | Progress: $COMPLETED/$TOTAL lessons"
    [ -z "$CURRENT_MODULE" ] && echo "  Progress: $COMPLETED/$TOTAL lessons"
else
    echo "  New learner — run /start to begin"
fi

echo "  Use /roadmap for full progress | /triage if unsure where to go"
echo ""
