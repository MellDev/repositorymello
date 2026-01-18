from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Server
    api_host: str = "0.0.0.0"
    api_port: int = int(os.getenv("PORT", "8000"))  # Use PORT env var from Cloud Run
    node_env: str = "development"

    # Database
    mongodb_uri: str = ""
    mongodb_db: str = "portfolio"

    # JWT
    secret_key: str = ""
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 10080

    # Google Calendar
    google_service_account_file: str = "credentials/service-account.json"
    google_calendar_id: str = ""

    # Email
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    email_from: str = ""

    # GitHub
    github_username: str = "MellDev"
    github_token: str = ""

    # OpenAI
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    max_chat_messages_per_session: int = 3

    # Gallery-dl
    download_path: str = "/tmp/downloads"

    # CORS
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:3001"]

    # Rate Limiting
    rate_limit_per_minute: int = 60

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
