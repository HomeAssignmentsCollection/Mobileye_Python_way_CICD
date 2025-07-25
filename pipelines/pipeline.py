import time
import sys  # Needed to exit in case of an error
from utils_py.logger_setup import get_logger
from repositories.artifactory import ArtifactoryTarget
from repositories.nexus import NexusTarget
from repositories.s3 import S3Target
from notifications.email_channel import EmailNotification
from notifications.slack_channel import SlackNotification

logger = get_logger("Pipeline")

# List of implemented pipeline steps
IMPLEMENTED_STEPS = ["build", "deploy", "notify"]


class Product:
    def __init__(
        self,
        name,
        git_repository,
        scheduled_time,
        target_branch,
        deploy_targets,
        notification_channels,
        valid_stages=None,
    ):
        self.name = name
        self.git_repository = git_repository
        self.scheduled_time = scheduled_time
        self.target_branch = target_branch
        self.deploy_targets = deploy_targets
        self.notification_channels = notification_channels
        # Use provided valid_stages or default to IMPLEMENTED_STEPS
        self.valid_stages = (
            valid_stages if valid_stages is not None else IMPLEMENTED_STEPS
        )

    def build(self):
        msg = f"Building product '{self.name}' from repository '{self.git_repository}' on branch '{self.target_branch}'."
        logger.info(msg)
        print(f"[Build] {msg}")

    def deploy(self):
        msg = f"Deploying product '{self.name}'."
        logger.info(msg)
        print(f"[Deploy] {msg}")
        for target in self.deploy_targets:
            target.deploy(self)

    def notify(self):
        msg = f"Notifying about product '{self.name}'."
        logger.info(msg)
        print(f"[Notify] {msg}")
        for channel in self.notification_channels:
            channel.notify(self)


class Pipeline:
    def __init__(self, product: Product, stages=None):
        self.product = product
        # Use provided stages or default to product.valid_stages
        if stages is None:
            stages = product.valid_stages
        # Validate that each provided stage is implemented
        for stage in stages:
            if stage not in IMPLEMENTED_STEPS:
                print(f"Error: Functionality for step '{stage}' is not implemented.")
                sys.exit(1)
        self.stages = stages

    def run(self):
        logger.info(f"Starting pipeline for product: '{self.product.name}'")
        print(f"Starting pipeline for product: '{self.product.name}'")
        for stage in self.stages:
            if stage == "build":
                self.product.build()
            elif stage == "deploy":
                self.product.deploy()
            elif stage == "notify":
                self.product.notify()
            time.sleep(1)  # Simulate delay between stages
        logger.info("Pipeline finished.")
        print("Pipeline finished.")


def create_deployment_target(repo_type, repo_config):
    target = None
    if repo_type.lower() == "artifactory" and repo_config.get("enabled", False):
        target = ArtifactoryTarget(
            credentials_ref=repo_config.get("credentials_ref"),
            credentials=repo_config.get("credentials"),
        )
    elif repo_type.lower() == "nexus" and repo_config.get("enabled", False):
        target = NexusTarget(
            credentials_ref=repo_config.get("credentials_ref"),
            credentials=repo_config.get("credentials"),
        )
    elif repo_type.lower() == "s3" and repo_config.get("enabled", False):
        target = S3Target(
            credentials_ref=repo_config.get("credentials_ref"),
            credentials=repo_config.get("credentials"),
        )
    return target


def create_notification_channel(channel_type, channel_config):
    channel = None
    if channel_type.lower() == "email" and channel_config.get("enabled", False):
        channel = EmailNotification(config=channel_config.get("config", {}))
    elif channel_type.lower() == "slack" and channel_config.get("enabled", False):
        channel = SlackNotification(config=channel_config.get("config", {}))
    return channel
