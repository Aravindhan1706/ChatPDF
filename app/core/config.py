from app.core.settings import AppSettings, ModelSettings


class Settings:
    """Application configuration."""

    def __init__(self) -> None:
        self.app = AppSettings()
        self.models = ModelSettings()


settings = Settings()
