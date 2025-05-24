import discord
from discord.ext import commands
from bot.config import settings

def setup_on_ready(bot: commands.Bot):
    @bot.event
    async def on_ready():   #type:ignore
        print(f"✅ Bot đã online: {bot.user}")
        # Đổi presence/status
        await bot.change_presence(activity=discord.Game(name="gái"))
        # Gửi log lên channel nếu có cấu hình
        channel_id = getattr(settings, "LOG_CHANNEL_ID", None)
        if channel_id:
            channel = bot.get_channel(channel_id)
            if channel and isinstance(channel, discord.TextChannel):
                await channel.send(f"🤖 Bot đã online: {bot.user}")
        # In thêm thông tin server
        for guild in bot.guilds:
            print(f"Đã kết nối tới server: {guild.name} (ID: {guild.id})")
