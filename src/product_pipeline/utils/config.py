import os
import yaml
from product_pipeline.utils.logging import get_logger

logger = get_logger("ConfigLoader")


def load_yaml_file(filepath):
    with open(filepath, "r") as f:
        return yaml.safe_load(f)


def load_configuration():
    # Assume config.yaml and secrets.yaml are in the project root.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    config_path = os.path.join(project_root, "config.yaml")
    secrets_path = os.path.join(project_root, "secrets.yaml")

    if not os.path.exists(config_path):
        logger.error(f"Configuration file {config_path} not found!")
        raise FileNotFoundError(f"Configuration file {config_path} not found!")
    if not os.path.exists(secrets_path):
        logger.error(f"Secrets file {secrets_path} not found!")
        raise FileNotFoundError(f"Secrets file {secrets_path} not found!")

    config = load_yaml_file(config_path)
    secrets = load_yaml_file(secrets_path) or {}

    # Process placeholders in secrets (e.g., "${ARTIFACTORY_USER}")
    for service, creds in secrets.items():
        if creds is None:
            continue
        for key, value in creds.items():
            if (
                isinstance(value, str)
                and value.startswith("${")
                and value.endswith("}")
            ):
                env_var = value[2:-1]
                creds[key] = os.environ.get(env_var, value)

    # Merge secrets into repository configurations
    for product in config.get("products", []):
        repos = product.get("repositories", {})
        for repo_type, repo_conf in repos.items():
            if repo_conf.get("enabled", False) and repo_conf.get("credentials_ref"):
                secret_key = repo_conf.get("credentials_ref")
                if secret_key in secrets:
                    repo_conf["credentials"] = secrets[secret_key]

    return config
