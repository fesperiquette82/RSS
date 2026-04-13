from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "RSS API"
    api_prefix: str = "/api/v1"
    mongodb_url: str = "mongodb://localhost:27017"
    db_name: str = "rss_db"
    cors_origins: str = "http://localhost:8081"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
