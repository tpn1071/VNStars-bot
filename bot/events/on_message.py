import discord
from bot.config import settings
from discord.ext import commands


def setup_on_message(bot: commands.Bot):
    @bot.event
    async def on_message(message: discord.Message):  # type:ignore
        # Kiểm tra nếu là tin nhắn của bot
        if not message.author.bot:
            return

        # Kiểm tra nếu là tin nhắn trong kênh chọn ngôn ngữ
        channel_id = settings.CHOOSE_LANGUAGE_TEXT_CHANNEL_ID
        if message.channel.id != channel_id:
            return
        if message.embeds[0].description != "\u200b":
            return

        # Xử lý tin nhắn ở đây
        await message.add_reaction("🌐")
        await message.add_reaction("⭐")
