import discord
from discord.ext import commands
from bot.config import settings
from datetime import datetime, timezone
from typing import Dict, Any


def setup_on_member_update(bot: commands.Bot):
    @bot.event
    async def on_member_update(  # type:ignore
        before: discord.Member, after: discord.Member
    ):
        await send_message_in_pending_approval_channel(before, after)


async def send_message_in_pending_approval_channel(
    before: discord.Member, after: discord.Member
):
    before_roles = set(before.roles)
    after_roles = set(after.roles)
    added_roles = after_roles - before_roles

    lang_configs: Dict[str, Dict[str, Any]] = {
        "vi_lang": {
            "role_id": settings.VI_UNKNOWN_ROLE_ID,
            "channel_id": settings.VI_PENDING_APPROVAL_TEXT_CHANNEL_ID,
            "embed_title": "",
            "embed_description": (
                f"Xin chào! Rất vui vì bạn đã đến đây\n"
                f"Nhớ ghé qua đọc phần hướng dẫn tại đây nha\n"
                f"# {settings.VI_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH}\n"
                f"Có gì thắc mắc cứ mạnh dạn hỏi nhé!\n"
            ),
        },
        "en_lang": {
            "role_id": settings.EN_UNKNOWN_ROLE_ID,
            "channel_id": settings.EN_PENDING_APPROVAL_TEXT_CHANNEL_ID,
            "embed_title": "",
            "embed_description": (
                f"Hey, welcome aboard!\n"
                f"Take a quick look at the guide here\n"
                f"# {settings.EN_PENDING_APPROVAL_CHANNEL_MESSAGE_PATH}\n"
                f"Got any questions? Don’t hesitate to ask!\n"
            ),
        },
    }

    for role in added_roles:
        if role.id == lang_configs["vi_lang"]["role_id"]:
            channel = after.guild.get_channel(lang_configs["vi_lang"]["channel_id"])
            if channel and isinstance(channel, discord.TextChannel):
                embed = discord.Embed(
                    title=lang_configs["vi_lang"]["embed_title"],
                    description=lang_configs["vi_lang"]["embed_description"],
                    color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
                )
                embed.timestamp = datetime.now(timezone.utc)

                print(embed.to_dict())
                await channel.send(content=after.mention, embed=embed)
        elif role.id == lang_configs["en_lang"]["role_id"]:
            channel = after.guild.get_channel(lang_configs["en_lang"]["channel_id"])
            if channel and isinstance(channel, discord.TextChannel):
                embed = discord.Embed(
                    title=lang_configs["en_lang"]["embed_title"],
                    description=lang_configs["en_lang"]["embed_description"],
                    color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
                )
                embed.timestamp = datetime.now(timezone.utc)

                print(embed.to_dict())
                await channel.send(content=after.mention, embed=embed)
