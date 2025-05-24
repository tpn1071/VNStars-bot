from discord.ext import commands
from typing import Any

def setup_ping_command(bot: commands.Bot):
    @bot.command()
    async def ping(ctx: commands.Context[Any]): # type:ignore
        await ctx.send("🏓 Pong!")
