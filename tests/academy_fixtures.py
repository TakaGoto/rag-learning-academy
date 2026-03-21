"""Shared fixtures for academy infrastructure tests."""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CLAUDE_DIR = ROOT / ".claude"
AGENTS_DIR = CLAUDE_DIR / "agents"
SKILLS_DIR = CLAUDE_DIR / "skills"
CURRICULUM_DIR = CLAUDE_DIR / "docs" / "curriculum"
REFERENCE_DIR = CLAUDE_DIR / "docs" / "reference"
TEMPLATES_DIR = CLAUDE_DIR / "docs" / "templates"
RULES_DIR = CLAUDE_DIR / "rules"
HOOKS_DIR = CLAUDE_DIR / "hooks"
DATA_DIR = ROOT / "data" / "raw"

EXPECTED_AGENTS = [
    "architecture-director",
    "chunking-strategist",
    "curriculum-director",
    "deployment-specialist",
    "document-parser",
    "embedding-lead",
    "evaluation-lead",
    "evaluation-specialist",
    "graph-rag-specialist",
    "hybrid-search-specialist",
    "indexing-lead",
    "integration-lead",
    "metadata-specialist",
    "multimodal-specialist",
    "prompt-engineer",
    "query-analyst",
    "reranking-specialist",
    "research-director",
    "retrieval-lead",
    "vector-db-specialist",
]

EXPECTED_SKILLS = [
    "architecture",
    "audit-content",
    "benchmark",
    "build",
    "challenge",
    "code-review",
    "compare",
    "debug-rag",
    "evaluate",
    "explain",
    "glossary",
    "lesson",
    "paper-review",
    "quiz",
    "roadmap",
    "start",
    "triage",
]

EXPECTED_MODULES = [
    "module-01-foundations",
    "module-02-document-processing",
    "module-03-embeddings",
    "module-04-vector-databases",
    "module-05-retrieval",
    "module-06-generation",
    "module-07-evaluation",
    "module-08-advanced-patterns",
    "module-09-production",
]

# Skill pairs that must have scope disambiguation blockquotes
SCOPE_PAIRS = [
    ("glossary", "explain"),
    ("quiz", "lesson"),
    ("challenge", "build"),
    ("evaluate", "benchmark"),
]

VALID_REVIEW_CYCLES = {"monthly", "quarterly", "semi-annually"}
VALID_STALENESS_RISKS = {"high", "medium", "low"}


def parse_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter from markdown text. Returns empty dict if none."""
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    fm_block = text[3:end].strip()
    result = {}
    for line in fm_block.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            result[key.strip()] = value
    return result


@pytest.fixture
def settings():
    """Load .claude/settings.json."""
    path = CLAUDE_DIR / "settings.json"
    return json.loads(path.read_text())


@pytest.fixture
def claude_md():
    """Load CLAUDE.md content."""
    return (ROOT / "CLAUDE.md").read_text()


@pytest.fixture
def glossary_text():
    """Load glossary content."""
    return (REFERENCE_DIR / "glossary.md").read_text()


@pytest.fixture
def coordination_rules_text():
    """Load coordination rules content."""
    return (REFERENCE_DIR / "coordination-rules.md").read_text()


@pytest.fixture
def agent_roster_text():
    """Load agent roster content."""
    return (REFERENCE_DIR / "agent-roster.md").read_text()
