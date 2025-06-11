import discord
from bot.config import settings
from typing import Dict, Any
from discord.ext import commands
from bot.helpers.send_message import send_message

general_channel_id = settings.GENERAL_TEXT_CHANNEL_ID
choose_language_channel_id = settings.CHOOSE_LANGUAGE_TEXT_CHANNEL_ID
configs: Dict[str, Any] = {
    "welcome": {
        "channel_id": general_channel_id,
        "vietnamese": {
            "channel_id": general_channel_id,
            "embed": {
                "title": "",
                "description": (
                    f"Chào mừng bạn đến với Cổng vào của Hội VNStars!\n"
                    f"Hãy chọn ngôn ngữ của bạn để tiếp tục\n"
                ),
            },
        },
        "english": {
            "channel_id": general_channel_id,
            "embed": {
                "title": "",
                "description": (
                    f"Welcome to the VNStars Guild Entrance!\n"
                    f"Please choose your language to proceed\n"
                ),
            },
        },
    },
    "choose_language": {
        "channel_id": choose_language_channel_id,
        "vietnamese": {
            "channel_id": choose_language_channel_id,
            "embed": {
                "title": "",
                "description": (
                    f"⭐ Bạn dùng ngôn ngữ nào, Tiếng Việt hay Tiếng Anh?\n"
                    f"⭐ Tiếng Việt — Thả emoji ⭐ để nhận role Tiếng Việt\n"
                    f"⭐ Ngại gì không thả! Cứ thả cả hai nếu thích 😄!\n"
                ),
            },
        },
        "english": {
            "channel_id": choose_language_channel_id,
            "embed": {
                "title": "",
                "description": (
                    f"🌐 What language do you use, English or Vietnamese?\n"
                    f"🌐 English — React 🌐 to get English role\n"
                    f"🌐 Don't be shy, drop that emoji! Why not both? React with both if you like 😄!\n"
                ),
            },
        },
    },
}


async def on_member_added_unknown_role(
    bot: commands.Bot, before: discord.Member, after: discord.Member
):
    await welcome(after, configs["welcome"])
    # await choose_language(after, configs["choose_language"])


async def welcome(member: discord.Member, configs: Dict[str, Any]):
    general_channel = member.guild.get_channel(configs["channel_id"])
    if general_channel and isinstance(general_channel, discord.TextChannel):
        await general_channel.send(member.mention)
        await send_message(general_channel, configs["vietnamese"])
        await send_message(general_channel, configs["english"])
        await general_channel.send(f"#{settings.CHOOSE_LANGUAGE_CHANNEL_MESSAGE_PATH}")


async def choose_language(member: discord.Member, configs: Dict[str, Any]):
    choose_language_channel = member.guild.get_channel(configs["channel_id"])
    if choose_language_channel and isinstance(
        choose_language_channel, discord.TextChannel
    ):
        await choose_language_channel.send(member.mention)
        await send_message(choose_language_channel, configs["vietnamese"])
        await send_message(choose_language_channel, configs["english"])
        embed = discord.Embed(
            description="\u200b",
            color=discord.Color.from_str("#000000"),
            timestamp=discord.utils.utcnow(),
        )
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        embed.set_author(name=str(member), icon_url=avatar_url)

        await choose_language_channel.send(embed=embed)
