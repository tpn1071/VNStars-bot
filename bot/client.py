import discord
from discord.ext import commands
from typing import Any
from bot.config import settings


class CustomBot(commands.Bot):
    def __init__(
        self,
        command_prefix: str = settings.BOT_PREFIX,
        intents: discord.Intents | None = None,
        **kwargs: Any
    ):
        if intents is None:
            intents = discord.Intents.default()
            intents.message_content = True
            intents.members = True
            intents.presences = True
        super().__init__(command_prefix=command_prefix, intents=intents, **kwargs)
