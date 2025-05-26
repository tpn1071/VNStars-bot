from typing import Any, Dict
import discord
from discord.ext import commands
from bot.config import settings


def setup_on_ready(bot: commands.Bot):
    @bot.event
    async def on_ready():  # type:ignore
        # Đổi presence/status
        await bot.change_presence(
            activity=discord.Game(name="cave"),
            status=discord.Status.online,
        )

        await send_message_to_test_channel(bot)

        await send_message_to_choose_language_channel(bot)


# Hàm này sẽ gửi thông báo vào kênh khi bot đã sẵn sàng
async def send_message_to_test_channel(bot: commands.Bot):
    message = (
        f"Name: **{bot.user.name}**\n"  # type:ignore
        f"ID: `{bot.user.id}`\n"  # type:ignore
    )
    embed = discord.Embed(
        title="Yo mọi người!🚀 Mình vừa khởi động xong rồi đây 😎",
        description=message,
        color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
        timestamp=discord.utils.utcnow(),
    )

    channel_id = settings.GENERAL_TEXT_CHANNEL_ID
    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.TextChannel):
        await channel.send(embed=embed)

        # log check run
        print(f"send_message: {channel.name} ({channel.id})")


async def send_message_to_choose_language_channel(bot: commands.Bot):
    # log để xem hàm chạy chưa
    print("send_message_to_choose_language_channel: Bot is ready to send messages.")

    async def send_message(
        channel: discord.TextChannel, language_configs: Dict[str, Any]
    ):
        # log để xem hàm chạy chưa
        print(f"send_message: {channel.name} ({channel.id})")
        embed = discord.Embed(
            title=language_configs["title"],
            description=language_configs["embed_description"],
            color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
            timestamp=discord.utils.utcnow(),
        )

        await channel.send(embed=embed)

    channel_id = settings.CHOOSE_LANGUAGE_TEXT_CHANNEL_ID
    languages_configs: Dict[str, Dict[str, Any]] = {
        "vi_lang": {
            "role_id": settings.VI_UNKNOWN_ROLE_ID,
            "channel_id": channel_id,
            "title": "",
            "embed_description": (
                f"Bạn dùng ngôn ngữ nào, Tiếng Việt hay Tiếng Anh?\n"
                f"Tiếng Việt — Thả emoji ⭐ để nhận role Tiếng Việt\n"
                f"Ngại gì không thả! Cứ thả cả hai nếu thích 😄!\n"
            ),
        },
        "en_lang": {
            "role_id": settings.EN_UNKNOWN_ROLE_ID,
            "channel_id": channel_id,
            "title": "",
            "embed_description": (
                f"What language do you use, English or Vietnamese?\n"
                f"English — React 🌐 to get English role\n"
                f"Don't be shy, drop that emoji! Why not both? React with both if you like 😄!\n"
            ),
        },
    }

    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.TextChannel):
        # Gửi tin nhắn vào kênh chọn ngôn ngữ
        await send_message(channel, languages_configs["vi_lang"])
        await send_message(channel, languages_configs["en_lang"])
        await channel.send(f"# | 🌐 | ⭐ |")
