.PHONY: install test lint format shellcheck ci clean knowledge-check dashboard

install:
	pip install -r requirements.txt
	pip install ruff pytest pyyaml

test:
	python -m pytest tests/test_structure.py tests/test_cross_references.py tests/test_content.py tests/test_hooks.py -v

test-all:
	python -m pytest tests/ -v

lint:
	ruff check tests/ src/
	ruff format --check tests/ src/

format:
	ruff format tests/ src/
	ruff check --fix tests/ src/

shellcheck:
	shellcheck .claude/hooks/*.sh

knowledge-check:
	python3 .github/scripts/weekly_knowledge_check.py

dashboard:
	python3 scripts/generate_dashboard.py

audit:
	@echo "Run /audit-content in Claude Code to check for stale content"

ci: lint shellcheck test

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
