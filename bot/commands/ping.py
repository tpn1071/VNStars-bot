from discord.ext import commands

from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_ping_command(bot: commands.Bot):

    @bot.command(name="hi_vnstars")
    @catch_all_errors
    @log_function_call
    async def ping(ctx: commands.Context[commands.Bot]):  # type:ignore
        await ctx.send("Hello")
