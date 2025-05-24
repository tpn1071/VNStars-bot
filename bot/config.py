from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    DISCORD_TOKEN: str = ""  # Default value, or remove if you want to require it from .env

    # Thêm các biến cấu hình khác nếu cần
    ROLE_UNKNOWN_ID: int = 0  # Provide a default value or set via .env
    ROLE_KHONG_RO_ID: int = 0  # Provide a default value or set via .env
    CHANNEL_PENDING_ID: int = 0  # Provide a default value or set via .env
    CHANNEL_CHO_DUYET_ID: int = 0  # Provide a default value or set via .env
    UNKNOWN_GUIDE_LINK: str = ""  # Provide a default value or set via .env
    KHONG_RO_GUIDE_LINK: str = ""  # Provide a default value or set via .env
    LOOP_CHANNEL_ID: int = 0  # Provide a default value or set via .env
    ANOTHER_CHANNEL_ID: int = 0  # Provide a default value or set via .env
    GREETING_CHANNEL_IDS: List[int] = []  # Provide a default value or set via .env

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
