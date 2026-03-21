#!/usr/bin/env python3
"""
Weekly Knowledge Check — detection-only CI script.

Checks for:
1. PyPI version drift on key dependencies
2. Deprecated model/pattern references in content
3. Content files past their review cycle
4. MTEB leaderboard changes (top embedding models)

Outputs a structured Markdown report to stdout.
Never modifies any files — detection only.
"""

import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent.parent
ACTION_ITEMS = []


def log_action(category: str, severity: str, message: str):
    """Track an action item for the final report."""
    ACTION_ITEMS.append({"category": category, "severity": severity, "message": message})


# ---------------------------------------------------------------------------
# 1. PyPI version checks
# ---------------------------------------------------------------------------

# Packages we track, with the version referenced in requirements.txt
TRACKED_PACKAGES = {
    "anthropic": "0.40.0",
    "openai": "1.50.0",
    "chromadb": "0.5.0",
    "langchain": "0.3.0",
    "langchain-community": "0.3.0",
    "ragas": "0.2.0",
    "sentence-transformers": "3.0.0",
}


def get_pypi_latest(package: str) -> str | None:
    """Fetch the latest version of a package from PyPI."""
    try:
        req = Request(
            f"https://pypi.org/pypi/{package}/json",
            headers={"User-Agent": "rag-learning-academy-ci/1.0"},
        )
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data["info"]["version"]
    except (URLError, json.JSONDecodeError, KeyError):
        return None


def check_pypi_versions():
    """Compare referenced versions against PyPI latest."""
    results = []
    for package, our_version in TRACKED_PACKAGES.items():
        latest = get_pypi_latest(package)
        if latest is None:
            continue
        # Parse major versions
        our_major = our_version.split(".")[0]
        latest_major = latest.split(".")[0]
        our_minor = our_version.split(".")[1] if "." in our_version else "0"
        latest_minor = latest.split(".")[1] if "." in latest else "0"

        if our_major != latest_major:
            severity = "critical"
            log_action(
                "PyPI",
                severity,
                f"`{package}`: major version bump {our_version} → **{latest}** (breaking changes likely)",
            )
        elif int(latest_minor) - int(our_minor) >= 3:
            severity = "warning"
            log_action(
                "PyPI",
                severity,
                f"`{package}`: significant update {our_version} → **{latest}** (review changelog)",
            )

        results.append(
            {
                "package": package,
                "ours": our_version,
                "latest": latest,
                "major_drift": our_major != latest_major,
            }
        )
    return results


# ---------------------------------------------------------------------------
# 2. Deprecated pattern scan
# ---------------------------------------------------------------------------

DEPRECATED_PATTERNS = {
    r"\bgpt-3\.5-turbo\b": "gpt-3.5-turbo (use gpt-4o-mini or newer)",
    r"\btext-embedding-ada-002\b": "text-embedding-ada-002 (use text-embedding-3-small or newer)",
    r"\bclaude-2\b(?![-.\w])": "claude-2 (use claude-sonnet-4-6 or newer)",
    r"\bclaude-instant\b": "claude-instant (use claude-haiku-4-5 or newer)",
    r"\bfrom langchain import\b": "old-style langchain import (use langchain-core or langchain-community)",
}

SCAN_DIRS = [
    ROOT / ".claude" / "docs",
    ROOT / ".claude" / "agents",
    ROOT / ".claude" / "rules",
    ROOT / ".claude" / "skills",
    ROOT / "src",
    ROOT / "data",
]


def scan_deprecated_patterns():
    """Scan content files for deprecated patterns."""
    hits = []
    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for md_file in scan_dir.rglob("*.md"):
            text = md_file.read_text()
            for pattern, description in DEPRECATED_PATTERNS.items():
                matches = re.findall(pattern, text)
                if matches:
                    rel_path = md_file.relative_to(ROOT)
                    hits.append({"file": str(rel_path), "pattern": description, "count": len(matches)})
    for py_file in (ROOT / "src").rglob("*.py") if (ROOT / "src").exists() else []:
        text = py_file.read_text()
        for pattern, description in DEPRECATED_PATTERNS.items():
            matches = re.findall(pattern, text)
            if matches:
                rel_path = py_file.relative_to(ROOT)
                hits.append({"file": str(rel_path), "pattern": description, "count": len(matches)})

    if hits:
        for hit in hits:
            log_action(
                "Deprecated",
                "warning",
                f"`{hit['file']}`: {hit['pattern']} ({hit['count']} occurrence{'s' if hit['count'] > 1 else ''})",
            )
    return hits


# ---------------------------------------------------------------------------
# 3. Review cycle checks
# ---------------------------------------------------------------------------

REVIEW_CYCLE_DAYS = {
    "monthly": 30,
    "quarterly": 90,
    "semi-annually": 180,
}


def parse_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter from markdown."""
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    result = {}
    for line in text[3:end].strip().split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip().strip("'\"")
    return result


def check_review_cycles():
    """Check which files are past their review cycle."""
    overdue = []
    content_dirs = [
        ROOT / ".claude" / "docs" / "curriculum",
        ROOT / ".claude" / "docs" / "reference",
        ROOT / ".claude" / "docs" / "templates",
        ROOT / ".claude" / "rules",
        ROOT / ".claude" / "agents",
        ROOT / "data" / "raw",
    ]

    today = datetime.now()

    for content_dir in content_dirs:
        if not content_dir.exists():
            continue
        for md_file in content_dir.glob("*.md"):
            text = md_file.read_text()
            fm = parse_frontmatter(text)
            last_reviewed = fm.get("last_reviewed", "")
            review_cycle = fm.get("review_cycle", "")
            staleness_risk = fm.get("staleness_risk", "")

            if not last_reviewed or not review_cycle:
                continue

            try:
                reviewed_date = datetime.strptime(last_reviewed, "%Y-%m-%d")
            except ValueError:
                continue

            max_days = REVIEW_CYCLE_DAYS.get(review_cycle, 90)
            age_days = (today - reviewed_date).days

            if age_days > max_days:
                rel_path = md_file.relative_to(ROOT)
                overdue_by = age_days - max_days
                severity = "critical" if staleness_risk == "high" else "warning"
                log_action(
                    "Review Cycle",
                    severity,
                    f"`{rel_path}`: {overdue_by} days overdue for {review_cycle} review "
                    f"(last reviewed: {last_reviewed}, risk: {staleness_risk})",
                )
                overdue.append(
                    {
                        "file": str(rel_path),
                        "last_reviewed": last_reviewed,
                        "cycle": review_cycle,
                        "risk": staleness_risk,
                        "overdue_by": overdue_by,
                    }
                )

    return overdue


# ---------------------------------------------------------------------------
# 4. MTEB leaderboard check
# ---------------------------------------------------------------------------

# Models we currently recommend in the curriculum
RECOMMENDED_MODELS = [
    "text-embedding-3-small",
    "all-MiniLM-L6-v2",
    "nomic-embed-text",
    "bge-base-en-v1.5",
]


def check_mteb_leaderboard():
    """Check if our recommended models are still competitive on MTEB.

    Uses the Hugging Face API to check model download trends as a proxy
    for continued community adoption. Direct MTEB scraping is fragile,
    so we check if models are still actively downloaded.
    """
    results = []
    for model in RECOMMENDED_MODELS:
        try:
            # Map common names to HF model IDs
            hf_model = {
                "text-embedding-3-small": None,  # OpenAI, not on HF
                "all-MiniLM-L6-v2": "sentence-transformers/all-MiniLM-L6-v2",
                "nomic-embed-text": "nomic-ai/nomic-embed-text-v1.5",
                "bge-base-en-v1.5": "BAAI/bge-base-en-v1.5",
            }.get(model)

            if hf_model is None:
                continue

            req = Request(
                f"https://huggingface.co/api/models/{hf_model}",
                headers={"User-Agent": "rag-learning-academy-ci/1.0"},
            )
            with urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                downloads = data.get("downloads", 0)
                last_modified = data.get("lastModified", "unknown")

                # Flag models with very low downloads (possibly abandoned)
                if downloads < 1000:
                    log_action(
                        "MTEB",
                        "warning",
                        f"`{model}` ({hf_model}): low download count ({downloads:,}) — may be superseded",
                    )

                results.append(
                    {
                        "model": model,
                        "hf_id": hf_model,
                        "downloads": downloads,
                        "last_modified": last_modified,
                    }
                )
        except (URLError, json.JSONDecodeError, KeyError):
            continue

    return results


# ---------------------------------------------------------------------------
# 5. Content age check (git-based)
# ---------------------------------------------------------------------------


def check_content_ages():
    """Check file ages via git log, flag files not updated in 90+ days."""
    stale = []
    now = datetime.now()

    content_globs = [
        ".claude/docs/curriculum/*.md",
        ".claude/agents/*.md",
        ".claude/docs/reference/*.md",
        ".claude/rules/*.md",
        "data/raw/*.md",
    ]

    for glob_pattern in content_globs:
        import glob

        for filepath in glob.glob(str(ROOT / glob_pattern)):
            try:
                result = subprocess.run(
                    ["git", "log", "-1", "--format=%ct", "--", filepath],
                    capture_output=True,
                    text=True,
                    cwd=str(ROOT),
                    timeout=10,
                )
                if result.returncode != 0 or not result.stdout.strip():
                    continue
                last_commit_ts = int(result.stdout.strip())
                last_commit_date = datetime.fromtimestamp(last_commit_ts)
                age_days = (now - last_commit_date).days

                if age_days > 90:
                    rel_path = Path(filepath).relative_to(ROOT)
                    stale.append(
                        {
                            "file": str(rel_path),
                            "days": age_days,
                            "date": last_commit_date.strftime("%Y-%m-%d"),
                        }
                    )
                    log_action(
                        "File Age",
                        "warning",
                        f"`{rel_path}`: {age_days} days since last update ({last_commit_date.strftime('%Y-%m-%d')})",
                    )
            except (subprocess.TimeoutExpired, ValueError):
                continue

    return stale


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def generate_report(pypi_results, deprecated_hits, overdue_files, mteb_results, stale_files):
    """Generate the final Markdown report."""
    today = datetime.now().strftime("%Y-%m-%d")
    critical_count = sum(1 for a in ACTION_ITEMS if a["severity"] == "critical")
    warning_count = sum(1 for a in ACTION_ITEMS if a["severity"] == "warning")

    lines = [
        f"## Weekly Knowledge Check — {today}",
        "",
        f"**{len(ACTION_ITEMS)} items found** ({critical_count} critical, {warning_count} warnings)",
        "",
    ]

    # Critical items first
    critical_items = [a for a in ACTION_ITEMS if a["severity"] == "critical"]
    if critical_items:
        lines.append("### Critical (action needed)")
        lines.append("")
        for item in critical_items:
            lines.append(f"- [ ] **[{item['category']}]** {item['message']}")
        lines.append("")

    # Warnings
    warning_items = [a for a in ACTION_ITEMS if a["severity"] == "warning"]
    if warning_items:
        lines.append("### Warnings (review recommended)")
        lines.append("")
        for item in warning_items:
            lines.append(f"- [ ] **[{item['category']}]** {item['message']}")
        lines.append("")

    # PyPI version summary table
    if pypi_results:
        lines.append("### Dependency Versions")
        lines.append("")
        lines.append("| Package | Our Min Version | Latest | Status |")
        lines.append("|---------|----------------|--------|--------|")
        for r in pypi_results:
            status = "Major drift" if r["major_drift"] else "OK"
            if r["ours"] == r["latest"]:
                status = "Current"
            lines.append(f"| `{r['package']}` | {r['ours']} | {r['latest']} | {status} |")
        lines.append("")

    # MTEB model health
    if mteb_results:
        lines.append("### Recommended Model Health")
        lines.append("")
        lines.append("| Model | HF Downloads | Status |")
        lines.append("|-------|-------------|--------|")
        for r in mteb_results:
            status = "Low downloads" if r["downloads"] < 1000 else "Active"
            lines.append(f"| `{r['model']}` | {r['downloads']:,} | {status} |")
        lines.append("")

    # No issues
    if not ACTION_ITEMS:
        lines.append("All checks passed — no action items this week.")
        lines.append("")

    lines.append("---")
    lines.append("*Generated by [Weekly Knowledge Check](.github/workflows/weekly-knowledge-check.yml). ")
    lines.append("Run `/audit-content` in Claude Code for a deeper review.*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    pypi_results = check_pypi_versions()
    deprecated_hits = scan_deprecated_patterns()
    overdue_files = check_review_cycles()
    mteb_results = check_mteb_leaderboard()
    stale_files = check_content_ages()

    report = generate_report(pypi_results, deprecated_hits, overdue_files, mteb_results, stale_files)
    print(report)

    # Exit with error if critical items found (makes CI status red)
    critical_count = sum(1 for a in ACTION_ITEMS if a["severity"] == "critical")
    sys.exit(1 if critical_count > 0 else 0)


if __name__ == "__main__":
    main()
