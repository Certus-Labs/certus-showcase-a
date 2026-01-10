"""Environment configuration and validation.

This module provides typed configuration loading from environment variables.
Inspired by the lakehouse_technical_challenge pattern.
"""

from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class APIConfig(BaseSettings):
    """API Adresse configuration."""

    api_adresse_base_url: str = Field(
        default="https://api-adresse.data.gouv.fr",
        description="Base URL for API Adresse",
    )
    api_adresse_rate_limit: int = Field(
        default=50,
        description="Max requests per second",
        ge=1,
        le=100,
    )

    model_config = SettingsConfigDict(env_file=".secrets.env", extra="ignore")


class PathConfig(BaseSettings):
    """Data paths configuration."""

    data_dir: Path = Field(
        default=Path("./data"),
        description="Root data directory",
    )
    output_dir: Path = Field(
        default=Path("./outputs"),
        description="Output directory for results",
    )

    @field_validator("data_dir", "output_dir", mode="before")
    @classmethod
    def resolve_path(cls, v: str | Path) -> Path:
        """Resolve path to absolute."""
        return Path(v).resolve()

    model_config = SettingsConfigDict(env_file=".secrets.env", extra="ignore")


class LogConfig(BaseSettings):
    """Logging configuration."""

    log_level: str = Field(
        default="INFO",
        description="Logging level",
    )

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level."""
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        v_upper = v.upper()
        if v_upper not in valid_levels:
            raise ValueError(f"Invalid log level: {v}. Must be one of {valid_levels}")
        return v_upper

    model_config = SettingsConfigDict(env_file=".secrets.env", extra="ignore")


class Config:
    """Central configuration holder.

    Loads and validates all configuration from environment.
    """

    def __init__(self, env_file: str | None = None):
        """Initialize configuration.

        Args:
            env_file: Optional path to .env file (defaults to .secrets.env)
        """
        self.api = APIConfig(_env_file=env_file or ".secrets.env")
        self.paths = PathConfig(_env_file=env_file or ".secrets.env")
        self.log = LogConfig(_env_file=env_file or ".secrets.env")

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"Config(\n"
            f"  api_base_url={self.api.api_adresse_base_url},\n"
            f"  data_dir={self.paths.data_dir},\n"
            f"  log_level={self.log.log_level}\n"
            f")"
        )


# Singleton instance
_config: Config | None = None


def get_config(reload: bool = False) -> Config:
    """Get configuration singleton.

    Args:
        reload: Force reload from environment

    Returns:
        Config instance
    """
    global _config
    if _config is None or reload:
        _config = Config()
    return _config
