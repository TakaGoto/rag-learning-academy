#!/usr/bin/env bash
# check-freshness.sh — Warn about content files not updated in 90+ days
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
STALE_DAYS=90
NOW=$(date +%s)
STALE_FILES=()

for f in "$PROJECT_ROOT"/.claude/docs/curriculum/*.md \
         "$PROJECT_ROOT"/.claude/agents/*.md \
         "$PROJECT_ROOT"/.claude/docs/reference/*.md \
         "$PROJECT_ROOT"/.claude/rules/*.md \
         "$PROJECT_ROOT"/data/raw/*.md; do
    [ -f "$f" ] || continue
    LAST_COMMIT=$(git -C "$PROJECT_ROOT" log -1 --format="%ct" -- "$f" 2>/dev/null || echo "0")
    if [ "$LAST_COMMIT" -gt 0 ]; then
        AGE_DAYS=$(( (NOW - LAST_COMMIT) / 86400 ))
        if [ "$AGE_DAYS" -gt "$STALE_DAYS" ]; then
            BASENAME=$(basename "$f")
            STALE_FILES+=("  - $BASENAME ($AGE_DAYS days)")
        fi
    fi
done

if [ ${#STALE_FILES[@]} -gt 0 ]; then
    echo ""
    echo "  Content Freshness Warning: ${#STALE_FILES[@]} files not updated in ${STALE_DAYS}+ days:"
    printf '%s\n' "${STALE_FILES[@]}"
    echo ""
    echo "  Run /audit-content to review and update stale materials."
    echo ""
fi

exit 0
