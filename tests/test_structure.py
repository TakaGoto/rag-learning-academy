"""
Structural integrity tests — verify all files exist, frontmatter is valid,
and required sections are present.
"""

import re

import pytest
from academy_fixtures import (
    AGENTS_DIR,
    CLAUDE_DIR,
    CURRICULUM_DIR,
    EXPECTED_AGENTS,
    EXPECTED_MODULES,
    EXPECTED_SKILLS,
    HOOKS_DIR,
    REFERENCE_DIR,
    RULES_DIR,
    SKILLS_DIR,
    TEMPLATES_DIR,
    VALID_REVIEW_CYCLES,
    VALID_STALENESS_RISKS,
    parse_frontmatter,
)

# ---------------------------------------------------------------------------
# File existence
# ---------------------------------------------------------------------------


class TestFileExistence:
    """Verify all expected files exist on disk."""

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_file_exists(self, agent):
        path = AGENTS_DIR / f"{agent}.md"
        assert path.exists(), f"Agent file missing: {path}"

    @pytest.mark.parametrize("skill", EXPECTED_SKILLS)
    def test_skill_file_exists(self, skill):
        path = SKILLS_DIR / skill / "SKILL.md"
        assert path.exists(), f"Skill file missing: {path}"

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_file_exists(self, module):
        path = CURRICULUM_DIR / f"{module}.md"
        assert path.exists(), f"Module file missing: {path}"

    def test_settings_json_exists(self):
        assert (CLAUDE_DIR / "settings.json").exists()

    def test_claude_md_exists(self):
        assert (CLAUDE_DIR / ".." / "CLAUDE.md").resolve().exists()

    @pytest.mark.parametrize(
        "ref_doc",
        [
            "agent-roster.md",
            "glossary.md",
            "coordination-rules.md",
            "coding-standards.md",
            "quick-start.md",
            "token-usage.md",
            "voice-examples.md",
        ],
    )
    def test_reference_doc_exists(self, ref_doc):
        assert (REFERENCE_DIR / ref_doc).exists(), f"Reference doc missing: {ref_doc}"

    @pytest.mark.parametrize(
        "shared_file",
        ["LANGUAGE_AWARENESS.md", "AGENT_TEMPLATE.md"],
    )
    def test_shared_file_exists(self, shared_file):
        assert (CLAUDE_DIR / shared_file).exists(), f"Shared file missing: {shared_file}"

    @pytest.mark.parametrize(
        "template",
        ["project-brief-template.md", "evaluation-report-template.md", "rag-architecture-template.md"],
    )
    def test_template_exists(self, template):
        assert (TEMPLATES_DIR / template).exists(), f"Template missing: {template}"

    @pytest.mark.parametrize(
        "hook",
        ["check-freshness.sh", "check-references.sh", "session-start.sh", "session-stop.sh", "validate-code.sh"],
    )
    def test_hook_exists(self, hook):
        path = HOOKS_DIR / hook
        assert path.exists(), f"Hook script missing: {hook}"

    @pytest.mark.parametrize(
        "hook",
        ["check-freshness.sh", "check-references.sh", "session-start.sh", "session-stop.sh", "validate-code.sh"],
    )
    def test_hook_is_executable(self, hook):
        import os

        path = HOOKS_DIR / hook
        assert os.access(path, os.X_OK), f"Hook not executable: {hook}"


# ---------------------------------------------------------------------------
# Agent structure
# ---------------------------------------------------------------------------

REQUIRED_AGENT_SECTIONS = [
    "Role Overview",
    "Core Philosophy",
    "Key Responsibilities",
    "Teaching Approach",
    "Level Calibration",
    "Common Misconceptions",
    "When to Use This Agent",
    "Delegation Rules",
]

REQUIRED_AGENT_FRONTMATTER = ["name", "description", "tools", "model"]


class TestAgentStructure:
    """Verify agent files have required frontmatter and sections."""

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_has_required_frontmatter(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        fm = parse_frontmatter(text)
        for field in REQUIRED_AGENT_FRONTMATTER:
            assert field in fm, f"{agent}: missing frontmatter field '{field}'"

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_model_is_valid(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        fm = parse_frontmatter(text)
        assert fm.get("model") in ("opus", "sonnet", "haiku"), f"{agent}: invalid model '{fm.get('model')}'"

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_has_required_sections(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        for section in REQUIRED_AGENT_SECTIONS:
            assert f"## {section}" in text, f"{agent}: missing section '## {section}'"

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_has_h1_heading(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        assert re.search(r"^# .+", text, re.MULTILINE), f"{agent}: missing H1 heading"

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_references_shared_template(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        assert "AGENT_TEMPLATE.md" in text, f"{agent}: missing reference to AGENT_TEMPLATE.md"

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_agent_references_language_awareness(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        assert "LANGUAGE_AWARENESS" in text, f"{agent}: missing reference to LANGUAGE_AWARENESS.md"


# ---------------------------------------------------------------------------
# Skill structure
# ---------------------------------------------------------------------------

REQUIRED_SKILL_FRONTMATTER = ["name", "description"]


class TestSkillStructure:
    """Verify skill files have required frontmatter and standard elements."""

    @pytest.mark.parametrize("skill", EXPECTED_SKILLS)
    def test_skill_has_required_frontmatter(self, skill):
        text = (SKILLS_DIR / skill / "SKILL.md").read_text()
        fm = parse_frontmatter(text)
        for field in REQUIRED_SKILL_FRONTMATTER:
            assert field in fm, f"{skill}: missing frontmatter field '{field}'"

    @pytest.mark.parametrize("skill", EXPECTED_SKILLS)
    def test_skill_has_h1_heading(self, skill):
        text = (SKILLS_DIR / skill / "SKILL.md").read_text()
        # H1 should follow pattern "# Name: Descriptor"
        assert re.search(r"^# .+: .+", text, re.MULTILINE), (
            f"{skill}: H1 heading should follow '# Name: Descriptor' pattern"
        )

    @pytest.mark.parametrize("skill", EXPECTED_SKILLS)
    def test_skill_has_next_steps(self, skill):
        text = (SKILLS_DIR / skill / "SKILL.md").read_text()
        assert "next step" in text.lower() or "/lesson" in text or "/build" in text or "/roadmap" in text, (
            f"{skill}: missing next-steps guidance with slash commands"
        )


# ---------------------------------------------------------------------------
# Module structure
# ---------------------------------------------------------------------------


class TestModuleStructure:
    """Verify curriculum modules have required sections and formatting."""

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_has_frontmatter(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        fm = parse_frontmatter(text)
        assert "last_reviewed" in fm, f"{module}: missing last_reviewed frontmatter"

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_has_objectives(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        assert "## Module Objectives" in text, f"{module}: missing Module Objectives section"

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_has_prerequisites(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        assert "## Prerequisites" in text, f"{module}: missing Prerequisites section"

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_has_key_takeaways(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        assert "## Key Takeaways" in text, f"{module}: missing Key Takeaways section"

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_has_hands_on_exercises(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        assert "## Hands-On Exercises" in text, f"{module}: missing Hands-On Exercises section"

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_module_has_navigation_footer(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        # All modules should have at least one navigation link
        has_prev = "**Previous:**" in text
        has_next = "**Next:**" in text
        assert has_prev or has_next, f"{module}: missing navigation footer"

    def test_module_01_has_no_previous(self):
        text = (CURRICULUM_DIR / "module-01-foundations.md").read_text()
        assert "**Previous:**" not in text, "Module 01 should not have a Previous link"

    def test_module_09_has_no_next(self):
        text = (CURRICULUM_DIR / "module-09-production.md").read_text()
        assert "**Next:**" not in text, "Module 09 should not have a Next link"

    @pytest.mark.parametrize("module", EXPECTED_MODULES[1:])  # modules 02-09
    def test_modules_02_09_have_before_you_begin(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        assert "### Before You Begin" in text, f"{module}: missing 'Before You Begin' checkpoint"


# ---------------------------------------------------------------------------
# Frontmatter freshness metadata
# ---------------------------------------------------------------------------

# All content files that should have last_reviewed frontmatter
FRONTMATTER_FILES = (
    [CURRICULUM_DIR / f"{m}.md" for m in EXPECTED_MODULES]
    + [
        RULES_DIR / f
        for f in [
            "chunking-code.md",
            "embedding-code.md",
            "evaluation-code.md",
            "pipeline-code.md",
            "prompt-templates.md",
            "retrieval-code.md",
            "vector-db-code.md",
        ]
    ]
    + [
        REFERENCE_DIR / f
        for f in [
            "agent-roster.md",
            "coding-standards.md",
            "coordination-rules.md",
            "glossary.md",
            "quick-start.md",
        ]
    ]
    + [
        TEMPLATES_DIR / f
        for f in [
            "project-brief-template.md",
            "evaluation-report-template.md",
            "rag-architecture-template.md",
        ]
    ]
)


class TestFreshnessFrontmatter:
    """Verify all content files have valid freshness tracking metadata."""

    @pytest.mark.parametrize("path", FRONTMATTER_FILES, ids=lambda p: p.name)
    def test_has_last_reviewed(self, path):
        fm = parse_frontmatter(path.read_text())
        assert "last_reviewed" in fm, f"{path.name}: missing last_reviewed"

    @pytest.mark.parametrize("path", FRONTMATTER_FILES, ids=lambda p: p.name)
    def test_has_valid_review_cycle(self, path):
        fm = parse_frontmatter(path.read_text())
        cycle = fm.get("review_cycle", "")
        assert cycle in VALID_REVIEW_CYCLES, f"{path.name}: review_cycle '{cycle}' not in {VALID_REVIEW_CYCLES}"

    @pytest.mark.parametrize("path", FRONTMATTER_FILES, ids=lambda p: p.name)
    def test_has_valid_staleness_risk(self, path):
        fm = parse_frontmatter(path.read_text())
        risk = fm.get("staleness_risk", "")
        assert risk in VALID_STALENESS_RISKS, f"{path.name}: staleness_risk '{risk}' not in {VALID_STALENESS_RISKS}"

    @pytest.mark.parametrize("path", FRONTMATTER_FILES, ids=lambda p: p.name)
    def test_last_reviewed_is_valid_date(self, path):
        fm = parse_frontmatter(path.read_text())
        date_str = fm.get("last_reviewed", "")
        assert re.match(r"\d{4}-\d{2}-\d{2}", date_str), (
            f"{path.name}: last_reviewed '{date_str}' is not a valid YYYY-MM-DD date"
        )
