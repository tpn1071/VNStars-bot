import discord
from discord.ext import commands
from bot.config import settings


def setup_on_ready(bot: commands.Bot):
    @bot.event
    async def on_ready():  # type:ignore
        # Đổi presence/status
        await bot.change_presence(
            activity=discord.Game(name="cave"),
            status=discord.Status.online,
        )

        # await send_message_to_test_channel(bot)


# Hàm này sẽ gửi thông báo vào kênh khi bot đã sẵn sàng
async def send_message_to_test_channel(bot: commands.Bot):
    message = (
        f"Name: **{bot.user.name}**\n"  # type:ignore
        f"ID: `{bot.user.id}`\n"  # type:ignore
    )
    embed = discord.Embed(
        title="Yo mọi người!🚀 Mình vừa khởi động xong rồi đây 😎",
        description=message,
        color=discord.Color.from_str(settings.GREEN_PRIMARY_COLOR),
        timestamp=discord.utils.utcnow(),
    )

    channel_id = settings.GENERAL_TEXT_CHANNEL_ID
    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.TextChannel):
        await channel.send(embed=embed)
