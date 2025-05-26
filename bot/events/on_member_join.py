import discord
from discord.ext import commands
from bot.config import settings
from typing import Dict, Any
from datetime import datetime, timezone


def setup_on_member_join(bot: commands.Bot):
    @bot.event
    async def on_member_join(member: discord.Member):  # type:ignore
        await add_unknown_role_on_member_join(member)
        await send_message_to_general_channel(member)

        # log check run
        print(f"on_member_join: {member.name} ({member.id})")


async def add_unknown_role_on_member_join(member: discord.Member):
    role_id = settings.UNKNOWN_ROLE_ID
    role = member.guild.get_role(role_id)
    if role:
        try:
            await member.add_roles(role)
            # log để xem hàm chạy chưa
            print(f"Added role {role.name} to {member.name}")
        except discord.Forbidden:
            print(f"Failed to add role {role.name} to {member.name}: Forbidden")
        except discord.HTTPException as e:
            print(f"Failed to add role {role.name} to {member.name}: {e}")
    else:
        print(f"Role with ID {role_id} not found in guild {member.guild.name}")

    # log check run
    print(f"add_unknown_role_on_member_join: {member.name} ({member.id})")


async def send_message_to_general_channel(member: discord.Member):
    async def send_message(
        channel: discord.TextChannel, language_configs: Dict[str, Any]
    ):
        embed = discord.Embed(
            title=language_configs["embed_title"],
            description=language_configs["embed_description"],
            color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
        )
        embed.timestamp = datetime.now(timezone.utc)

        print(embed.to_dict())
        await channel.send(embed=embed)

        # log check run
        print(f"send_message: {channel.name} ({channel.id})")

    role_id = settings.UNKNOWN_ROLE_ID
    channel_id = settings.GENERAL_TEXT_CHANNEL_ID

    languages_configs: Dict[str, Dict[str, Any]] = {
        "vi_lang": {
            "role_id": role_id,
            "channel_id": channel_id,
            "embed_title": "",
            "embed_description": (
                f"Chào mừng bạn đến với Cổng vào của Hội VNStars!\n"
                f"Hãy chọn ngôn ngữ của bạn để tiếp tục\n"
            ),
        },
        "en_lang": {
            "role_id": role_id,
            "channel_id": channel_id,
            "embed_title": "",
            "embed_description": (
                f"Welcome to the VNStars Guild Entrance!\n"
                f"Please choose your language to proceed\n"
            ),
        },
    }

    channel = member.guild.get_channel(channel_id)
    if channel and isinstance(channel, discord.TextChannel):
        await channel.send(member.mention)
        await send_message(channel, languages_configs["vi_lang"])
        await send_message(channel, languages_configs["en_lang"])
        await channel.send(f"# {settings.CHOOSE_LANGUAGE_CHANNEL_MESSAGE_PATH}")

    # log check run
    print(f"send_message_to_general_channel: {member.name} ({member.id})")
