import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

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

def run_web():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "VNStars-bot is running!"

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run_web).start()
    for cog in cogs:
        bot.load_extension(cog)
    bot.run(TOKEN)