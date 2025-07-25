from product_pipeline.repositories.base import DeploymentTarget
from product_pipeline.utils.logging import get_logger

logger = get_logger("S3")


class S3Target(DeploymentTarget):
    def __init__(self, credentials_ref=None, credentials=None):
        self.credentials_ref = credentials_ref
        self.credentials = credentials

    def deploy(self, product):
        msg = f"Deploying product '{product.name}' to S3 (credentials: {self.credentials})."
        logger.info(msg)
        print(f"[S3] {msg}")
