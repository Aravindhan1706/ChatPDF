from app.core.settings import AppSettings


class Settings:
    """Application configuration."""

    def __init__(self) -> None:
        self.app = AppSettings()


settings = Settings()
