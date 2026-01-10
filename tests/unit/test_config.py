"""Test configuration loading and validation."""

import pytest
from pydantic import ValidationError

from src.config.env import APIConfig, Config, LogConfig, PathConfig, get_config


def test_api_config_defaults():
    """Test APIConfig with default values."""
    config = APIConfig()
    assert config.api_adresse_base_url == "https://api-adresse.data.gouv.fr"
    assert config.api_adresse_rate_limit == 50


def test_api_config_rate_limit_validation():
    """Test rate limit validation."""
    # Valid
    config = APIConfig(api_adresse_rate_limit=10)
    assert config.api_adresse_rate_limit == 10

    # Invalid (too low)
    with pytest.raises(ValidationError):
        APIConfig(api_adresse_rate_limit=0)

    # Invalid (too high)
    with pytest.raises(ValidationError):
        APIConfig(api_adresse_rate_limit=101)


def test_log_config_level_validation():
    """Test log level validation."""
    # Valid levels
    for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        config = LogConfig(log_level=level)
        assert config.log_level == level

    # Case insensitive
    config = LogConfig(log_level="info")
    assert config.log_level == "INFO"

    # Invalid level
    with pytest.raises(ValidationError):
        LogConfig(log_level="INVALID")


def test_path_config_resolution():
    """Test path resolution."""
    config = PathConfig(data_dir="./data", output_dir="./outputs")
    assert config.data_dir.is_absolute()
    assert config.output_dir.is_absolute()


def test_config_integration():
    """Test full Config integration."""
    config = Config()
    assert config.api is not None
    assert config.paths is not None
    assert config.log is not None


def test_get_config_singleton():
    """Test get_config returns singleton."""
    config1 = get_config()
    config2 = get_config()
    assert config1 is config2

    # Test reload
    config3 = get_config(reload=True)
    assert config3 is not config1
