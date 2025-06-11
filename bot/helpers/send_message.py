import discord
from typing import Dict, Any
from bot.config import settings


async def send_message(channel: discord.TextChannel, configs: Dict[str, Any]):
    embed = discord.Embed()
    embed.title = configs["embed"]["title"]
    embed.description = configs["embed"]["description"]
    embed.color = discord.Color.from_str(settings.GREEN_PRIMARY_COLOR)
    await channel.send(embed=embed)
