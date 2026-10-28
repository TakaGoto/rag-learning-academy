"""
Integration tests for hook scripts — verify they execute without errors.
"""

import os
import subprocess

import pytest
from academy_fixtures import HOOKS_DIR, ROOT


class TestHookExecution:
    """Verify hook scripts run successfully."""

    @pytest.mark.parametrize(
        "hook",
        ["check-freshness.sh", "check-references.sh"],
    )
    def test_hook_runs_without_error(self, hook):
        """Hook scripts should always exit 0 (informational only)."""
        path = HOOKS_DIR / hook
        result = subprocess.run(
            [str(path)],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            timeout=30,
        )
        assert result.returncode == 0, (
            f"{hook} exited with {result.returncode}:\nstdout: {result.stdout}\nstderr: {result.stderr}"
        )

    @pytest.mark.parametrize(
        "hook",
        ["check-freshness.sh", "check-references.sh"],
    )
    def test_hook_output_is_clean(self, hook):
        """Hook output should not contain error traces."""
        path = HOOKS_DIR / hook
        result = subprocess.run(
            [str(path)],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            timeout=30,
        )
        assert "syntax error" not in result.stderr.lower(), f"{hook} has syntax errors"
        assert "command not found" not in result.stderr.lower(), f"{hook} has missing commands"

    def test_check_freshness_uses_git(self):
        """check-freshness.sh should reference git for date checking."""
        text = (HOOKS_DIR / "check-freshness.sh").read_text()
        assert "git" in text, "check-freshness.sh should use git for date checking"

    def test_check_references_has_patterns(self):
        """check-references.sh should define deprecated patterns to scan."""
        text = (HOOKS_DIR / "check-references.sh").read_text()
        assert "gpt-3.5-turbo" in text or "DEPRECATED" in text, (
            "check-references.sh should define deprecated model patterns"
        )


# ---------------------------------------------------------------------------
# Deprecated-pattern scan must not flag the script that defines the patterns
# ---------------------------------------------------------------------------


class TestReferenceCheckSelfMatch:
    def test_check_references_does_not_flag_itself(self):
        """Regression: the hook used to report its own DEPRECATED_MODELS line every run."""
        result = subprocess.run(
            [str(HOOKS_DIR / "check-references.sh")],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            timeout=30,
        )
        assert "check-references.sh" not in result.stdout, result.stdout


# ---------------------------------------------------------------------------
# Shared freshness script (used by the session hook and the monthly workflow)
# ---------------------------------------------------------------------------

FRESHNESS_SCRIPT = ROOT / ".github" / "scripts" / "content_freshness.sh"


def run_freshness(*args, env=None):
    return subprocess.run(
        ["bash", str(FRESHNESS_SCRIPT), *args],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
        timeout=60,
        env=env,
    )


class TestFreshnessScript:
    def test_report_mode_runs_clean(self, tmp_path):
        report = tmp_path / "report.md"
        stale = tmp_path / "stale.txt"
        result = run_freshness("--report", str(report), "--stale-list", str(stale))
        assert result.returncode == 0, result.stderr
        text = report.read_text()
        assert "## Content Freshness Report" in text
        assert "### Deprecated Pattern Scan" in text
        assert "check-references.sh" not in text, "the deprecated scan must skip .claude/hooks"
        assert stale.exists()

    def test_hook_mode_runs_clean(self):
        result = run_freshness("--hook")
        assert result.returncode == 0, result.stderr
        assert "error" not in result.stderr.lower(), result.stderr

    def test_honors_review_cycle_frontmatter(self, tmp_path):
        """A monthly file reviewed yesterday is current; a semi-annual file reviewed last year is stale."""
        from datetime import date, timedelta

        docs = tmp_path / ".claude" / "docs" / "curriculum"
        docs.mkdir(parents=True)
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        (docs / "fresh.md").write_text(f"---\nlast_reviewed: {yesterday}\nreview_cycle: monthly\n---\n# Fresh\n")
        (docs / "old.md").write_text("---\nlast_reviewed: 2025-01-01\nreview_cycle: semi-annually\n---\n# Old\n")
        (docs / "bare.md").write_text("# No frontmatter and no git history: skipped, not a crash\n")
        stale = tmp_path / "stale.txt"
        result = run_freshness("--root", str(tmp_path), "--stale-list", str(stale), "--report", str(tmp_path / "r.md"))
        assert result.returncode == 0, result.stderr
        stale_paths = stale.read_text().split()
        assert ".claude/docs/curriculum/old.md" in stale_paths
        assert ".claude/docs/curriculum/fresh.md" not in stale_paths
        assert ".claude/docs/curriculum/bare.md" not in stale_paths

    def test_writes_github_outputs(self, tmp_path):
        out = tmp_path / "gh_output"
        out.touch()
        result = run_freshness("--report", str(tmp_path / "r.md"), env={**os.environ, "GITHUB_OUTPUT": str(out)})
        assert result.returncode == 0, result.stderr
        keys = {line.split("=", 1)[0] for line in out.read_text().splitlines()}
        assert {"stale_count", "warn_count", "deprecated_count", "today"} <= keys
