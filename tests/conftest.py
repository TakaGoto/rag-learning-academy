"""Pytest conftest — re-export fixtures from academy_fixtures."""

import sys
from pathlib import Path

# Make tests/ importable
sys.path.insert(0, str(Path(__file__).parent))

from academy_fixtures import *  # noqa: F401, F403, E402
