# Makefile for Product Delivery Pipeline

.PHONY: help test lint format build docker-run clean docker-test docker-dev install-deps
.PHONY: install-dev-deps pre-commit-install pre-commit-run quality-check security-check
.PHONY: complexity-check type-check coverage-report docs-build restructure restructure-dry-run

help:
	@echo "Available targets:"
	@echo "  install-deps      Install Python dependencies"
	@echo "  install-dev-deps  Install development dependencies"
	@echo "  pre-commit-install Install pre-commit hooks"
	@echo "  pre-commit-run    Run pre-commit hooks on all files"
	@echo "  test              Run all tests"
	@echo "  test-cov          Run tests with coverage"
	@echo "  lint              Run flake8 linter"
	@echo "  format            Run black code formatter"
	@echo "  format-check      Check if code is formatted"
	@echo "  type-check        Run mypy type checking"
	@echo "  security-check    Run bandit security scanner"
	@echo "  complexity-check  Run radon complexity analysis"
	@echo "  quality-check     Run all quality checks"
	@echo "  build             Build Docker image"
	@echo "  docker-run        Run pipeline in Docker"
	@echo "  docker-test       Run tests in Docker"
	@echo "  docker-dev        Run development environment in Docker"
	@echo "  clean             Remove Python cache and build artifacts"
	@echo "  docs-build        Build documentation"
	@echo "  restructure       Restructure project to follow Python packaging best practices"
	@echo "  restructure-dry-run Show what restructure would do without making changes"

install-deps:
	pip install -r requirements.txt

install-dev-deps:
	pip install -r requirements-dev.txt

pre-commit-install:
	pre-commit install
	pre-commit install --hook-type commit-msg

pre-commit-run:
	pre-commit run --all-files

test:
	python3 -m pytest unit_test_PyTest/

test-cov:
	python3 -m pytest unit_test_PyTest/ --cov=. --cov-report=html --cov-report=term

lint:
	flake8 .

format:
	black .

format-check:
	black --check .

type-check:
	mypy .

security-check:
	bandit -r . -f json -o bandit-report.json
	@echo "Security scan completed. Check bandit-report.json for details."

complexity-check:
	radon cc . -a
	radon mi . -a

quality-check: format-check lint type-check security-check complexity-check
	@echo "All quality checks completed!"

build:
	docker build -t product-pipeline .

docker-run:
	docker run --rm -v $(PWD):/app -w /app product-pipeline python product_pipeline.py --help

docker-test:
	docker run --rm -v $(PWD):/app -w /app product-pipeline python -m pytest unit_test_PyTest/

docker-dev:
	docker-compose up dev

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache *.pyc *.pyo *.pyd *.log
	rm -rf .coverage htmlcov bandit-report.json
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Docker Compose shortcuts
compose-up:
	docker-compose up

compose-down:
	docker-compose down

compose-build:
	docker-compose build

# Development helpers
check-deps:
	python3 -c "import yaml; print('✓ PyYAML available')"
	python3 -c "from utils_py.config_loader import load_yaml_file; print('✓ Config loader available')"

run-example:
	python3 product_pipeline.py --repo_name ProductA

# Documentation
docs-build:
	cd docs && make html

# CI/CD helpers
ci-check: quality-check test-cov
	@echo "CI checks completed successfully!"

# Project restructuring
restructure:
	@echo "Restructuring project to follow Python packaging best practices..."
	@echo "This will move files and update imports. Make sure you have a backup!"
	@read -p "Are you sure you want to continue? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		python3 scripts/restructure_project.py; \
	else \
		echo "Restructure cancelled."; \
	fi

restructure-dry-run:
	@echo "Showing what restructure would do (dry run)..."
	python3 scripts/restructure_project.py --dry-run 