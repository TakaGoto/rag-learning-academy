#!/usr/bin/env bash
# session-start.sh — Compact welcome for RAG Learning Academy

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PROGRESS_DIR="$PROJECT_ROOT/progress"
PROFILE_FILE="$PROGRESS_DIR/learner-profile.md"
TRACKER_FILE="$PROGRESS_DIR/module-tracker.md"
STREAK_FILE="$PROGRESS_DIR/streaks.md"

echo ""
echo "  RAG Learning Academy"
echo ""

if [ -f "$PROFILE_FILE" ] && [ -f "$TRACKER_FILE" ]; then
    CURRENT_MODULE=$(grep -i 'current module' "$PROFILE_FILE" 2>/dev/null | head -1 | sed 's/.*: *//' || echo "")
    COMPLETED=$(grep -c '\[x\]' "$TRACKER_FILE" 2>/dev/null || echo "0")
    TOTAL=$(grep -c '\[.\]' "$TRACKER_FILE" 2>/dev/null || echo "?")

    # Streak tracking
    TODAY=$(date '+%Y-%m-%d')
    STREAK_DISPLAY=""
    if [ -f "$STREAK_FILE" ]; then
        LAST_DATE=$(grep -i 'last_active' "$STREAK_FILE" 2>/dev/null | head -1 | sed 's/.*: *//' || echo "")
        CURRENT_STREAK=$(grep -i 'current_streak' "$STREAK_FILE" 2>/dev/null | head -1 | sed 's/.*: *//' || echo "0")
        YESTERDAY=$(date -v-1d '+%Y-%m-%d' 2>/dev/null || date -d 'yesterday' '+%Y-%m-%d' 2>/dev/null || echo "")

        if [ "$LAST_DATE" = "$TODAY" ]; then
            STREAK_DISPLAY=" | Streak: ${CURRENT_STREAK}d"
        elif [ "$LAST_DATE" = "$YESTERDAY" ]; then
            NEW_STREAK=$((CURRENT_STREAK + 1))
            STREAK_DISPLAY=" | Streak: ${NEW_STREAK}d"
            # Update streak file
            sed -i.bak "s/current_streak: .*/current_streak: $NEW_STREAK/" "$STREAK_FILE" 2>/dev/null && rm -f "${STREAK_FILE}.bak"
            sed -i.bak "s/last_active: .*/last_active: $TODAY/" "$STREAK_FILE" 2>/dev/null && rm -f "${STREAK_FILE}.bak"
        else
            STREAK_DISPLAY=" | Streak: 1d (welcome back!)"
            sed -i.bak "s/current_streak: .*/current_streak: 1/" "$STREAK_FILE" 2>/dev/null && rm -f "${STREAK_FILE}.bak"
            sed -i.bak "s/last_active: .*/last_active: $TODAY/" "$STREAK_FILE" 2>/dev/null && rm -f "${STREAK_FILE}.bak"
        fi
    else
        # Create streak file
        mkdir -p "$PROGRESS_DIR"
        cat > "$STREAK_FILE" << STREAKEOF
# Learning Streaks
current_streak: 1
longest_streak: 1
last_active: $TODAY
STREAKEOF
        STREAK_DISPLAY=" | Streak: 1d"
    fi

    [ -n "$CURRENT_MODULE" ] && echo "  Current: $CURRENT_MODULE | Progress: $COMPLETED/$TOTAL lessons${STREAK_DISPLAY}"
    [ -z "$CURRENT_MODULE" ] && echo "  Progress: $COMPLETED/$TOTAL lessons${STREAK_DISPLAY}"
else
    echo "  New learner — run /start to begin"
fi

echo "  Use /roadmap for full progress | /triage if unsure where to go"
echo ""
