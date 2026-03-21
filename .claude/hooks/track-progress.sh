#!/usr/bin/env bash
# track-progress.sh — Update learner progress when a lesson/quiz/challenge is completed
#
# This is a utility script that skills can call to update the JSON-based progress
# tracking. The skills themselves write markdown files to progress/, but this script
# maintains a structured learner.json for programmatic access (session-start.sh,
# progress summaries, etc.).
#
# Usage:
#   track-progress.sh lesson <module_number> <lesson_name>
#   track-progress.sh quiz <module_number> <score>
#   track-progress.sh challenge <module_number> <challenge_name>

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PROGRESS_DIR="$PROJECT_ROOT/progress"
PROGRESS_FILE="$PROGRESS_DIR/learner.json"

# Ensure progress directory exists
mkdir -p "$PROGRESS_DIR"

# Initialize progress file if it doesn't exist
if [ ! -f "$PROGRESS_FILE" ]; then
    cat > "$PROGRESS_FILE" << INIT_JSON
{
  "current_module": "Module 1: Foundations",
  "completed_lessons": [],
  "completed_quizzes": [],
  "completed_challenges": [],
  "quiz_scores": {},
  "total_lessons": 36,
  "streak_days": 1,
  "last_activity": "$(date '+%Y-%m-%d')",
  "started_at": "$(date '+%Y-%m-%d')"
}
INIT_JSON
    echo "  Initialized new learner progress file."
fi

if [ $# -lt 2 ]; then
    echo "Usage: track-progress.sh <type> <module_number> [name_or_score]"
    echo ""
    echo "Types:"
    echo "  lesson    - Mark a lesson as completed"
    echo "  quiz      - Record a quiz score"
    echo "  challenge - Mark a challenge as completed"
    exit 1
fi

TYPE="$1"
MODULE="$2"
VALUE="${3:-}"
TODAY=$(date '+%Y-%m-%d')

# Update streak
LAST_ACTIVITY=$(jq -r '.last_activity // ""' "$PROGRESS_FILE" 2>/dev/null || echo "")
YESTERDAY=$(date -v-1d '+%Y-%m-%d' 2>/dev/null || date -d 'yesterday' '+%Y-%m-%d' 2>/dev/null || echo "")

if [ "$LAST_ACTIVITY" = "$YESTERDAY" ]; then
    # Continue streak
    jq ".streak_days += 1 | .last_activity = \"$TODAY\"" "$PROGRESS_FILE" > "${PROGRESS_FILE}.tmp" && mv "${PROGRESS_FILE}.tmp" "$PROGRESS_FILE"
elif [ "$LAST_ACTIVITY" != "$TODAY" ]; then
    # Reset streak
    jq ".streak_days = 1 | .last_activity = \"$TODAY\"" "$PROGRESS_FILE" > "${PROGRESS_FILE}.tmp" && mv "${PROGRESS_FILE}.tmp" "$PROGRESS_FILE"
fi

MODULE_NAMES=(
    ""
    "Module 1: Foundations"
    "Module 2: Document Processing"
    "Module 3: Embeddings"
    "Module 4: Vector Databases"
    "Module 5: Retrieval Strategies"
    "Module 6: Generation"
    "Module 7: Evaluation"
    "Module 8: Advanced Patterns"
    "Module 9: Production"
)

case "$TYPE" in
    lesson)
        ENTRY="module_${MODULE}:${VALUE:-lesson}"
        jq --arg entry "$ENTRY" '
            if (.completed_lessons | index($entry)) then .
            else .completed_lessons += [$entry]
            end
        ' "$PROGRESS_FILE" > "${PROGRESS_FILE}.tmp" && mv "${PROGRESS_FILE}.tmp" "$PROGRESS_FILE"
        echo "  Lesson completed: $ENTRY"
        ;;

    quiz)
        SCORE="${VALUE:-0}"
        jq --arg mod "module_$MODULE" --arg score "$SCORE" '
            .quiz_scores[$mod] = ($score | tonumber) |
            if (.completed_quizzes | index($mod)) then .
            else .completed_quizzes += [$mod]
            end
        ' "$PROGRESS_FILE" > "${PROGRESS_FILE}.tmp" && mv "${PROGRESS_FILE}.tmp" "$PROGRESS_FILE"
        echo "  Quiz recorded: Module $MODULE - Score: $SCORE"
        ;;

    challenge)
        ENTRY="module_${MODULE}:${VALUE:-challenge}"
        jq --arg entry "$ENTRY" '
            if (.completed_challenges | index($entry)) then .
            else .completed_challenges += [$entry]
            end
        ' "$PROGRESS_FILE" > "${PROGRESS_FILE}.tmp" && mv "${PROGRESS_FILE}.tmp" "$PROGRESS_FILE"
        echo "  Challenge completed: $ENTRY"
        ;;

    *)
        echo "  Unknown type: $TYPE"
        echo "  Use: lesson, quiz, or challenge"
        exit 1
        ;;
esac

# Update current module based on progress
COMPLETED_COUNT=$(jq '.completed_lessons | length' "$PROGRESS_FILE" 2>/dev/null || echo "0")
# Roughly 4 lessons per module
CURRENT_MODULE_NUM=$(( (COMPLETED_COUNT / 4) + 1 ))
if [ "$CURRENT_MODULE_NUM" -gt 9 ]; then
    CURRENT_MODULE_NUM=9
fi
CURRENT_MODULE="${MODULE_NAMES[$CURRENT_MODULE_NUM]}"

jq --arg mod "$CURRENT_MODULE" '.current_module = $mod' "$PROGRESS_FILE" > "${PROGRESS_FILE}.tmp" && mv "${PROGRESS_FILE}.tmp" "$PROGRESS_FILE"

echo ""
echo "  Progress updated. Current module: $CURRENT_MODULE"
echo "  Total lessons completed: $COMPLETED_COUNT"
echo ""
