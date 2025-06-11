from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# from typing import List


class Settings(BaseSettings):
    # 1. Bot info
    BOT_TOKEN: str = Field(..., alias="BOT_TOKEN")
    BOT_PREFIX: str = Field("!", alias="BOT_PREFIX")
    OWNER_ID: int = Field(..., alias="OWNER_ID")
    DEBUG_MODE: bool = Field(False, alias="DEBUG_MODE")

    # 2. Guild / Server
    # ID của server
    GUILD_ID: str = Field(..., alias="GUILD_ID")
    # Tên của server
    GUILD_NAME: str = Field(..., alias="GUILD_NAME")

    # 3. Channel IDs
    # Ngôn ngữ - Mô tả - Loại kênh - ID
    # [🏰⭐🌐]
    GENERAL_TEXT_CHANNEL_ID: int = Field(..., alias="GENERAL_TEXT_CHANNEL_ID")
    # [🏰⭐⏳-chờ-xét-duyệt]
    VI_PENDING_APPROVAL_TEXT_CHANNEL_ID: int = Field(
        ..., alias="VI_PENDING_APPROVAL_TEXT_CHANNEL_ID"
    )
    # [🏰🌐⏳-pending-approval]
    EN_PENDING_APPROVAL_TEXT_CHANNEL_ID: int = Field(
        ..., alias="EN_PENDING_APPROVAL_TEXT_CHANNEL_ID"
    )
    # [🏰🌍]
    CHOOSE_LANGUAGE_TEXT_CHANNEL_ID: int = Field(
        ..., alias="CHOOSE_LANGUAGE_TEXT_CHANNEL_ID"
    )
    # [⭐📢-tin-tức]
    VI_NEWS_TEXT_CHANNEL_ID: int = Field(..., alias="VI_NEWS_TEXT_CHANNEL_ID")
    # [🌐📢-news]
    EN_NEWS_TEXT_CHANNEL_ID: int = Field(..., alias="EN_NEWS_TEXT_CHANNEL_ID")
    # [⭐💬-tán-gẫu]
    VI_CHAT_TEXT_CHANNEL_ID: int = Field(..., alias="VI_CHAT_TEXT_CHANNEL_ID")
    # [🌐💬-chat]
    EN_CHAT_TEXT_CHANNEL_ID: int = Field(..., alias="EN_CHAT_TEXT_CHANNEL_ID")
    # [⭐📜-sảnh]
    VI_HALL_FORUM_CHANNEL_ID: int = Field(..., alias="VI_HALL_FORUM_CHANNEL_ID")
    # [🌐📜-hall]
    EN_HALL_FORUM_CHANNEL_ID: int = Field(..., alias="EN_HALL_FORUM_CHANNEL_ID")
    # [🤖💻-bot-commands]
    BOT_COMMANDS_TEXT_CHANNEL_ID: int = Field(..., alias="BOT_COMMANDS_TEXT_CHANNEL_ID")
    # [🤖📝-bot-logs]
    BOT_LOGS_TEXT_CHANNEL_ID: int = Field(..., alias="BOT_LOGS_TEXT_CHANNEL_ID")

    # 4. Role IDs
    # Loại vai trò - ROLE - ID
    # [🧙‍♂️ Hội Trưởng / Leader]
    LEADER_ROLE_ID: int = Field(..., alias="LEADER_ROLE_ID")
    # [❔.]
    UNKNOWN_ROLE_ID: int = Field(..., alias="UNKNOWN_ROLE_ID")
    # [❔ không rõ]
    VI_UNKNOWN_ROLE_ID: int = Field(..., alias="VI_UNKNOWN_ROLE_ID")
    # [❔ unknown]
    EN_UNKNOWN_ROLE_ID: int = Field(..., alias="EN_UNKNOWN_ROLE_ID")
    # [🧝‍♂️.]
    VICE_LEADER_ROLE_ID: int = Field(..., alias="VICE_LEADER_ROLE_ID")
    # [🧝‍♂️ Hội Phó]
    VI_VICE_LEADER_ROLE_ID: int = Field(..., alias="VI_VICE_LEADER_ROLE_ID")
    # [🧝‍♂️ Vice Leader]
    EN_VICE_LEADER_ROLE_ID: int = Field(..., alias="EN_VICE_LEADER_ROLE_ID")
    # [🧍.]
    MEMBER_ROLE_ID: int = Field(..., alias="MEMBER_ROLE_ID")
    # [🧍 Hội Viên]
    VI_MEMBER_ROLE_ID: int = Field(..., alias="VI_MEMBER_ROLE_ID")
    # [🧍 Member]
    EN_MEMBER_ROLE_ID: int = Field(..., alias="EN_MEMBER_ROLE_ID")

    # 6. Các loại PATH (channel, message, image,...)
    # Ngôn ngữ - Vị trí ở - Loại liên kết - PATH
    # [🏰🌐⏳-pending-approval] - Hướng dẫn được duyệt
    EN_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH: str = Field(
        ..., alias="EN_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH"
    )
    # [🏰⭐⏳-chờ-xét-duyệt] - Hướng dẫn được duyệt
    VI_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH: str = Field(
        ..., alias="VI_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH"
    )
    # Message - [🏰🌍] - Hướng dẫn chọn ngôn ngữ
    CHOOSE_LANGUAGE_CHANNEL_MESSAGE_PATH: str = Field(
        ..., alias="CHOOSE_LANGUAGE_CHANNEL_MESSAGE_PATH"
    )

    # Màu
    GREEN_PRIMARY_COLOR: str = Field(..., alias="GREEN_PRIMARY_COLOR")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()  # type:ignore
