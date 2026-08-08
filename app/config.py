"""
centralizate configuration
Uses pydantic-settings for validated environment variables
"""

from pydantic_settings import BaseSettings
from functools import lru_cache

class Setting(BaseSettings):
  # LLM configuration
  openai_api_key: str
  primary_model: str = "gpt-4o-mini"
  fallback_model: str = "gpt-4o-mini"

  # LangSmith
  langchain_tracing_v2: bool = True
  langchain_api_key: str = ""
  langchain_project_name: str = "production-api"

  # Application
  app_anv: str = "development"
  log_level: str = "INFO"
  rate_limit: str = "20/minute"
  cache_ttl_seconds: int = 300
  max_retries: int = 3

  model_config = { "env_file": ".env", "extra": "ignore" }

  @property
  def is_production(self) -> bool:
    return self.app_anv == "production"

  @lru_cache
  def get_settings() -> Setting:
    """Cached settings instance - loaded once, reused everywhere. """
    return Setting()
