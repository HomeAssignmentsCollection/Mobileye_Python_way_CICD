import sys
from utils_py.logger_setup import get_logger
from pipelines.pipeline import create_deployment_target, create_notification_channel

logger = get_logger("ConfigHelper")


def find_product_config(config, repo_name):
    """
    Searches the configuration for a product with the given repo_name.
    Returns the product configuration if found, otherwise logs an error and exits.
    """
    for prod in config.get("products", []):
        if prod.get("product_name") == repo_name:
            return prod
    logger.error(f"Product '{repo_name}' not found in configuration!")
    sys.exit(1)


def init_deployment_targets(product_config):
    """
    Initializes deployment targets based on the product configuration.
    Returns a list of deployment target objects.
    """
    deploy_targets = []
    repos_config = product_config.get("repositories", {})
    for repo_type in ["artifactory", "nexus", "s3"]:
        repo_conf = repos_config.get(repo_type, {})
        target_obj = create_deployment_target(repo_type, repo_conf)
        if target_obj:
            deploy_targets.append(target_obj)
    return deploy_targets


def init_notification_channels(product_config):
    """
    Initializes notification channels based on the product configuration.
    Returns a list of notification channel objects.
    """
    notification_channels = []
    notifications_config = product_config.get("notifications", {})
    for channel_type in ["email", "slack"]:
        chan_conf = notifications_config.get(channel_type, {})
        notif_obj = create_notification_channel(channel_type, chan_conf)
        if notif_obj:
            notification_channels.append(notif_obj)
    return notification_channels
