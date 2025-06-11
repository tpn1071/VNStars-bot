import discord
from discord.ext import commands
from bot.config import settings
from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_on_member_join(bot: commands.Bot):

    @bot.event
    @catch_all_errors
    @log_function_call
    async def on_member_join(member: discord.Member):  # type:ignore
        await add_unknown_role(member)


# Hàm này sẽ thêm vai trò "Unknown" cho thành viên mới tham gia
async def add_unknown_role(member: discord.Member):
    role_id = settings.UNKNOWN_ROLE_ID
    role = member.guild.get_role(role_id)
    if role:
        await member.add_roles(role)
