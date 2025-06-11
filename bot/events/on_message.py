import discord
from bot.config import settings
from discord.ext import commands

from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_on_message(bot: commands.Bot):

    @bot.event
    @catch_all_errors
    @log_function_call
    async def on_message(message: discord.Message):  # type:ignore
        # Kiểm tra nếu là tin nhắn của bot
        if message.author.bot:

            # Kiểm tra nếu là tin nhắn trong kênh chọn ngôn ngữ
            channel_id = settings.CHOOSE_LANGUAGE_TEXT_CHANNEL_ID
            if message.channel.id != channel_id:
                return
            if message.embeds[0].description != "\u200b":
                return

            # Xử lý tin nhắn ở đây
            await message.add_reaction("🌐")
            await message.add_reaction("⭐")

        # Bắt buộc phải gọi dòng này nếu bạn override on_message.
        # Nếu không, bot sẽ không xử lý được các lệnh như !ping, !help, v.v.
        await process_commands(bot, message)


async def process_commands(bot: commands.Bot, message: discord.Message):
    await bot.process_commands(message)
