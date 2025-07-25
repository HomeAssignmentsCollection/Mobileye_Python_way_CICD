# Naming Conventions

## 📋 Overview

This document outlines the naming conventions used in the Product Delivery Pipeline project, following Python best practices and industry standards.

## 🐍 Python Naming Conventions

### **Files and Directories**

#### **Python Files**
- **snake_case**: All Python files should use snake_case
- **Examples**:
  - ✅ `main.py`
  - ✅ `config_loader.py`
  - ✅ `email_notification.py`
  - ❌ `ConfigLoader.py`
  - ❌ `emailNotification.py`

#### **Directories**
- **snake_case**: All directories should use snake_case
- **Examples**:
  - ✅ `src/`
  - ✅ `product_pipeline/`
  - ✅ `notifications/`
  - ✅ `utils/`
  - ❌ `ProductPipeline/`
  - ❌ `utils_py/`

#### **Special Files**
- **`__init__.py`**: Package initialization files
- **`__version__.py`**: Version information
- **`__main__.py`**: Entry point for modules

### **Code Elements**

#### **Variables and Functions**
- **snake_case**: Variables and functions
- **Examples**:
  ```python
  # Variables
  user_name = "john_doe"
  config_file = "config.yaml"
  
  # Functions
  def load_configuration():
      pass
  
  def send_email_notification():
      pass
  ```

#### **Classes**
- **PascalCase**: Class names
- **Examples**:
  ```python
  class ProductPipeline:
      pass
  
  class EmailNotification:
      pass
  
  class DeploymentTarget:
      pass
  ```

#### **Constants**
- **UPPER_SNAKE_CASE**: Constants and module-level variables
- **Examples**:
  ```python
  DEFAULT_TIMEOUT = 30
  MAX_RETRY_ATTEMPTS = 3
  SUPPORTED_FORMATS = ["yaml", "json"]
  ```

#### **Protected and Private**
- **Single underscore**: Protected members
- **Double underscore**: Private members
- **Examples**:
  ```python
  class Pipeline:
      def __init__(self):
          self._config = {}  # Protected
          self.__secret_key = "abc"  # Private
  ```

## 📁 Project Structure Naming

### **Root Level**
```
Mobileye_Python_way_CICD/
├── src/                    # Source code (snake_case)
├── tests/                  # Test files (snake_case)
├── docs/                   # Documentation (snake_case)
├── config/                 # Configuration (snake_case)
├── scripts/                # Utility scripts (snake_case)
├── code-quality/           # Code quality tools (kebab-case)
├── requirements.txt        # Dependencies (snake_case)
├── pyproject.toml         # Project config (snake_case)
├── setup.py               # Package setup (snake_case)
├── Dockerfile             # Container definition (PascalCase)
├── docker-compose.yml     # Docker compose (kebab-case)
├── Makefile               # Build automation (PascalCase)
├── README.md              # Documentation (PascalCase)
└── .gitignore             # Git ignore (dot-case)
```

### **Source Code Structure**
```
src/
└── product_pipeline/       # Main package (snake_case)
    ├── __init__.py
    ├── __version__.py
    ├── main.py            # Entry point (snake_case)
    ├── core/              # Core functionality (snake_case)
    │   ├── __init__.py
    │   └── pipeline.py
    ├── notifications/     # Notification channels (snake_case)
    │   ├── __init__.py
    │   ├── base.py
    │   ├── email.py
    │   └── slack.py
    ├── repositories/      # Deployment targets (snake_case)
    │   ├── __init__.py
    │   ├── base.py
    │   ├── artifactory.py
    │   ├── nexus.py
    │   └── s3.py
    ├── utils/             # Utilities (snake_case)
    │   ├── __init__.py
    │   ├── config.py
    │   ├── helpers.py
    │   └── logging.py
    └── stages/            # Pipeline stages (snake_case)
        ├── __init__.py
        ├── clone.py
        ├── deploy.py
        ├── test.py
        └── notify.py
```

### **Test Structure**
```
tests/
├── __init__.py
├── unit/                  # Unit tests (snake_case)
│   ├── test_main.py
│   ├── test_notifications.py
│   ├── test_repositories.py
│   ├── test_pipeline.py
│   └── test_utils.py
└── integration/           # Integration tests (snake_case)
    └── test_integration.py
```

## 🔧 Configuration Files

### **File Extensions**
- **`.py`**: Python source files
- **`.yaml`**: YAML configuration files
- **`.yml`**: Alternative YAML extension
- **`.toml`**: TOML configuration files
- **`.ini`**: INI configuration files
- **`.json`**: JSON data files
- **`.md`**: Markdown documentation

### **Configuration File Naming**
```
config/
├── config.yaml           # Main configuration
├── secrets.yaml          # Secrets and credentials
└── env.example           # Environment template

code-quality/
├── .flake8              # Flake8 configuration
├── .yamllint            # YAML linting configuration
├── pylintrc             # Pylint configuration
└── .pre-commit-config.yaml  # Pre-commit hooks
```

## 🐳 Docker and Container Files

### **Docker Files**
- **`Dockerfile`**: Main container definition
- **`docker-compose.yml`**: Multi-container setup
- **`.dockerignore`**: Docker ignore patterns

### **Docker Naming**
```dockerfile
# Image names
product-pipeline:latest
product-pipeline:dev
product-pipeline:test

# Container names
product-pipeline-prod
product-pipeline-dev
product-pipeline-test
```

## 📦 Package and Module Naming

### **Package Names**
- **snake_case**: Package names
- **Examples**:
  - `product_pipeline`
  - `notifications`
  - `repositories`
  - `utils`

### **Module Names**
- **snake_case**: Module names
- **Examples**:
  - `main.py`
  - `pipeline.py`
  - `config_loader.py`
  - `email_notification.py`

### **Import Statements**
```python
# Package imports
from product_pipeline.core.pipeline import Product, Pipeline
from product_pipeline.notifications.email import EmailNotification
from product_pipeline.utils.config import load_configuration

# Standard library imports
import os
import sys
import yaml

# Third-party imports
import pytest
import docker
```

## 🧪 Test Naming

### **Test Files**
- **Prefix**: All test files should start with `test_`
- **snake_case**: Use snake_case for test file names
- **Examples**:
  - `test_main.py`
  - `test_notifications.py`
  - `test_repositories.py`
  - `test_integration.py`

### **Test Functions**
- **Prefix**: All test functions should start with `test_`
- **Descriptive**: Use descriptive names that explain what is being tested
- **Examples**:
  ```python
  def test_load_configuration_success():
      pass
  
  def test_email_notification_send():
      pass
  
  def test_pipeline_execution_with_valid_stages():
      pass
  ```

### **Test Classes**
- **PascalCase**: Test classes should use PascalCase
- **Prefix**: Start with `Test` if needed
- **Examples**:
  ```python
  class TestEmailNotification:
      pass
  
  class TestProductPipeline:
      pass
  ```

## 🔍 Code Quality Tools

### **Configuration Files**
```
code-quality/
├── .flake8              # Flake8 linting
├── .yamllint            # YAML validation
├── pylintrc             # Pylint analysis
└── .pre-commit-config.yaml  # Git hooks
```

### **Report Files**
- **snake_case**: Report file names
- **Examples**:
  - `bandit-report.json`
  - `coverage-report.xml`
  - `pylint-report.txt`

## 📝 Documentation Naming

### **Documentation Files**
- **PascalCase**: Main documentation files
- **snake_case**: Technical documentation
- **Examples**:
  - `README.md`
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `naming_conventions.md`
  - `api_documentation.md`

### **Documentation Structure**
```
docs/
├── README.md                    # Main documentation
├── api.md                       # API documentation
├── architecture.md              # Architecture overview
├── code-quality.md              # Code quality guide
├── docker-best-practices.md     # Docker guidelines
├── naming-conventions.md        # This file
├── project-structure-analysis.md # Structure analysis
├── restructure-completion-summary.md # Restructure summary
└── structure-recommendations.md # Structure recommendations
```

## 🚫 What to Avoid

### **Anti-patterns**
- ❌ **camelCase** for Python files and directories
- ❌ **PascalCase** for variables and functions
- ❌ **UPPERCASE** for regular variables
- ❌ **Mixed_case** or **mixedCase**
- ❌ **UPPER_CASE** for regular constants
- ❌ **lowercase** for classes

### **Examples of Bad Naming**
```python
# ❌ Bad
class emailNotification:  # Should be PascalCase
    def SendEmail():      # Should be snake_case
        pass

# ❌ Bad
def LoadConfig():         # Should be snake_case
    pass

# ❌ Bad
userName = "john"         # Should be snake_case

# ❌ Bad
CONFIG_FILE = "config.yaml"  # Should be UPPER_SNAKE_CASE for constants
```

## ✅ Best Practices Summary

1. **Use snake_case** for files, directories, variables, and functions
2. **Use PascalCase** for classes
3. **Use UPPER_SNAKE_CASE** for constants
4. **Use descriptive names** that explain purpose
5. **Be consistent** across the entire project
6. **Follow Python PEP 8** guidelines
7. **Use meaningful prefixes** for test files and functions
8. **Keep names short but descriptive**
9. **Avoid abbreviations** unless they are widely understood
10. **Use plural names** for collections and directories containing multiple items

## 🔧 Tools for Enforcement

### **Automated Checks**
- **Flake8**: Style guide enforcement
- **Pylint**: Naming convention checks
- **Pre-commit hooks**: Automated validation
- **Black**: Code formatting
- **isort**: Import sorting

### **Manual Checks**
- **Code reviews**: Peer review of naming
- **Documentation**: Keep this guide updated
- **Team training**: Ensure team awareness

## 📚 References

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python - Python Naming Conventions](https://realpython.com/python-naming-conventions/) 