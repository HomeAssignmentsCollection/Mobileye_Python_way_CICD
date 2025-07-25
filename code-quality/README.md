# Code Quality Tools and Static Analysis

## 📋 Overview

This directory contains all tools and configurations for code quality, static analysis, and automated code checking in the Product Delivery Pipeline project.

## 🛠️ Tools Included

### **1. Code Formatting**
- **Black**: Automatic code formatter (88 character line length)
- **isort**: Import sorting and organization
- **autopep8**: PEP 8 compliance

### **2. Linting & Static Analysis**
- **flake8**: Style guide enforcement
- **pylint**: Advanced static analysis
- **mypy**: Static type checking
- **yamllint**: YAML file validation

### **3. Security**
- **bandit**: Security vulnerability scanner
- **safety**: Dependency vulnerability checker

### **4. Code Complexity**
- **radon**: Cyclomatic complexity analysis
- **mccabe**: McCabe complexity checker

### **5. Testing**
- **pytest**: Testing framework with coverage
- **pytest-cov**: Coverage reporting
- **pytest-mock**: Mocking utilities

### **6. Pre-commit Hooks**
- **pre-commit**: Git hooks for code quality
- **commitizen**: Commit message formatting

## 📁 File Structure

```
code-quality/
├── README.md                    # This documentation
├── requirements-dev.txt         # Development dependencies
├── .flake8                     # Flake8 configuration
├── .yamllint                   # YAML linting configuration
├── pylintrc                    # Pylint configuration
└── .pre-commit-config.yaml     # Pre-commit hooks configuration
```

## 🚀 Quick Start

### **Installation**
```bash
# Install development dependencies
pip install -r code-quality/requirements-dev.txt

# Install pre-commit hooks
pre-commit install
pre-commit install --hook-type commit-msg
```

### **Run All Quality Checks**
```bash
# From project root
make quality-check

# Or individual tools
make format      # Black formatting
make lint        # Flake8 linting
make type-check  # MyPy type checking
make security-check  # Bandit security scan
```

## 📖 Detailed Tool Documentation

### **Black - Code Formatter**

**Purpose**: Automatic code formatting with consistent style

**Configuration**: Uses `pyproject.toml` settings
```toml
[tool.black]
line-length = 88
target-version = ['py39']
```

**Usage**:
```bash
# Format all Python files
black .

# Check formatting without changes
black --check .

# Format specific file
black src/product_pipeline/main.py
```

**Features**:
- ✅ **Uncompromising**: No configuration options for style
- ✅ **Fast**: Written in Rust for performance
- ✅ **PEP 8 compliant**: Follows Python style guide
- ✅ **Git integration**: Works with pre-commit hooks

### **isort - Import Sorter**

**Purpose**: Organize and sort Python imports

**Configuration**: Uses `pyproject.toml` settings
```toml
[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
include_trailing_comma = true
```

**Usage**:
```bash
# Sort imports in all files
isort .

# Check import sorting
isort --check-only .

# Sort specific file
isort src/product_pipeline/main.py
```

**Features**:
- ✅ **Black compatible**: Works seamlessly with Black
- ✅ **Customizable**: Configurable import grouping
- ✅ **Auto-detection**: Detects import types automatically

### **flake8 - Style Guide Enforcement**

**Purpose**: Enforce Python style guide (PEP 8)

**Configuration**: `.flake8`
```ini
[flake8]
max-line-length = 88
extend-ignore = E203,W503
exclude = 
    __pycache__,
    .git,
    .venv,
    env,
    build,
    dist,
    tests,
    docs,
    *.egg-info
per-file-ignores = 
    __init__.py:F401
```

**Usage**:
```bash
# Run flake8 on all files
flake8 .

# Run on specific directory
flake8 src/

# Show error codes
flake8 --show-source .
```

**Features**:
- ✅ **PEP 8 compliant**: Enforces Python style guide
- ✅ **Configurable**: Customizable rules and exclusions
- ✅ **Fast**: Efficient checking algorithm

### **pylint - Advanced Static Analysis**

**Purpose**: Advanced code analysis and error detection

**Configuration**: `pylintrc`
```ini
[MASTER]
py-version = 3.9
jobs = 0

[MESSAGES CONTROL]
disable = C0114,C0115,C0116,R0903,R0913,W0621,W0703,W0612,W0611

[FORMAT]
max-line-length = 88
```

**Usage**:
```bash
# Run pylint on all files
pylint src/

# Run on specific module
pylint src/product_pipeline/

# Generate report
pylint --reports=y src/
```

**Features**:
- ✅ **Comprehensive**: Checks for errors, warnings, and conventions
- ✅ **Customizable**: Extensive configuration options
- ✅ **Reports**: Detailed analysis reports

### **mypy - Static Type Checking**

**Purpose**: Static type checking for Python

**Configuration**: Uses `pyproject.toml` settings
```toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
disallow_untyped_defs = true
check_untyped_defs = true
```

**Usage**:
```bash
# Type check all files
mypy .

# Check specific module
mypy src/product_pipeline/

# Show error codes
mypy --show-error-codes .
```

**Features**:
- ✅ **Type safety**: Catches type-related errors
- ✅ **Gradual typing**: Works with existing code
- ✅ **IDE integration**: Better IDE support

### **yamllint - YAML Validation**

**Purpose**: Validate YAML files for syntax and style

**Configuration**: `.yamllint`
```yaml
extends: default

rules:
  line-length:
    max: 88
    level: warning
  trailing-spaces: enable
  truthy:
    check-keys: false
```

**Usage**:
```bash
# Validate all YAML files
yamllint .

# Validate specific file
yamllint config/config.yaml

# Show all rules
yamllint --list-files .
```

**Features**:
- ✅ **Syntax checking**: Validates YAML syntax
- ✅ **Style enforcement**: Consistent YAML formatting
- ✅ **Configurable**: Customizable rules

### **bandit - Security Scanner**

**Purpose**: Security vulnerability scanning

**Configuration**: Uses `pyproject.toml` settings
```toml
[tool.bandit]
exclude_dirs = ["tests"]
skips = ["B101", "B601"]
```

**Usage**:
```bash
# Security scan all files
bandit -r .

# Generate JSON report
bandit -r . -f json -o bandit-report.json

# Scan specific file
bandit src/product_pipeline/main.py
```

**Features**:
- ✅ **Security focused**: Detects security vulnerabilities
- ✅ **Multiple formats**: JSON, CSV, XML reports
- ✅ **Configurable**: Skip specific tests

### **radon - Complexity Analysis**

**Purpose**: Analyze code complexity

**Usage**:
```bash
# Cyclomatic complexity
radon cc src/

# Maintainability index
radon mi src/

# All metrics
radon cc src/ -a
radon mi src/ -a
```

**Features**:
- ✅ **Complexity metrics**: Cyclomatic complexity analysis
- ✅ **Maintainability**: Code maintainability index
- ✅ **Visual reports**: ASCII art reports

### **pre-commit - Git Hooks**

**Purpose**: Automated code quality checks before commits

**Configuration**: `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 6.0.1
    hooks:
      - id: isort
```

**Usage**:
```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black
```

**Features**:
- ✅ **Automated**: Runs automatically on commit
- ✅ **Configurable**: Customizable hooks
- ✅ **Fast**: Only checks changed files

## 🔧 Configuration Files

### **requirements-dev.txt**
Contains all development dependencies:
```
# Core linting and formatting
flake8>=7.0.0
black>=25.0.0
isort>=5.13.0
autopep8>=2.0.0

# Type checking
mypy>=1.8.0
types-PyYAML>=6.0.12

# Security scanning
bandit>=1.7.0
safety>=2.3.0

# Code complexity
radon>=6.0.0
mccabe>=0.7.0
pylint>=3.0.0

# Pre-commit hooks
pre-commit>=3.6.0

# Testing
pytest>=8.3.0
pytest-cov>=5.0.0
pytest-mock>=3.12.0
pytest-xdist>=3.5.0

# Documentation
sphinx>=7.2.0
sphinx-rtd-theme>=2.0.0

# Additional tools
yamllint>=1.35.0
```

## 🎯 Best Practices

### **1. Development Workflow**
```bash
# Before committing
make quality-check
make test-cov

# Install pre-commit hooks (one-time)
make pre-commit-install
```

### **2. Code Style**
- Use Black for formatting (88 character line length)
- Follow PEP 8 guidelines
- Use type hints where possible
- Keep functions simple (low cyclomatic complexity)

### **3. Security**
- Run security scans regularly
- Keep dependencies updated
- Follow security best practices
- Review bandit reports

### **4. Testing**
- Write unit tests for new features
- Maintain good test coverage
- Use meaningful test names
- Mock external dependencies

## 🚨 Troubleshooting

### **Common Issues**

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

### **Ignoring Issues**

Sometimes you need to ignore specific warnings:

```python
# Ignore specific mypy errors
# type: ignore[import-untyped]

# Ignore specific flake8 errors
# noqa: E501

# Ignore bandit warnings
# nosec
```

## 📊 Metrics and Reports

### **Coverage Report**
```bash
make test-cov
# Opens htmlcov/index.html
```

### **Security Report**
```bash
make security-check
# Check bandit-report.json
```

### **Complexity Report**
```bash
make complexity-check
# Shows cyclomatic complexity metrics
```

## 🔄 Continuous Improvement

1. **Regular Reviews**: Review and update tool configurations
2. **Dependency Updates**: Keep tools updated
3. **Rule Refinement**: Adjust rules based on project needs
4. **Team Training**: Ensure team understands tool usage
5. **Automation**: Automate quality checks in CI/CD

## 📚 Additional Resources

- [Black Documentation](https://black.readthedocs.io/)
- [isort Documentation](https://pycqa.github.io/isort/)
- [flake8 Documentation](https://flake8.pycqa.org/)
- [pylint Documentation](https://pylint.pycqa.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [bandit Documentation](https://bandit.readthedocs.io/)
- [pre-commit Documentation](https://pre-commit.com/)

## 🤝 Contributing

When adding new code quality tools:

1. **Add to requirements-dev.txt**
2. **Create configuration file**
3. **Update pre-commit hooks**
4. **Update this documentation**
5. **Test with existing codebase**
6. **Update CI/CD pipeline**

## 📝 Changelog

### **v1.0.0** - Initial Setup
- Added Black, isort, flake8, pylint, mypy
- Added bandit for security scanning
- Added radon for complexity analysis
- Added pre-commit hooks
- Added comprehensive documentation 