# Product Delivery Pipeline

## Overview

The Product Delivery Pipeline is an object-oriented Python solution designed to manage the build, deployment, and notification processes for multiple products. Each product is treated as a standalone package that can be built, deployed, and versioned independently. The pipeline is executed within a Docker container to ensure portability, scalability, and isolation.

## Features

- **Modular Architecture**: Extensible design with abstract base classes for deployment targets and notification channels
- **Multi-Product Support**: Configure and manage multiple products independently
- **Multiple Deployment Targets**: Support for Artifactory, Nexus, and AWS S3
- **Flexible Notifications**: Email and Slack notification channels
- **Docker Integration**: Containerized execution for consistency and isolation
- **Comprehensive Testing**: Unit tests and integration test framework
- **CI/CD Ready**: GitHub Actions workflow for continuous integration
- **Security Best Practices**: Secure credential management and environment variable support
- **Code Quality Tools**: Comprehensive static analysis, linting, and formatting
- **Pre-commit Hooks**: Automated code quality checks before commits

## Quick Start

### Prerequisites

- Python 3.9+
- Docker
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Mobileye_Python_way_CICD
   ```

2. **Install dependencies**:
   ```bash
   # Install runtime dependencies
   pip install -r requirements.txt
   
   # Install development dependencies (for code quality tools)
   pip install -r requirements-dev.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your actual credentials
   ```

4. **Install pre-commit hooks**:
   ```bash
   make pre-commit-install
   ```

5. **Run the pipeline**:
   ```bash
   python product_pipeline.py --repo_name ProductA
   ```

### Using Docker

```bash
# Build the Docker image
make build

# Run the pipeline in Docker
make docker-run

# Or use docker-compose
docker-compose up product-pipeline
```

## Code Quality Tools

The project includes comprehensive code quality tools:

### **Code Formatting**
- **Black**: Automatic code formatter (88 character line length)
- **isort**: Import sorting and organization
- **autopep8**: PEP 8 compliance

### **Linting & Static Analysis**
- **flake8**: Style guide enforcement
- **pylint**: Advanced static analysis
- **mypy**: Static type checking
- **yamllint**: YAML file validation

### **Security**
- **bandit**: Security vulnerability scanner
- **safety**: Dependency vulnerability checker

### **Code Complexity**
- **radon**: Cyclomatic complexity analysis
- **mccabe**: McCabe complexity checker

### **Testing**
- **pytest**: Testing framework with coverage
- **pytest-cov**: Coverage reporting
- **pytest-mock**: Mocking utilities

### **Pre-commit Hooks**
- **pre-commit**: Git hooks for code quality
- **commitizen**: Commit message formatting

## Development Workflow

### **Before Committing**
```bash
# Run all quality checks
make quality-check

# Run tests with coverage
make test-cov

# Format code
make format

# Install pre-commit hooks (one-time setup)
make pre-commit-install
```

### **Individual Tools**
```bash
# Code formatting
make format
make format-check

# Linting
make lint

# Type checking
make type-check

# Security scanning
make security-check

# Complexity analysis
make complexity-check

# Testing
make test
make test-cov
```

### **Pre-commit Hooks**
Pre-commit hooks automatically run quality checks before each commit:
- Code formatting (Black, isort)
- Linting (flake8, pylint)
- Type checking (mypy)
- Security scanning (bandit)
- File validation (YAML, JSON)
- Commit message formatting (commitizen)

## Configuration

### Product Configuration (`config.yaml`)

```yaml
products:
  - product_name: "ProductA"
    git_repository: "https://github.com/example/ProductA.git"
    default_target_branch: "main"
    repositories:
      artifactory:
        enabled: true
        credentials_ref: "artifactory"
      nexus:
        enabled: false
      s3:
        enabled: true
        credentials_ref: "s3"
    notifications:
      email:
        enabled: true
        config:
          smtp_server: "smtp.example.com"
          port: 587
      slack:
        enabled: true
        config:
          webhook_url: "https://hooks.slack.com/services/xxx"
```

### Secrets Configuration (`secrets.yaml`)

```yaml
artifactory:
  username: "${ARTIFACTORY_USER}"
  password: "${ARTIFACTORY_PASSWORD}"

nexus:
  username: "${NEXUS_USER}"
  password: "${NEXUS_PASSWORD}"

s3:
  access_key: "${S3_ACCESS_KEY}"
  secret_key: "${S3_SECRET_KEY}"
```

## Project Structure

```
Mobileye_Python_way_CICD/
├── product_pipeline.py              # Main entry point
├── pipelines/                       # Core pipeline logic
├── notifications/                   # Notification channels
├── repositories/                    # Deployment targets
├── utils_py/                        # Utility modules
├── unit_test_PyTest/                # Test suite
├── docs/                            # Documentation
├── src/                             # Source code (future)
├── config.yaml                      # Product configuration
├── secrets.yaml                     # Secure credentials
├── requirements.txt                 # Runtime dependencies
├── requirements-dev.txt             # Development dependencies
├── requirements-prod.txt            # Production dependencies
├── Dockerfile                       # Container definition
├── docker-compose.yml              # Local development
├── Makefile                        # Development tasks
├── pyproject.toml                  # Tool configuration
├── tox.ini                         # Test automation
├── setup.py                        # Package configuration
├── .pre-commit-config.yaml         # Pre-commit hooks
├── .flake8                         # Flake8 configuration
├── .yamllint                       # YAML linting configuration
├── pylintrc                        # Pylint configuration
├── .github/workflows/ci.yml        # CI/CD pipeline
├── env.example                     # Environment template
├── .gitignore                      # Git ignores
├── .dockerignore                   # Docker ignores
├── CONTRIBUTING.md                 # Contribution guidelines
├── CODE_OF_CONDUCT.md             # Code of conduct
├── security_placeholder.md         # Security guidelines
└── README.md                       # This file
```

## Architecture

The pipeline follows a modular, extensible architecture:

1. **Main Entry Point**: `product_pipeline.py` orchestrates the entire process
2. **Pipeline Engine**: `pipelines/pipeline.py` contains core logic and stage execution
3. **Deployment Targets**: Abstract base class with implementations for Artifactory, Nexus, and S3
4. **Notification Channels**: Abstract base class with implementations for Email and Slack
5. **Configuration Management**: YAML-based configuration with environment variable support
6. **Utility Modules**: Logging, configuration loading, and helper functions

## Extending the Pipeline

### Adding New Deployment Targets

1. Create a new class in `repositories/`
2. Inherit from `DeploymentTarget`
3. Implement the `deploy()` method
4. Update the factory function in `pipelines/pipeline.py`

### Adding New Notification Channels

1. Create a new class in `notifications/`
2. Inherit from `NotificationChannel`
3. Implement the `notify()` method
4. Update the factory function in `pipelines/pipeline.py`

### Adding New Pipeline Stages

1. Add the stage name to `IMPLEMENTED_STAGES`
2. Implement stage logic in the `Product` class
3. Add stage handling in `Pipeline.run()`

## Security

- **Never commit real secrets** to version control
- Use environment variables or secret managers for sensitive data
- Regularly rotate credentials and access keys
- Follow the security guidelines in `security_placeholder.md`
- Run security scans regularly with `make security-check`

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### **Development Setup**
```bash
# Install development dependencies
make install-dev-deps

# Install pre-commit hooks
make pre-commit-install

# Run quality checks
make quality-check

# Run tests
make test-cov
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions and support, please:
1. Check the [documentation](docs/)
2. Review existing [issues](../../issues)
3. Create a new issue if needed

## Project Structure (Best Practices)

- All source code should be moved under `src/` for import safety and packaging.
- Tests are in `unit_test_PyTest/` (consider renaming to `tests/` in the future).
- Use `Makefile` for common development tasks.
- Use `Dockerfile` and `.dockerignore` for containerization.
- Use `pyproject.toml` for tool configuration.
- Use `tox.ini` for test automation.
- Use `.gitignore` to avoid committing unnecessary files.
- Use `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` for open source best practices.
- Use `docs/` for detailed documentation and diagrams.
- Use `security_placeholder.md` for actionable security guidelines.
- Use `src/__version__.py` for project versioning.
- Use pre-commit hooks for automated code quality checks.
- Use comprehensive static analysis tools for code quality. 