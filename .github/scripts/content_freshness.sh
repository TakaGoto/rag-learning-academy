#!/usr/bin/env bash
# content_freshness.sh — Find academy content that is past its review cycle.
#
# The review date comes from each file's `last_reviewed:` frontmatter, falling
# back to the last git commit that touched the file. The threshold comes from
# `review_cycle:` (monthly = 30 days, quarterly = 90, semi-annually = 180;
# files without a cycle get 90). A separate scan flags deprecated model IDs.
#
# Usage:
#   content_freshness.sh                    # Markdown report on stdout
#   content_freshness.sh --report FILE      # write the Markdown report to FILE
#   content_freshness.sh --stale-list FILE  # one stale path per line to FILE
#   content_freshness.sh --hook             # short summary for the session hook
#   content_freshness.sh --root DIR         # scan DIR instead of this repo
#
# When GITHUB_OUTPUT is set, also writes stale_count, warn_count,
# deprecated_count and today for later workflow steps. Always exits 0.
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
REPORT=""
STALE_LIST=""
HOOK_MODE=0
WARN_WINDOW=14 # start warning this many days before a file is due

while [ $# -gt 0 ]; do
    case "$1" in
        --report) REPORT="$2"; shift 2 ;;
        --stale-list) STALE_LIST="$2"; shift 2 ;;
        --root) PROJECT_ROOT="$(cd "$2" && pwd)"; shift 2 ;;
        --hook) HOOK_MODE=1; shift ;;
        *) echo "content_freshness.sh: unknown option $1" >&2; exit 2 ;;
    esac
done

CONTENT_GLOBS=(
    ".claude/docs/curriculum/*.md"
    ".claude/docs/reference/*.md"
    ".claude/docs/templates/*.md"
    ".claude/rules/*.md"
    ".claude/agents/*.md"
    "data/raw/*.md"
)

DEPRECATED_PATTERNS="gpt-3.5-turbo|text-embedding-ada-002|claude-2[^-]|claude-instant"

# Print one frontmatter value (empty when the file has no frontmatter or key).
frontmatter_value() {
    awk -v key="$2" '
        NR == 1 { if ($0 != "---") exit; next }
        $0 == "---" { exit }
        index($0, key ":") == 1 { sub(/^[^:]*:[[:space:]]*/, ""); print; exit }
    ' "$1"
}

# Days since 1970-01-01 for a YYYY-MM-DD date. Pure arithmetic, so it behaves
# the same on macOS and Linux (their `date` flags differ).
days_from_ymd() {
    local y m d era yoe mp doy doe
    y=$((10#${1:0:4}))
    m=$((10#${1:5:2}))
    d=$((10#${1:8:2}))
    if [ "$m" -le 2 ]; then y=$((y - 1)); fi
    era=$((y / 400))
    yoe=$((y - era * 400))
    mp=$(((m + 9) % 12))
    doy=$(((153 * mp + 2) / 5 + d - 1))
    doe=$((yoe * 365 + yoe / 4 - yoe / 100 + doy))
    echo $((era * 146097 + doe - 719468))
}

cycle_days() {
    case "$1" in
        monthly) echo 30 ;;
        quarterly) echo 90 ;;
        semi-annually | semiannually) echo 180 ;;
        annually | yearly) echo 365 ;;
        *) echo 90 ;;
    esac
}

TODAY="$(date +%Y-%m-%d)"
TODAY_DAYS=$(($(date +%s) / 86400))
STALE_ROWS=()
WARN_ROWS=()
STALE_PATHS=()
HOOK_LINES=()
OK_COUNT=0

cd "$PROJECT_ROOT"

for pattern in "${CONTENT_GLOBS[@]}"; do
    # shellcheck disable=SC2086  # the pattern is meant to glob
    for f in $pattern; do
        [ -f "$f" ] || continue
        last="$(frontmatter_value "$f" last_reviewed)"
        cycle="$(frontmatter_value "$f" review_cycle)"
        source="frontmatter"
        if [[ "$last" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
            ref_days="$(days_from_ymd "$last")"
        else
            ts="$(git log -1 --format=%ct -- "$f" 2>/dev/null || true)"
            [ -n "$ts" ] || continue
            ref_days=$((ts / 86400))
            last="$(git log -1 --format=%cs -- "$f")"
            source="git"
        fi
        max="$(cycle_days "$cycle")"
        [ -n "$cycle" ] || cycle="none (90d default)"
        age=$((TODAY_DAYS - ref_days))
        if [ "$age" -gt "$max" ]; then
            STALE_ROWS+=("| :red_circle: STALE | \`$f\` | $cycle | $last ($source) | $age | $((age - max)) days overdue |")
            STALE_PATHS+=("$f")
            HOOK_LINES+=("  - $f ($((age - max)) days overdue, $cycle)")
        elif [ $((max - age)) -le "$WARN_WINDOW" ]; then
            WARN_ROWS+=("| :yellow_circle: DUE SOON | \`$f\` | $cycle | $last ($source) | $age | due in $((max - age)) days |")
        else
            OK_COUNT=$((OK_COUNT + 1))
        fi
    done
done

# Deprecated model IDs in content and code. Skip .claude/hooks: the hook that
# defines the pattern list would otherwise flag itself every month.
DEPRECATED_HITS="$(grep -rnE "$DEPRECATED_PATTERNS" --exclude-dir=hooks .claude/ src/ data/ 2>/dev/null || true)"
DEPRECATED_COUNT=0
if [ -n "$DEPRECATED_HITS" ]; then
    DEPRECATED_COUNT="$(printf '%s\n' "$DEPRECATED_HITS" | wc -l | tr -d ' ')"
fi

STALE_COUNT=${#STALE_PATHS[@]}
WARN_COUNT=${#WARN_ROWS[@]}

if [ "$HOOK_MODE" -eq 1 ]; then
    if [ "$STALE_COUNT" -gt 0 ] || [ "$DEPRECATED_COUNT" -gt 0 ]; then
        echo ""
        if [ "$STALE_COUNT" -gt 0 ]; then
            echo "  Content Freshness Warning: $STALE_COUNT files are past their review cycle:"
            printf '%s\n' "${HOOK_LINES[@]}"
        fi
        if [ "$DEPRECATED_COUNT" -gt 0 ]; then
            echo "  Deprecated model references: $DEPRECATED_COUNT line(s). Run /audit-content for details."
        fi
        echo ""
        echo "  Run /audit-content to review and update stale materials."
        echo ""
    fi
    exit 0
fi

build_report() {
    echo "## Content Freshness Report — $TODAY"
    echo ""
    echo "### Review-cycle status"
    echo ""
    echo "Dates come from each file's \`last_reviewed\` frontmatter (or git history when it has none); thresholds from \`review_cycle\`."
    echo ""
    if [ "$STALE_COUNT" -gt 0 ] || [ "$WARN_COUNT" -gt 0 ]; then
        echo "| Status | File | Cycle | Last reviewed | Age (days) | Note |"
        echo "|--------|------|-------|---------------|------------|------|"
        if [ "$STALE_COUNT" -gt 0 ]; then printf '%s\n' "${STALE_ROWS[@]}"; fi
        if [ "$WARN_COUNT" -gt 0 ]; then printf '%s\n' "${WARN_ROWS[@]}"; fi
        echo ""
    fi
    echo "**Summary:** $STALE_COUNT past their review cycle, $WARN_COUNT due within $WARN_WINDOW days, $OK_COUNT current."
    echo ""
    echo "### Deprecated Pattern Scan"
    echo ""
    if [ "$DEPRECATED_COUNT" -gt 0 ]; then
        echo "**Deprecated model references found:**"
        echo '```'
        printf '%s\n' "$DEPRECATED_HITS"
        echo '```'
    else
        echo "No deprecated model references found."
    fi
}

if [ -n "$REPORT" ]; then
    build_report > "$REPORT"
    echo "Freshness report written to $REPORT ($STALE_COUNT stale, $WARN_COUNT due soon, $DEPRECATED_COUNT deprecated hits)"
else
    build_report
fi

if [ -n "$STALE_LIST" ]; then
    : > "$STALE_LIST"
    if [ "$STALE_COUNT" -gt 0 ]; then printf '%s\n' "${STALE_PATHS[@]}" > "$STALE_LIST"; fi
fi

if [ -n "${GITHUB_OUTPUT:-}" ]; then
    {
        echo "stale_count=$STALE_COUNT"
        echo "warn_count=$WARN_COUNT"
        echo "deprecated_count=$DEPRECATED_COUNT"
        echo "today=$TODAY"
    } >> "$GITHUB_OUTPUT"
fi

exit 0
