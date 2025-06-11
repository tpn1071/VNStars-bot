import discord
from bot.config import settings
from typing import Dict, Any
from discord.ext import commands

from bot.helpers.send_message import send_message


configs: Dict[str, Any] = {
    "pending_approval": {
        "channel_id": "",
        "vietnamese": {
            "channel_id": settings.VI_PENDING_APPROVAL_TEXT_CHANNEL_ID,
            "embed": {
                "title": "",
                "description": (
                    f"Xin chào! Rất vui vì bạn đã đến đây\n"
                    f"Nhớ ghé qua đọc phần hướng dẫn tại đây nha\n"
                    f"# {settings.VI_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH}\n"
                    f"Có gì thắc mắc cứ mạnh dạn hỏi nhé!\n"
                ),
            },
        },
    }
}


async def on_member_added_vi_unknown_role(
    bot: commands.Bot, before: discord.Member, after: discord.Member
):
    channel = after.guild.get_channel(
        configs["pending_approval"]["vietnamese"]["channel_id"]
    )
    if channel and isinstance(channel, discord.TextChannel):
        await send_message(channel, configs["pending_approval"]["vietnamese"])
