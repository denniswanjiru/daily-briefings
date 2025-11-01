"""
Application configuration management.
Loads environment variables and provides settings throughout the app.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # App Settings
    app_name: str = "Daily Briefings"
    app_version: str = "0.1.0"
    debug: bool = False

    # API Settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # LLM Provider Settings
    # TODO: Configure your preferred LLM provider
    llm_provider: str = "openai"  # Options: openai, anthropic, etc.
    llm_model: str = "gpt-4"
    llm_temperature: float = 0.7

    # API Keys
    # TODO: Add API keys for your LLM provider
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None

    # Calendar Integration
    # TODO: Add calendar service credentials (Google Calendar, Outlook, etc.)
    calendar_api_key: Optional[str] = None

    # Database / Storage (if needed)
    # TODO: Configure database connection if persisting user data
    database_url: Optional[str] = None

    # User Memory Settings
    memory_max_tokens: int = 2000
    memory_ttl_hours: int = 24


# Global settings instance
settings = Settings()
