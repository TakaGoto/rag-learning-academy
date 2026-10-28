#!/usr/bin/env bash
# freshness_routine.sh — Local monthly routine: review content that is past its
# review cycle with Claude Code (your subscription; no API key), open a PR,
# wait for CI, and merge it.
#
# The GitHub Action (.github/workflows/content-freshness.yml) only reports;
# this script does the fixing, from a maintainer's machine.
#
# Usage:
#   scripts/freshness_routine.sh --check      # verify gh / claude / python / ruff are ready
#   scripts/freshness_routine.sh --install    # macOS: launchd job on the 2nd of each month, 10:00
#   scripts/freshness_routine.sh --uninstall  # remove that launchd job
#   scripts/freshness_routine.sh              # run once now
#   scripts/freshness_routine.sh --dry-run    # review + commit on a branch, but no push / PR / merge
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LABEL="com.rag-learning-academy.freshness"
LOG_DIR="$HOME/Library/Logs"
LOG_FILE="$LOG_DIR/rag-academy-freshness.log"
REPORT_TITLE="Monthly Content Freshness Report"
MAX_MINUTES=90 # wall-clock cap for the Claude Code run
ALLOWED_TOOLS="Read,Edit,MultiEdit,Write,Glob,Grep,WebSearch,WebFetch,Bash(python3 -m pytest:*)"
TEST_FILES=(tests/test_structure.py tests/test_cross_references.py tests/test_content.py tests/test_hooks.py)
MODE=run
DRY_RUN=0

for arg in "$@"; do
    case "$arg" in
        --check) MODE=check ;;
        --install) MODE=install ;;
        --uninstall) MODE=uninstall ;;
        --dry-run) DRY_RUN=1 ;;
        -h | --help) sed -n '2,15p' "$0"; exit 0 ;;
        *) echo "freshness_routine.sh: unknown option $arg" >&2; exit 2 ;;
    esac
done

# launchd starts jobs with a bare PATH; add the usual tool locations. The
# native Claude Code install (~/.local/bin) goes first so it beats an older
# npm copy under nvm.
for d in "$HOME"/.nvm/versions/node/*/bin; do
    [ -d "$d" ] && PATH="$d:$PATH"
done
export PATH="$HOME/.local/bin:$HOME/.claude/local:/opt/homebrew/bin:/usr/local/bin:$PATH"
# A nested Claude Code session refuses to start; this script may be launched from one.
unset CLAUDECODE

log() { printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"; }
die() { log "ERROR: $*"; exit 1; }
need() { command -v "$1" > /dev/null 2>&1 || die "$1 not found on PATH"; }

check_deps() {
    for c in git gh claude python3 ruff; do need "$c"; done
    gh auth status > /dev/null 2>&1 || die "gh is not logged in (run: gh auth login)"
    python3 -c "import pytest, yaml" 2> /dev/null || die "pytest/pyyaml missing (pip install pytest pyyaml)"
    log "git:     $(git --version)"
    log "gh:      $(gh --version | head -1) ($(command -v gh))"
    log "claude:  $(claude --version 2> /dev/null | head -1) ($(command -v claude))"
    log "python3: $(python3 --version) ($(command -v python3))"
    log "ruff:    $(ruff --version) ($(command -v ruff))"
    log "repo:    $REPO_ROOT ($(git -C "$REPO_ROOT" remote get-url origin))"
    log "deps ok"
}

install_launchd() {
    [ "$(uname)" = "Darwin" ] || die "--install writes a launchd job and only works on macOS; use cron elsewhere"
    check_deps
    local plist="$HOME/Library/LaunchAgents/$LABEL.plist"
    local clean_path
    clean_path="$(printf '%s' "$PATH" | tr ':' '\n' | grep -v cmux | paste -sd: -)" # terminal shims don't exist outside the terminal
    mkdir -p "$HOME/Library/LaunchAgents" "$LOG_DIR"
    cat > "$plist" << PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$REPO_ROOT/scripts/freshness_routine.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Day</key><integer>2</integer>
    <key>Hour</key><integer>10</integer>
    <key>Minute</key><integer>0</integer>
  </dict>
  <key>StandardOutPath</key><string>$LOG_FILE</string>
  <key>StandardErrorPath</key><string>$LOG_FILE</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key><string>$clean_path</string>
    <key>HOME</key><string>$HOME</string>
  </dict>
</dict>
</plist>
PLIST
    launchctl bootout "gui/$(id -u)" "$plist" 2> /dev/null || true
    launchctl bootstrap "gui/$(id -u)" "$plist"
    log "installed $LABEL: runs on the 2nd of each month at 10:00 local time (or at next wake if the Mac was asleep)"
    log "log file: $LOG_FILE"
    log "run it now with: launchctl kickstart gui/$(id -u)/$LABEL"
}

uninstall_launchd() {
    local plist="$HOME/Library/LaunchAgents/$LABEL.plist"
    launchctl bootout "gui/$(id -u)" "$plist" 2> /dev/null || true
    rm -f "$plist"
    log "removed $LABEL"
}

run_review() {
    check_deps
    cd "$REPO_ROOT"
    if ! git diff --quiet || ! git diff --cached --quiet; then
        die "working tree has uncommitted changes; refusing to run"
    fi
    git fetch -q origin
    git checkout -q main
    git merge -q --ff-only origin/main

    local today work stale issue branch prompt url
    today="$(date +%Y-%m-%d)"
    work="$(mktemp -d)"
    bash .github/scripts/content_freshness.sh --report "$work/report.md" --stale-list "$work/stale.txt" > /dev/null
    stale="$(grep -c . "$work/stale.txt" || true)"
    issue="$(gh issue list --state open --label content-review --search "\"$REPORT_TITLE\" in:title" --json number --jq '.[0].number // empty')"

    if [ "$stale" -eq 0 ]; then
        log "nothing is past its review cycle"
        if [ -n "$issue" ] && [ "$DRY_RUN" -eq 0 ]; then
            gh issue close "$issue" --comment "Local freshness routine: every content file is within its review cycle as of $today. Closing."
            log "closed tracking issue #$issue"
        fi
        return 0
    fi
    log "$stale file(s) past their review cycle${issue:+ (tracking issue #$issue)}"

    branch="content/freshness-$(date +%Y-%m)"
    git checkout -q -B "$branch"
    cp "$work/report.md" freshness-report.md
    cp "$work/stale.txt" stale-files.txt

    prompt="$(cat << 'PROMPT'
You are running the RAG Learning Academy's monthly content-freshness review. Today is __TODAY__.

`freshness-report.md` in the repo root is this month's report, and `stale-files.txt` lists one content file per line that is past its review cycle. Review and update ONLY the files in `stale-files.txt`.

For each stale file:
1. Read the whole file.
2. Find every time-sensitive claim: model names and API model IDs, context windows, prices, library versions and import paths, vendor product names, papers described as "recent" or "new", and code that may no longer run on current library versions.
3. Verify each one with WebSearch or WebFetch against official sources (Anthropic model docs, OpenAI docs, PyPI, the MTEB leaderboard, library changelogs). Never guess a model ID, price, or version number. If you cannot verify a claim, leave the text alone and list it in your summary.
4. Fix what is outdated with surgical edits. Keep headings, section order, tables, lesson and exercise numbering, cross-references, and the number of code blocks. Match the voice described in CLAUDE.md. Do not add lessons, sections, agents, or exercises.
5. Set `last_reviewed:` in the file's frontmatter to today's date, including files where nothing else needed changing, because you reviewed them. In `.claude/agents/*.md` change only that key; Claude Code reads the rest of that frontmatter.

Constraints: do not use git; do not create, rename, or delete files; do not edit tests, hooks, workflows, or `.claude/settings.json`. The tests enforce: Python code blocks must compile; the strings gpt-3.5-turbo, text-embedding-ada-002, claude-2 and claude-instant may not appear in content; agent files keep their `## Delegation Rules` section; the glossary keeps `## Terms by Topic`.

When you are done, run `python3 -m pytest tests/test_content.py tests/test_cross_references.py tests/test_structure.py -q` and fix any failure you caused. Then write `freshness-summary.md` in the repo root: a short Markdown summary for the pull request with one bullet per file (what changed, or "reviewed, no change needed") followed by a "Could not verify" list. Write nothing else there.
PROMPT
)"
    prompt="${prompt//__TODAY__/$today}"

    log "running Claude Code on $stale file(s) (wall-clock cap ${MAX_MINUTES}m; this can take a while)"
    local claude_pid watchdog_pid
    claude -p "$prompt" --allowedTools "$ALLOWED_TOOLS" --output-format text > "$work/claude.txt" 2>&1 &
    claude_pid=$!
    (sleep $((MAX_MINUTES * 60)) && kill "$claude_pid" 2> /dev/null) &
    watchdog_pid=$!
    if ! wait "$claude_pid"; then
        log "claude exited non-zero or hit the ${MAX_MINUTES}m cap (see $work/claude.txt); checking the working tree anyway"
    fi
    kill "$watchdog_pid" 2> /dev/null || true
    rm -f freshness-report.md stale-files.txt
    git diff --quiet && die "Claude made no changes; transcript: $work/claude.txt"

    log "running the test gate"
    if ! python3 -m pytest "${TEST_FILES[@]}" -q > "$work/tests.txt" 2>&1; then
        tail -40 "$work/tests.txt"
        if [ -n "$issue" ] && [ "$DRY_RUN" -eq 0 ]; then
            gh issue comment "$issue" --body "Local freshness routine on $today: Claude's edits failed the test gate, so nothing was pushed. Branch \`$branch\` is left on the maintainer's machine for inspection."
        fi
        die "test gate failed; branch $branch left in place for inspection"
    fi
    if ! ruff check tests/ src/ .github/scripts/ -q || ! ruff format --check tests/ src/ .github/scripts/ -q; then
        die "ruff failed on $branch"
    fi

    git add .claude data projects requirements.txt README.md CLAUDE.md
    git commit -q -m "content: monthly freshness review $today"
    log "committed $(git diff --stat HEAD~1 | tail -1)"

    {
        echo "Automated monthly freshness review, run by \`scripts/freshness_routine.sh\` on a maintainer's machine on $today."
        echo
        echo "## What changed"
        echo
        if [ -s freshness-summary.md ]; then cat freshness-summary.md; else echo "_Claude did not write a summary; see the diff._"; fi
        echo
        echo "<details><summary>Freshness report that triggered this run</summary>"
        echo
        cat "$work/report.md"
        echo
        echo "</details>"
        if [ -n "$issue" ]; then
            echo
            echo "Closes #$issue"
        fi
    } > "$work/pr-body.md"
    rm -f freshness-summary.md

    if [ "$DRY_RUN" -eq 1 ]; then
        log "dry run: committed on $branch; PR body at $work/pr-body.md; nothing pushed"
        return 0
    fi

    git push -q -u origin "$branch" --force-with-lease
    url="$(gh pr create --base main --head "$branch" --title "Content freshness review — $today" --body-file "$work/pr-body.md" --label content-review --label automated)"
    log "opened $url"
    if ! gh pr checks "$branch" --watch --fail-fast > /dev/null; then
        die "CI failed on $url; not merging"
    fi
    gh pr merge "$branch" --squash --delete-branch
    log "merged $url"
    git checkout -q main
    git pull -q --ff-only
}

mkdir -p "$LOG_DIR"
case "$MODE" in
    check) check_deps ;;
    install) install_launchd ;;
    uninstall) uninstall_launchd ;;
    run) run_review ;;
esac
