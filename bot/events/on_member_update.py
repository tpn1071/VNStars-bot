import discord
from discord.ext import commands
from bot.config import settings
from typing import Dict, Any


def setup_on_member_update(bot: commands.Bot):
    @bot.event
    async def on_member_update(  # type:ignore
        before: discord.Member, after: discord.Member
    ):
        await on_member_added_unknown_role(before, after)
        await on_member_added_vi_and_en_unknown_role(before, after)


# Hàm này sẽ gửi tin nhắn vào kênh chung khi thành viên có vai trò "Unknown" mới
async def on_member_added_unknown_role(before: discord.Member, after: discord.Member):

    async def send_message_to_general_channel(
        channel: discord.TextChannel, language_configs: Dict[str, Any]
    ):
        embed = discord.Embed(
            title=language_configs["embed_title"],
            description=language_configs["embed_description"],
            color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
            timestamp=discord.utils.utcnow(),
        )

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

    channel = after.guild.get_channel(channel_id)
    if channel and isinstance(channel, discord.TextChannel):
        await channel.send(after.mention)
        await send_message_to_general_channel(channel, languages_configs["vi_lang"])
        await send_message_to_general_channel(channel, languages_configs["en_lang"])
        await channel.send(f"# {settings.CHOOSE_LANGUAGE_CHANNEL_MESSAGE_PATH}")

    # log check run
    print(f"on_member_update: {before.name} -> {after.name} ({after.id})")


# Hàm này sẽ gửi tin nhắn vào kênh chờ phê duyệt khi thành viên có vai trò mới
async def on_member_added_vi_and_en_unknown_role(
    before: discord.Member, after: discord.Member
):

    async def send_message_to_pending_approval_channel(
        channel: discord.TextChannel, language_configs: Dict[str, Any]
    ):
        embed = discord.Embed(
            title=language_configs["embed_title"],
            description=language_configs["embed_description"],
            color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
            timestamp=discord.utils.utcnow(),
        )

        print(embed.to_dict())
        await channel.send(content=after.mention)
        await channel.send(embed=embed)

    before_roles = set(before.roles)
    after_roles = set(after.roles)
    added_roles = after_roles - before_roles

    languages_configs: Dict[str, Dict[str, Any]] = {
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
        if role.id == languages_configs["vi_lang"]["role_id"]:
            channel = after.guild.get_channel(
                languages_configs["vi_lang"]["channel_id"]
            )
            if channel and isinstance(channel, discord.TextChannel):
                await send_message_to_pending_approval_channel(
                    channel, languages_configs["vi_lang"]
                )

        elif role.id == languages_configs["en_lang"]["role_id"]:
            channel = after.guild.get_channel(
                languages_configs["en_lang"]["channel_id"]
            )
            if channel and isinstance(channel, discord.TextChannel):
                await send_message_to_pending_approval_channel(
                    channel, languages_configs["en_lang"]
                )
