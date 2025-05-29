import discord
from discord.ext import commands


def setup_on_presence_update(bot: commands.Bot):
    @bot.event
    async def on_presence_update(before: discord.Member, after: discord.Member):  # type: ignore
        # log check run
        print("heh")
