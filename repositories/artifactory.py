from repositories.base_repository import DeploymentTarget
from utils_py.logger_setup import get_logger

logger = get_logger("Artifactory")


class ArtifactoryTarget(DeploymentTarget):
    def __init__(self, credentials_ref=None, credentials=None):
        self.credentials_ref = credentials_ref
        self.credentials = credentials

    def deploy(self, product):
        msg = f"Deploying product '{product.name}' to Artifactory (credentials: {self.credentials})."
        logger.info(msg)
        print(f"[Artifactory] {msg}")
