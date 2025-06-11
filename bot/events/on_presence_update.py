import discord
from discord.ext import commands

from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_on_presence_update(bot: commands.Bot):

    @bot.event
    @catch_all_errors
    @log_function_call
    async def on_presence_update(before: discord.Member, after: discord.Member):  # type: ignore
        # log check run
        print("on_presence_update")
