import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập với tên {bot.user}")

# Load cogs
cogs = [
    "cogs.role_clone",
    "cogs.auto_tag",
    "cogs.vns",
    "cogs.help_suggest",
]

if __name__ == "__main__":
    for cog in cogs:
        bot.load_extension(cog)

bot.run(TOKEN)