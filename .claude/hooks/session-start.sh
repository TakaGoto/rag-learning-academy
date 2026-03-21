#!/usr/bin/env bash
# session-start.sh — Welcome message and progress summary for RAG Learning Academy

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PROGRESS_DIR="$PROJECT_ROOT/progress"

echo ""
echo "=============================================="
echo "   RAG Learning Academy - Session Start"
echo "=============================================="
echo ""

# Show current date/time
echo "  Date: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Check for progress directory and show learner status
PROFILE_FILE="$PROGRESS_DIR/learner-profile.md"
TRACKER_FILE="$PROGRESS_DIR/module-tracker.md"

if [ -d "$PROGRESS_DIR" ] && { [ -f "$PROFILE_FILE" ] || [ -f "$TRACKER_FILE" ]; }; then
    echo "----------------------------------------------"
    echo "  Your Progress"
    echo "----------------------------------------------"

    # Read current module from learner-profile.md
    if [ -f "$PROFILE_FILE" ]; then
        CURRENT_MODULE=$(grep -i 'current module' "$PROFILE_FILE" 2>/dev/null | head -1 | sed 's/.*: *//' || echo "Unknown")
        [ -z "$CURRENT_MODULE" ] && CURRENT_MODULE="Unknown"
        echo "  Current Module : $CURRENT_MODULE"
    fi

    # Read completion info from module-tracker.md
    if [ -f "$TRACKER_FILE" ]; then
        COMPLETED=$(grep -c '\[x\]' "$TRACKER_FILE" 2>/dev/null || echo "0")
        TOTAL=$(grep -c '\[.\]' "$TRACKER_FILE" 2>/dev/null || echo "?")
        echo "  Lessons Done   : $COMPLETED / $TOTAL"
    fi

    # Show recent session if it exists
    SESSIONS_DIR="$PROGRESS_DIR/sessions"
    if [ -d "$SESSIONS_DIR" ]; then
        LATEST_SESSION=$(ls -t "$SESSIONS_DIR"/*.md 2>/dev/null | head -1)
        if [ -n "$LATEST_SESSION" ]; then
            echo ""
            echo "  Last session: $(basename "$LATEST_SESSION" .md)"
        fi
    fi
else
    echo "----------------------------------------------"
    echo "  Welcome, new learner!"
    echo "----------------------------------------------"
    echo "  No progress found yet. Start with Module 1"
    echo "  to begin your RAG learning journey."
fi

echo ""
echo "----------------------------------------------"
echo "  Available Commands"
echo "----------------------------------------------"
echo "  /lesson    - Start or continue a lesson"
echo "  /quiz      - Take a quiz on current module"
echo "  /challenge - Attempt a coding challenge"
echo "  /roadmap   - View detailed progress"
echo "  /explain   - Deep-dive explanation of any concept"
echo ""
echo "----------------------------------------------"
echo "  Modules"
echo "----------------------------------------------"
echo "  1. Foundations"
echo "  2. Document Processing"
echo "  3. Embeddings"
echo "  4. Vector Databases"
echo "  5. Retrieval Strategies"
echo "  6. Generation"
echo "  7. Evaluation"
echo "  8. Advanced Patterns"
echo "  9. Production"
echo ""
echo "=============================================="
echo ""
