# Security Best Practices

- **Never commit real secrets or credentials to version control.**
- Use environment variables or secret managers (e.g., Vault, AWS Secrets Manager) for sensitive data.
- Regularly rotate credentials and access keys.
- Use least privilege principle for all service accounts.
- Enable logging and monitoring for all pipeline activities.
- Review dependencies for vulnerabilities (e.g., use `pip-audit`, `safety`).
- Keep Docker images and dependencies up to date.
- Use static analysis tools (e.g., `bandit`) to scan for security issues in code.
- Document all security-related procedures and incident response plans.
