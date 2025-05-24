from discord.ext import tasks
from discord.ext.commands import Bot    # type: ignore
from discord import TextChannel
from bot.config import settings

def start_background_tasks(bot: Bot):
    @tasks.loop(seconds=60)
    async def send_loop_message():
        channel = bot.get_channel(settings.LOOP_CHANNEL_ID)
        if channel and isinstance(channel, TextChannel):
            await channel.send("🕒 Đây là tin nhắn định kỳ mỗi 60s.")

    @tasks.loop(minutes=10)
    async def another_background_task():
        # Ví dụ: gửi thông báo khác mỗi 10 phút
        channel = bot.get_channel(settings.ANOTHER_CHANNEL_ID)
        if channel and isinstance(channel, TextChannel):
            await channel.send("🔔 Đây là thông báo mỗi 10 phút.")

    send_loop_message.start()
    another_background_task.start()