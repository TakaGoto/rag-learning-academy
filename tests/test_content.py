"""
Content quality tests — verify no deprecated patterns, valid code blocks,
and consistent formatting across all content files.
"""

import re

import pytest
from academy_fixtures import (
    AGENTS_DIR,
    CURRICULUM_DIR,
    DATA_DIR,
    EXPECTED_AGENTS,
    EXPECTED_SKILLS,
    REFERENCE_DIR,
    ROOT,
    RULES_DIR,
    SKILLS_DIR,
    TEMPLATES_DIR,
)

# Patterns that should not appear in content
DEPRECATED_MODEL_PATTERNS = [
    r"\bgpt-3\.5-turbo\b",
    r"\btext-embedding-ada-002\b",
    r"\bclaude-2\b(?![-\w])",  # claude-2 but not claude-2.1 etc
    r"\bclaude-instant\b",
]

# All markdown content directories to scan
CONTENT_DIRS = [CURRICULUM_DIR, REFERENCE_DIR, TEMPLATES_DIR, RULES_DIR]


def all_content_files():
    """Yield all markdown content files across the academy."""
    for d in CONTENT_DIRS:
        yield from d.glob("*.md")
    yield from DATA_DIR.glob("*.md")
    for agent in EXPECTED_AGENTS:
        yield AGENTS_DIR / f"{agent}.md"
    for skill in EXPECTED_SKILLS:
        path = SKILLS_DIR / skill / "SKILL.md"
        if path.exists():
            yield path


# ---------------------------------------------------------------------------
# Deprecated patterns
# ---------------------------------------------------------------------------


class TestDeprecatedPatterns:
    """Ensure no deprecated model IDs appear in content."""

    @pytest.mark.parametrize("path", list(all_content_files()), ids=lambda p: p.name)
    def test_no_deprecated_models(self, path):
        text = path.read_text()
        for pattern in DEPRECATED_MODEL_PATTERNS:
            matches = re.findall(pattern, text)
            # Allow matches inside deprecated-pattern lists (like check-references.sh docs)
            if (
                matches
                and "deprecated" not in text[max(0, text.find(matches[0]) - 200) : text.find(matches[0])].lower()
            ):
                assert not matches, f"{path.name} contains deprecated model reference: {matches[0]}"


# ---------------------------------------------------------------------------
# Python code block syntax
# ---------------------------------------------------------------------------


class TestCodeBlockSyntax:
    """Verify Python code blocks in content have valid syntax."""

    @pytest.mark.parametrize("path", list(all_content_files()), ids=lambda p: p.name)
    def test_python_blocks_parse(self, path):
        text = path.read_text()
        # Extract python code blocks
        blocks = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
        for i, block in enumerate(blocks):
            block = block.strip()
            if not block or block.startswith("#") and "\n" not in block:
                continue  # Skip comment-only blocks
            # Remove lines with ... (placeholder) and non-Python markers
            lines = []
            for line in block.split("\n"):
                stripped = line.strip()
                if stripped in ("...", "# Your implementation goes here", "pass"):
                    lines.append("    pass" if line.startswith(" ") else "pass")
                else:
                    lines.append(line)
            cleaned = "\n".join(lines)
            try:
                compile(cleaned, f"{path.name}:block{i}", "exec")
            except SyntaxError:
                # Some blocks are intentionally incomplete (showing patterns)
                # Only fail on blocks that look complete (have def/class/import)
                if any(cleaned.startswith(kw) for kw in ("def ", "class ", "import ", "from ")):
                    pytest.fail(f"{path.name} block {i}: Python syntax error in:\n{cleaned[:200]}")


# ---------------------------------------------------------------------------
# Consistent formatting
# ---------------------------------------------------------------------------


class TestFormattingConsistency:
    """Verify formatting conventions are followed."""

    @pytest.mark.parametrize("skill", EXPECTED_SKILLS)
    def test_skill_heading_format(self, skill):
        """All skill H1 headings should match '# Name: Descriptor' pattern."""
        text = (SKILLS_DIR / skill / "SKILL.md").read_text()
        h1_match = re.search(r"^# (.+)$", text, re.MULTILINE)
        assert h1_match, f"{skill}: no H1 heading found"
        heading = h1_match.group(1)
        assert ":" in heading, f"{skill}: H1 '{heading}' missing colon separator"

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_has_delegation_subsections(self, agent):
        """Agent delegation sections should have Delegate/Escalate/Accept."""
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        delegation_idx = text.find("## Delegation Rules")
        if delegation_idx == -1:
            pytest.fail(f"{agent}: missing Delegation Rules section")
        delegation_text = text[delegation_idx:]
        has_delegate = "Delegate" in delegation_text or "delegate" in delegation_text
        has_escalate = "Escalate" in delegation_text or "escalate" in delegation_text
        assert has_delegate, f"{agent}: Delegation Rules missing delegate guidance"
        assert has_escalate, f"{agent}: Delegation Rules missing escalation guidance"


# ---------------------------------------------------------------------------
# Settings.json validity
# ---------------------------------------------------------------------------


class TestSettingsJson:
    """Verify settings.json has valid structure."""

    def test_has_permissions(self, settings):
        assert "permissions" in settings
        assert "allow" in settings["permissions"]
        assert "deny" in settings["permissions"]

    def test_has_hooks(self, settings):
        assert "hooks" in settings

    def test_hooks_have_valid_structure(self, settings):
        hooks = settings["hooks"]
        for lifecycle_event, entries in hooks.items():
            assert isinstance(entries, list), f"{lifecycle_event}: hooks must be a list"
            for entry in entries:
                assert "matcher" in entry, f"{lifecycle_event}: entry missing 'matcher'"
                assert "hooks" in entry, f"{lifecycle_event}: entry missing 'hooks'"
                assert isinstance(entry["hooks"], list), f"{lifecycle_event}: hooks must be array"
                for hook in entry["hooks"]:
                    assert "type" in hook, f"{lifecycle_event}: hook missing 'type'"
                    assert "command" in hook, f"{lifecycle_event}: hook missing 'command'"

    def test_hook_commands_reference_existing_files(self, settings):
        hooks = settings["hooks"]
        for lifecycle_event, entries in hooks.items():
            for entry in entries:
                for hook in entry["hooks"]:
                    cmd = hook["command"]
                    # Check if the command references a file path
                    if cmd.startswith(".claude/hooks/"):
                        path = ROOT / cmd
                        assert path.exists(), f"{lifecycle_event}: hook command '{cmd}' references missing file"

    def test_no_env_files_in_allow(self, settings):
        """Ensure .env files are never whitelisted."""
        for perm in settings["permissions"]["allow"]:
            assert ".env" not in perm, f"Security: .env access should not be in allow list: {perm}"


# ---------------------------------------------------------------------------
# GitHub Actions workflow
# ---------------------------------------------------------------------------


class TestGitHubActions:
    """Verify GitHub Actions workflow is valid."""

    def test_workflow_exists(self):
        path = ROOT / ".github" / "workflows" / "content-freshness.yml"
        assert path.exists(), "Missing GitHub Actions workflow"

    def test_workflow_is_valid_yaml(self):
        import yaml

        path = ROOT / ".github" / "workflows" / "content-freshness.yml"
        try:
            with open(path) as f:
                data = yaml.safe_load(f)
            assert "on" in data or True in data, "Workflow missing trigger"
            assert "jobs" in data, "Workflow missing jobs"
        except ImportError:
            pytest.skip("PyYAML not installed")
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML in workflow: {e}")
