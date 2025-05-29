import discord
from discord.ext import commands


def setup_on_reaction_add(bot: commands.Bot):
    @bot.event
    async def on_reaction_add(reaction: discord.Reaction, user: discord.User):  # type: ignore
        print(" ff")
