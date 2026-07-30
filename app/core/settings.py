from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsBase(BaseSettings):
    """Base class for all application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class AppSettings(SettingsBase):
    """Application-specific settings."""

    name: str = Field(alias="APP_NAME")
    env: str = Field(alias="APP_ENV")
    debug: bool = Field(alias="DEBUG")
