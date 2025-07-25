from abc import ABC, abstractmethod


class DeploymentTarget(ABC):
    @abstractmethod
    def deploy(self, product):
        """Method for deploying the product to the target repository."""
        pass
