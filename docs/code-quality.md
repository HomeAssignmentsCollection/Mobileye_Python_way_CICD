# Code Quality Tools and Static Analysis

This document describes the code quality tools and static analysis setup for the Product Delivery Pipeline project.

## Overview

The project uses a comprehensive set of tools to ensure code quality, security, and maintainability:

## Tools Overview

### 1. **Code Formatting**
- **Black**: Automatic code formatter
- **isort**: Import sorting
- **autopep8**: PEP 8 compliance

### 2. **Linting**
- **flake8**: Style guide enforcement
- **pylint**: Advanced static analysis
- **yamllint**: YAML file validation

### 3. **Type Checking**
- **mypy**: Static type checking
- **types-PyYAML**: Type stubs for PyYAML

### 4. **Security**
- **bandit**: Security vulnerability scanner
- **safety**: Dependency vulnerability checker

### 5. **Code Complexity**
- **radon**: Cyclomatic complexity analysis
- **mccabe**: McCabe complexity checker

### 6. **Testing**
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **pytest-mock**: Mocking utilities

### 7. **Pre-commit Hooks**
- **pre-commit**: Git hooks for code quality
- **commitizen**: Commit message formatting

## Installation

### Install Development Dependencies
```bash
make install-dev-deps
```

### Install Pre-commit Hooks
```bash
make pre-commit-install
```

## Usage

### Run All Quality Checks
```bash
make quality-check
```

### Individual Tools

#### Code Formatting
```bash
# Format code
make format

# Check formatting
make format-check
```

#### Linting
```bash
# Run flake8
make lint

# Run pylint
pylint pipelines/ notifications/ repositories/ utils_py/
```

#### Type Checking
```bash
make type-check
```

#### Security Scanning
```bash
make security-check
```

#### Complexity Analysis
```bash
make complexity-check
```

#### Testing with Coverage
```bash
make test-cov
```

## Configuration Files

### pyproject.toml
Central configuration for most tools:
- Black formatting settings
- isort import sorting
- flake8 linting rules
- mypy type checking
- pytest configuration
- Coverage settings

### .pre-commit-config.yaml
Pre-commit hooks configuration:
- Code formatting hooks
- Linting hooks
- Security scanning
- File validation

### .yamllint
YAML file validation rules

### pylintrc
Pylint configuration

## Pre-commit Hooks

Pre-commit hooks automatically run quality checks before each commit:

1. **Code Formatting**: Black and isort
2. **Linting**: flake8 and pylint
3. **Type Checking**: mypy
4. **Security**: bandit
5. **File Validation**: YAML, JSON, etc.
6. **Commit Message**: commitizen formatting

### Manual Pre-commit Run
```bash
make pre-commit-run
```

## CI/CD Integration

The GitHub Actions workflow includes:

1. **Quality Checks Job**:
   - Pre-commit hooks
   - Code formatting check
   - Linting
   - Type checking
   - Security scanning
   - Complexity analysis
   - YAML linting

2. **Testing Job**:
   - Unit tests with coverage
   - Coverage reporting

3. **Docker Job**:
   - Docker image build
   - Docker image testing

## Best Practices

### 1. **Before Committing**
```bash
# Run all quality checks
make quality-check

# Run tests
make test

# Install pre-commit hooks (one-time setup)
make pre-commit-install
```

### 2. **Code Style**
- Use Black for formatting (88 character line length)
- Follow PEP 8 guidelines
- Use type hints where possible
- Keep functions simple (low cyclomatic complexity)

### 3. **Security**
- Run security scans regularly
- Keep dependencies updated
- Follow security best practices
- Review bandit reports

### 4. **Testing**
- Write unit tests for new features
- Maintain good test coverage
- Use meaningful test names
- Mock external dependencies

## Troubleshooting

### Common Issues

1. **Pre-commit Hook Failures**
   ```bash
   # Run hooks manually to see errors
   pre-commit run --all-files
   ```

2. **Type Checking Errors**
   ```bash
   # Run mypy with verbose output
   mypy . --verbose
   ```

3. **Import Sorting Issues**
   ```bash
   # Fix imports manually
   isort .
   ```

4. **Formatting Issues**
   ```bash
   # Format code automatically
   black .
   ```

### Ignoring Issues

Sometimes you need to ignore specific warnings:

```python
# Ignore specific mypy errors
# type: ignore[import-untyped]

# Ignore specific flake8 errors
# noqa: E501

# Ignore bandit warnings
# nosec
```

## Metrics and Reports

### Coverage Report
```bash
make test-cov
# Opens htmlcov/index.html
```

### Security Report
```bash
make security-check
# Check bandit-report.json
```

### Complexity Report
```bash
make complexity-check
# Shows cyclomatic complexity metrics
```

## Continuous Improvement

1. **Regular Reviews**: Review and update tool configurations
2. **Dependency Updates**: Keep tools updated
3. **Rule Refinement**: Adjust rules based on project needs
4. **Team Training**: Ensure team understands tool usage
5. **Automation**: Automate quality checks in CI/CD 