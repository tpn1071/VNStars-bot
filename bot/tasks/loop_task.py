from discord.ext import tasks
from discord import TextChannel
from discord import TextChannel
from discord.ext import commands
from bot.config import settings
from discord.ext import tasks
import datetime


def start_background_tasks(bot: commands.Bot):

    # Hàm này sẽ gọi lên vào lúc 6 giờ sáng, 12 giờ trưa, 18 giờ tối
    @tasks.loop(
        time=[
            datetime.time(hour=6, minute=0),
            datetime.time(hour=12, minute=0),
            datetime.time(hour=18, minute=0),
        ]
    )
    async def send_loop_message():  # type:ignore
        now = datetime.datetime.now().hour
        greeting = ""

        if now == 6:
            greeting = (
                "🌅 **Chào buổi sáng!** Chúc bạn một ngày mới tràn đầy năng lượng ☀️"
            )
        elif now == 12:
            greeting = "🌞 **Chúc buổi trưa vui vẻ!** Nhớ nghỉ ngơi nhé 🍱"
        elif now == 18:
            greeting = "🌙 **Chào buổi tối!** Thư giãn sau một ngày dài nào 🌃"

        channel = bot.get_channel(settings.GENERAL_TEXT_CHANNEL_ID)
        if channel and isinstance(channel, TextChannel):
            await channel.send(f"@everyone\n")
            await channel.send(greeting)

    send_loop_message.start()
