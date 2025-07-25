import sys
import os

# Add the project root directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from product_pipeline.core.pipeline import Product, Pipeline


# Dummy deployment target for testing
class DummyTarget:
    def __init__(self):
        self.deployed = False

    def deploy(self, product):
        self.deployed = True


# Dummy notification channel for testing
class DummyChannel:
    def __init__(self):
        self.notified = False

    def notify(self, product):
        self.notified = True


# Fixture to create a dummy product with dummy dependencies
@pytest.fixture
def dummy_product():
    deploy_target = DummyTarget()
    notification_channel = DummyChannel()
    product = Product(
        name="TestProduct",
        git_repository="https://example.com/test.git",
        scheduled_time="2025-03-01T00:00:00",  # Dummy scheduled time
        target_branch="main",
        deploy_targets=[deploy_target],
        notification_channels=[notification_channel],
        valid_stages=["build", "deploy", "notify"],
    )
    return product, deploy_target, notification_channel


# Test for the build stage
def test_build(dummy_product, capsys):
    product, _, _ = dummy_product
    product.build()
    captured = capsys.readouterr().out
    # Check that the build message is printed
    assert "Building product 'TestProduct'" in captured


# Test for the deploy stage
def test_deploy(dummy_product):
    product, deploy_target, _ = dummy_product
    product.deploy()
    # Verify that the dummy deploy target was used
    assert deploy_target.deployed == True


# Test for the notify stage
def test_notify(dummy_product):
    product, _, notification_channel = dummy_product
    product.notify()
    # Verify that the dummy notification channel was used
    assert notification_channel.notified == True


# Test for the entire pipeline run
def test_pipeline_run(dummy_product, capsys):
    product, deploy_target, notification_channel = dummy_product
    pipeline = Pipeline(product, stages=["build", "deploy", "notify"])
    pipeline.run()
    # Verify that deploy and notify were called during pipeline run
    assert deploy_target.deployed == True
    assert notification_channel.notified == True
    captured = capsys.readouterr().out
    # Check that the output includes the starting message
    assert "Starting pipeline for product: 'TestProduct'" in captured
