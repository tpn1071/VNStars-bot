import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from threading import Thread

# Thêm Flask để mở port cho Render
from flask import Flask

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("❌ DISCORD_TOKEN không tồn tại trong biến môi trường!")
    exit(1)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập với tên {bot.user}")

# Load cogs
cogs = [
    "cogs.role_clone",
    "cogs.auto_tag"
]

def run_web():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "VNStars-bot is running!"

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Chạy web server trên thread riêng
    Thread(target=run_web).start()

    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"✅ Đã load cog: {cog}")
        except Exception as e:
            print(f"❌ Lỗi khi load cog {cog}: {e}")

    bot.run(TOKEN)