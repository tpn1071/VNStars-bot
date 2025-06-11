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
        intents = intents or self.default_intents()
        super().__init__(command_prefix=command_prefix, intents=intents, **kwargs)

    @staticmethod
    def default_intents() -> discord.Intents:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.presences = True
        intents.guild_reactions = True
        intents.guilds = True
        return intents

    async def setup_hook(self):
        # Đồng bộ slash commands (toàn cầu)
        await self.tree.sync()
