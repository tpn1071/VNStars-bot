import discord
from bot.config import settings


async def on_member_added_member_role(before: discord.Member, after: discord.Member):
    await after.send("ok")
