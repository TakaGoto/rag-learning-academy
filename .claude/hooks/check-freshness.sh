#!/usr/bin/env bash
# check-freshness.sh — Warn on session start about content past its review cycle.
#
# Thin wrapper around .github/scripts/content_freshness.sh, which reads each
# file's last_reviewed / review_cycle frontmatter and falls back to git history
# for files without it. The monthly CI workflow runs the same script.
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SCRIPT="$PROJECT_ROOT/.github/scripts/content_freshness.sh"

[ -f "$SCRIPT" ] || exit 0
bash "$SCRIPT" --hook --root "$PROJECT_ROOT"

exit 0
