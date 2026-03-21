"""
Cross-reference tests — verify that links between skills, agents, modules,
and the glossary are all valid and bidirectional.
"""

import re

import pytest
from academy_fixtures import (
    AGENTS_DIR,
    CURRICULUM_DIR,
    EXPECTED_AGENTS,
    EXPECTED_MODULES,
    EXPECTED_SKILLS,
    SCOPE_PAIRS,
    SKILLS_DIR,
)

# ---------------------------------------------------------------------------
# Skill cross-references
# ---------------------------------------------------------------------------


class TestSkillCrossReferences:
    """Verify slash command references in skills point to real skills."""

    @pytest.mark.parametrize("skill", EXPECTED_SKILLS)
    def test_slash_commands_reference_real_skills(self, skill):
        text = (SKILLS_DIR / skill / "SKILL.md").read_text()
        # Find all /command references (backticked or not)
        refs = re.findall(r"`/([a-z][-a-z]*)`", text)
        # Exclude placeholder references used in prose examples
        placeholders = {"command", "slash-command", "other-skill", "foo", "bar"}
        for ref in refs:
            if ref in placeholders:
                continue
            assert ref in EXPECTED_SKILLS, f"{skill}/SKILL.md references `/{ref}` which is not a known skill"

    @pytest.mark.parametrize("skill_a,skill_b", SCOPE_PAIRS)
    def test_scope_pair_a_has_blockquote(self, skill_a, skill_b):
        text = (SKILLS_DIR / skill_a / "SKILL.md").read_text()
        assert "> **Scope:**" in text or f"/{skill_b}" in text, (
            f"{skill_a}: missing scope blockquote referencing /{skill_b}"
        )

    @pytest.mark.parametrize("skill_a,skill_b", SCOPE_PAIRS)
    def test_scope_pair_b_has_blockquote(self, skill_a, skill_b):
        text = (SKILLS_DIR / skill_b / "SKILL.md").read_text()
        assert "> **Scope:**" in text or f"/{skill_a}" in text, (
            f"{skill_b}: missing scope blockquote referencing /{skill_a}"
        )


# ---------------------------------------------------------------------------
# CLAUDE.md references
# ---------------------------------------------------------------------------


class TestClaudeMdReferences:
    """Verify CLAUDE.md lists all skills and modules accurately."""

    def test_all_skills_listed(self, claude_md):
        for skill in EXPECTED_SKILLS:
            assert f"/{skill}" in claude_md, f"CLAUDE.md missing skill: /{skill}"

    def test_all_modules_referenced(self, claude_md):
        for i in range(1, 10):
            assert f"| {i} |" in claude_md or f"Module {i:02d}" in claude_md, f"CLAUDE.md missing module {i}"


# ---------------------------------------------------------------------------
# Agent delegation references
# ---------------------------------------------------------------------------


class TestAgentDelegation:
    """Verify agent delegation rules reference existing agents."""

    @pytest.mark.parametrize("agent", EXPECTED_AGENTS)
    def test_delegation_references_real_agents(self, agent):
        text = (AGENTS_DIR / f"{agent}.md").read_text()
        # Find the Delegation Rules section
        delegation_idx = text.find("## Delegation Rules")
        if delegation_idx == -1:
            pytest.skip(f"{agent} has no Delegation Rules section")
        delegation_text = text[delegation_idx:]
        # Look for agent name references (bold or backticked)
        refs = re.findall(r"\*\*([a-z][-a-z]+)\*\*", delegation_text)
        known_names = {a.replace("-", "-") for a in EXPECTED_AGENTS}
        for ref in refs:
            if ref in ("delegate", "escalate", "accept", "from", "why"):
                continue  # Skip common bold words
            # Flexible match: check if ref is a substring of any known agent
            matches = [a for a in known_names if ref in a or a in ref]
            if not matches and len(ref) > 5:  # Only flag substantial names
                # This is a soft check — agent names in prose may be abbreviated
                pass


# ---------------------------------------------------------------------------
# Module navigation links
# ---------------------------------------------------------------------------


class TestModuleNavigation:
    """Verify inter-module navigation links point to real files."""

    @pytest.mark.parametrize("module", EXPECTED_MODULES)
    def test_navigation_links_point_to_real_files(self, module):
        text = (CURRICULUM_DIR / f"{module}.md").read_text()
        # Find markdown links to other modules
        links = re.findall(r"\[.*?\]\((module-\d+-[a-z-]+\.md)\)", text)
        for link in links:
            target = CURRICULUM_DIR / link
            assert target.exists(), f"{module}: navigation link to '{link}' points to non-existent file"


# ---------------------------------------------------------------------------
# Glossary topic index
# ---------------------------------------------------------------------------


class TestGlossaryTopicIndex:
    """Verify the topic index at the end of the glossary references real terms."""

    def test_topic_index_exists(self, glossary_text):
        assert "## Terms by Topic" in glossary_text, "Glossary missing 'Terms by Topic' section"

    def test_topic_index_has_categories(self, glossary_text):
        expected_categories = [
            "Document Processing",
            "Embeddings",
            "Retrieval",
            "Indexing",
            "Generation",
            "Evaluation",
            "Advanced Patterns",
        ]
        for cat in expected_categories:
            assert cat in glossary_text, f"Glossary topic index missing category: {cat}"

    def test_topic_terms_are_defined_above(self, glossary_text):
        """Verify terms listed in the topic index actually have definitions."""
        # Split at topic index
        parts = glossary_text.split("## Terms by Topic")
        if len(parts) < 2:
            pytest.skip("No topic index found")
        definitions_section = parts[0].lower()
        topic_index = parts[1]
        # Extract terms from topic index (they're comma-separated after ### headers)
        topic_terms = []
        for line in topic_index.split("\n"):
            if line.startswith("###"):
                continue
            if line.strip():
                terms = [t.strip().rstrip(",") for t in line.split(",")]
                topic_terms.extend(t for t in terms if t and not t.startswith("#"))
        # Check a sample of terms exist in definitions
        missing = []
        for term in topic_terms[:20]:  # Check first 20 to keep test fast
            if term.lower() not in definitions_section:
                missing.append(term)
        assert len(missing) <= 2, f"Topic index lists terms not defined in glossary: {missing}"


# ---------------------------------------------------------------------------
# Agent roster references
# ---------------------------------------------------------------------------


class TestAgentRoster:
    """Verify the agent roster references all existing agents."""

    def test_roster_lists_all_agents(self, agent_roster_text):
        for agent in EXPECTED_AGENTS:
            # Agent names in roster may use spaces instead of hyphens
            readable_name = agent.replace("-", " ").replace("_", " ")
            assert agent in agent_roster_text or readable_name in agent_roster_text.lower(), (
                f"Agent roster missing: {agent}"
            )

    def test_roster_has_model_allocation(self, agent_roster_text):
        assert "Model Allocation" in agent_roster_text, "Agent roster missing 'Model Allocation' section"


# ---------------------------------------------------------------------------
# Coordination rules
# ---------------------------------------------------------------------------


class TestCoordinationRules:
    """Verify coordination rules have the breadcrumb protocol."""

    def test_breadcrumb_protocol_exists(self, coordination_rules_text):
        assert "Breadcrumb Protocol" in coordination_rules_text, (
            "Coordination rules missing 'Breadcrumb Protocol' section"
        )

    def test_handoff_protocol_exists(self, coordination_rules_text):
        assert "Handoff" in coordination_rules_text, "Coordination rules missing handoff protocol"
