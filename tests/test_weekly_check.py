"""
Weekly knowledge check — the script reports findings; it must not turn them into a red run.
"""

import importlib.util
import sys

import pytest
from academy_fixtures import ROOT

SCRIPT = ROOT / ".github" / "scripts" / "weekly_knowledge_check.py"


@pytest.fixture
def weekly():
    spec = importlib.util.spec_from_file_location("weekly_knowledge_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.ACTION_ITEMS.clear()
    yield module
    module.ACTION_ITEMS.clear()
    sys.modules.pop(spec.name, None)


def stub_checks(weekly, monkeypatch, latest):
    """Skip the network checks; PyPI answers come from `latest`."""
    monkeypatch.setattr(weekly, "get_pypi_latest", lambda package: latest.get(package))
    monkeypatch.setattr(weekly, "check_mteb_leaderboard", lambda: [])


class TestWeeklyExitCode:
    def test_critical_findings_do_not_fail_the_run(self, weekly, monkeypatch, capsys):
        """Regression: a critical item used to sys.exit(1), failing every weekly run since March."""
        stub_checks(weekly, monkeypatch, {"anthropic": "99.0.0"})  # a major version ahead of our floor
        assert weekly.main() == 0
        out = capsys.readouterr().out
        assert "major version bump" in out, "the critical item must still appear in the report"
        assert any(a["severity"] == "critical" for a in weekly.ACTION_ITEMS)

    def test_script_entrypoint_exits_zero(self):
        text = SCRIPT.read_text()
        assert "sys.exit(main())" in text
        assert "sys.exit(1" not in text


class TestPypiNoise:
    def test_minor_lag_is_not_reported(self, weekly, monkeypatch):
        """Requirements are minimums, so being several minors behind is normal."""
        ours = weekly.TRACKED_PACKAGES["chromadb"].split(".")
        latest = f"{ours[0]}.{int(ours[1]) + 10}.0"
        stub_checks(weekly, monkeypatch, {"chromadb": latest})
        weekly.check_pypi_versions()
        assert not [a for a in weekly.ACTION_ITEMS if a["category"] == "PyPI"]


class TestDeprecatedScan:
    def test_audit_skill_is_exempt(self, weekly):
        """audit-content/SKILL.md quotes `from langchain import` as an example of what to look for."""
        hits = weekly.scan_deprecated_patterns()
        assert not [h for h in hits if "audit-content" in h["file"]], hits
