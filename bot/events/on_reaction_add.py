import discord
from discord.ext import commands

from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_on_reaction_add(bot: commands.Bot):

    @bot.event
    @catch_all_errors
    @log_function_call
    async def on_reaction_add(reaction: discord.Reaction, user: discord.User):  # type: ignore
        print("on_reaction_add")
