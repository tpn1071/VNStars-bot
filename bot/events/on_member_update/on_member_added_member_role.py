import discord
from bot.config import settings

from bot.utils.decorators import try_catch_async


@try_catch_async
async def on_member_added_member_role(before: discord.Member, after: discord.Member):
    await after.send("ok")
