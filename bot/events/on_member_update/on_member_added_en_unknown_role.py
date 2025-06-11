import discord
from bot.config import settings
from typing import Dict, Any
from bot.helpers.send_message import send_message
from discord.ext import commands


configs: Dict[str, Any] = {
    "pending_approval": {
        "english": {
            "channel_id": settings.EN_PENDING_APPROVAL_TEXT_CHANNEL_ID,
            "embed": {
                "title": "",
                "description": (
                    f"Hey, welcome aboard!\n"
                    f"Take a quick look at the guide here\n"
                    f"# {settings.EN_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH}\n"
                    f"Got any questions? Don’t hesitate to ask!\n"
                ),
            },
        },
    }
}


async def on_member_added_en_unknown_role(
    bot: commands.Bot, before: discord.Member, after: discord.Member
):
    channel = after.guild.get_channel(
        configs["pending_approval"]["english"]["channel_id"]
    )
    if channel and isinstance(channel, discord.TextChannel):
        await send_message(channel, configs["pending_approval"]["english"])
