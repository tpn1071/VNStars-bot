import discord
from discord.ext import commands
from bot.config import settings


def setup_on_member_join(bot: commands.Bot):
    @bot.event
    async def on_member_join(member: discord.Member):  # type:ignore
        await add_unknown_role(member)


# Hàm này sẽ thêm vai trò "Unknown" cho thành viên mới tham gia
async def add_unknown_role(member: discord.Member):
    role_id = settings.UNKNOWN_ROLE_ID
    role = member.guild.get_role(role_id)
    if role:
        await member.add_roles(role)
