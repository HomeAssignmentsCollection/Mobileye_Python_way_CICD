import sys
import os
import pytest

# Add the project root directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.product_pipeline.main import main

# Fake implementations for external functions


def fake_load_configuration():
    """
    Fake load_configuration returns a dummy configuration dictionary.
    """
    return {
        "products": [
            {
                "product_name": "TestProduct",
                "git_repository": "https://example.com/test.git",
                "default_target_branch": "main",
                "deploy_targets": [],
                "notification_channels": [],
            }
        ]
    }


def fake_find_product_config(config, repo_name):
    """
    Fake find_product_config returns the product config if found.
    """
    for product in config.get("products", []):
        if product.get("product_name") == repo_name:
            return product
    # Return a valid product config for TestProduct
    if repo_name == "TestProduct":
        return {
            "product_name": "TestProduct",
            "git_repository": "https://github.com/example/TestProduct.git",
            "default_target_branch": "main",
            "repositories": {},
            "notifications": {},
        }
    return {}


def fake_init_deployment_targets(product_config):
    """
    Fake init_deployment_targets returns an empty list.
    """
    return []


def fake_init_notification_channels(product_config):
    """
    Fake init_notification_channels returns an empty list.
    """
    return []


def test_product_pipeline_valid(monkeypatch, capsys):
    """
    Test product_pipeline.main() with valid stages.
    This simulates passing valid command-line arguments and verifies output.
    """
    # Override external configuration functions with fake implementations
    monkeypatch.setattr(
        "src.product_pipeline.utils.config.load_configuration", fake_load_configuration
    )
    monkeypatch.setattr(
        "src.product_pipeline.utils.helpers.find_product_config",
        fake_find_product_config,
    )
    monkeypatch.setattr(
        "src.product_pipeline.utils.helpers.init_deployment_targets",
        fake_init_deployment_targets,
    )
    monkeypatch.setattr(
        "src.product_pipeline.utils.helpers.init_notification_channels",
        fake_init_notification_channels,
    )

    # Mock the Docker container check
    monkeypatch.setattr(
        "os.environ.get",
        lambda key, default=None: "1" if key == "INSIDE_DOCKER" else default,
    )

    # Set sys.argv to simulate command-line arguments for a valid case
    test_args = [
        "product_pipeline.py",
        "--repo_name",
        "TestProduct",
        "--stages",
        "build,deploy,notify",
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    # Run the main function
    main()

    # Capture the output and verify expected strings
    output = capsys.readouterr().out
    assert "[DEBUG]" in output
    assert "Starting pipeline for product: 'TestProduct'" in output
    assert "Pipeline finished." in output


def test_product_pipeline_invalid_stage(monkeypatch, capsys):
    """
    Test product_pipeline.main() with an invalid stage.
    An invalid stage should cause the script to exit with error code 1.
    """
    # Override external configuration functions with fake implementations
    monkeypatch.setattr(
        "src.product_pipeline.utils.config.load_configuration", fake_load_configuration
    )
    monkeypatch.setattr(
        "src.product_pipeline.utils.helpers.find_product_config",
        fake_find_product_config,
    )
    monkeypatch.setattr(
        "src.product_pipeline.utils.helpers.init_deployment_targets",
        fake_init_deployment_targets,
    )
    monkeypatch.setattr(
        "src.product_pipeline.utils.helpers.init_notification_channels",
        fake_init_notification_channels,
    )

    # Set sys.argv with an invalid stage ("invalid")
    test_args = [
        "product_pipeline.py",
        "--repo_name",
        "TestProduct",
        "--stages",
        "build,invalid,notify",
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    with pytest.raises(SystemExit) as e:
        main()

    # Check that the exit code is 1
    assert e.value.code == 1

    # Optionally, check that an appropriate error message was printed
    output = capsys.readouterr().out
    assert "Error: Stage 'invalid' is not valid." in output
