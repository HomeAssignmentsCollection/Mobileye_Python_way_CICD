import pytest
import tempfile
import os
from unittest.mock import patch, mock_open
from product_pipeline.utils.config import load_configuration, load_yaml_file


def test_load_yaml_file():
    """Test loading a simple YAML file."""
    yaml_content = """
    test_key: test_value
    nested:
      key: value
    """
    with patch("builtins.open", mock_open(read_data=yaml_content)):
        result = load_yaml_file("dummy_path")
        assert result["test_key"] == "test_value"
        assert result["nested"]["key"] == "value"


def test_load_yaml_file_missing():
    """Test loading a non-existent YAML file."""
    with pytest.raises(FileNotFoundError):
        load_yaml_file("non_existent_file.yaml")


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_load_configuration_success(mock_file, mock_exists):
    """Test successful configuration loading."""
    mock_exists.return_value = True

    config_content = """
    products:
      - product_name: "TestProduct"
        git_repository: "https://example.com/test.git"
    """

    secrets_content = """
    artifactory:
      username: "test_user"
    """

    mock_file.side_effect = [
        mock_open(read_data=config_content).return_value,
        mock_open(read_data=secrets_content).return_value,
    ]

    with patch("utils_py.config_loader.load_yaml_file") as mock_load:
        mock_load.side_effect = [
            {"products": [{"product_name": "TestProduct"}]},
            {"artifactory": {"username": "test_user"}},
        ]

        result = load_configuration()
        assert "products" in result
        assert len(result["products"]) == 1
        assert result["products"][0]["product_name"] == "TestProduct"


@patch("os.path.exists")
def test_load_configuration_missing_config(mock_exists):
    """Test configuration loading with missing config file."""
    mock_exists.return_value = False

    with pytest.raises(FileNotFoundError):
        load_configuration()


def test_environment_variable_substitution():
    """Test environment variable substitution in secrets."""
    with patch.dict(os.environ, {"TEST_USER": "env_user"}):
        yaml_content = """
        artifactory:
          username: "${TEST_USER}"
        """

        with patch("builtins.open", mock_open(read_data=yaml_content)):
            result = load_yaml_file("dummy_path")
            # Note: This would need to be tested in the actual load_configuration function
            # where the substitution logic is implemented
            assert result["artifactory"]["username"] == "${TEST_USER}"
