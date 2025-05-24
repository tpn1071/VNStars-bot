import discord
from discord.ext import commands
from bot.config import settings


def setup_on_member_update(bot: commands.Bot):
    @bot.event
    async def on_member_update(  # type:ignore
        before: discord.Member, after: discord.Member
    ):
        before_roles = set(before.roles)
        after_roles = set(after.roles)
        # Nếu role được thêm
        added_roles = after_roles - before_roles

        for role in added_roles:
            if role.id == settings.ROLE_UNKNOWN_ID:
                channel = after.guild.get_channel(settings.CHANNEL_PENDING_ID)
                if channel and isinstance(channel, discord.TextChannel):
                    await channel.send(
                        f"Chào mừng {after.mention}! Vui lòng đọc hướng dẫn tại đây: {settings.UNKNOWN_GUIDE_LINK}"
                    )
            elif role.id == settings.ROLE_KHONG_RO_ID:
                channel = after.guild.get_channel(settings.CHANNEL_CHO_DUYET_ID)
                if channel and isinstance(channel, discord.TextChannel):
                    await channel.send(
                        f"Chào mừng {after.mention}! Vui lòng đọc hướng dẫn tại đây: {settings.KHONG_RO_GUIDE_LINK}"
                    )
