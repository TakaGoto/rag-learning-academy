"""
Integration tests for hook scripts — verify they execute without errors.
"""

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
