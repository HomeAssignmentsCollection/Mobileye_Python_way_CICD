import pytest
from unittest.mock import patch, MagicMock
from repositories.artifactory import ArtifactoryTarget
from repositories.nexus import NexusTarget
from repositories.s3 import S3Target
from repositories.base_repository import DeploymentTarget


class TestDeploymentTarget:
    """Test the abstract base class for deployment targets."""

    def test_abstract_methods(self):
        """Test that abstract methods are properly defined."""
        # Should not be able to instantiate abstract class
        with pytest.raises(TypeError):
            DeploymentTarget()


class TestArtifactoryTarget:
    """Test Artifactory deployment target."""

    def test_artifactory_target_init(self):
        """Test Artifactory target initialization."""
        target = ArtifactoryTarget(
            credentials_ref="artifactory",
            credentials={"username": "user", "password": "pass"},
        )
        assert target.credentials_ref == "artifactory"
        assert target.credentials == {"username": "user", "password": "pass"}

    def test_artifactory_deploy(self):
        """Test Artifactory deployment."""
        target = ArtifactoryTarget(
            credentials_ref="artifactory",
            credentials={"username": "user", "password": "pass"},
        )

        # Mock product
        mock_product = MagicMock()
        mock_product.name = "TestProduct"

        # Test deployment (currently just logs)
        target.deploy(mock_product)
        # No assertion needed as it just logs for now


class TestNexusTarget:
    """Test Nexus deployment target."""

    def test_nexus_target_init(self):
        """Test Nexus target initialization."""
        target = NexusTarget(
            credentials_ref="nexus",
            credentials={"username": "user", "password": "pass"},
        )
        assert target.credentials_ref == "nexus"
        assert target.credentials == {"username": "user", "password": "pass"}

    def test_nexus_deploy(self):
        """Test Nexus deployment."""
        target = NexusTarget(
            credentials_ref="nexus",
            credentials={"username": "user", "password": "pass"},
        )

        # Mock product
        mock_product = MagicMock()
        mock_product.name = "TestProduct"

        # Test deployment (currently just logs)
        target.deploy(mock_product)
        # No assertion needed as it just logs for now


class TestS3Target:
    """Test S3 deployment target."""

    def test_s3_target_init(self):
        """Test S3 target initialization."""
        target = S3Target(
            credentials_ref="s3",
            credentials={"access_key": "key", "secret_key": "secret"},
        )
        assert target.credentials_ref == "s3"
        assert target.credentials == {"access_key": "key", "secret_key": "secret"}

    def test_s3_deploy(self):
        """Test S3 deployment."""
        target = S3Target(
            credentials_ref="s3",
            credentials={"access_key": "key", "secret_key": "secret"},
        )

        # Mock product
        mock_product = MagicMock()
        mock_product.name = "TestProduct"

        # Test deployment (currently just logs)
        target.deploy(mock_product)
        # No assertion needed as it just logs for now


class TestDeploymentTargetFactory:
    """Test deployment target factory functions."""

    def test_create_artifactory_target(self):
        """Test creating Artifactory target."""
        from pipelines.pipeline import create_deployment_target

        repo_config = {
            "enabled": True,
            "credentials_ref": "artifactory",
            "credentials": {"username": "user", "password": "pass"},
        }

        target = create_deployment_target("artifactory", repo_config)
        assert isinstance(target, ArtifactoryTarget)
        assert target.credentials_ref == "artifactory"

    def test_create_nexus_target(self):
        """Test creating Nexus target."""
        from pipelines.pipeline import create_deployment_target

        repo_config = {
            "enabled": True,
            "credentials_ref": "nexus",
            "credentials": {"username": "user", "password": "pass"},
        }

        target = create_deployment_target("nexus", repo_config)
        assert isinstance(target, NexusTarget)
        assert target.credentials_ref == "nexus"

    def test_create_s3_target(self):
        """Test creating S3 target."""
        from pipelines.pipeline import create_deployment_target

        repo_config = {
            "enabled": True,
            "credentials_ref": "s3",
            "credentials": {"access_key": "key", "secret_key": "secret"},
        }

        target = create_deployment_target("s3", repo_config)
        assert isinstance(target, S3Target)
        assert target.credentials_ref == "s3"

    def test_create_disabled_target(self):
        """Test creating disabled target returns None."""
        from pipelines.pipeline import create_deployment_target

        repo_config = {"enabled": False, "credentials_ref": "artifactory"}

        target = create_deployment_target("artifactory", repo_config)
        assert target is None
