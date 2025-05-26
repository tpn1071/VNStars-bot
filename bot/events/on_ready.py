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

        # Gửi thông báo đã sẵn sàng
        await send_message_ready_on_channel(bot)


async def send_message_ready_on_channel(bot: commands.Bot):
    message = (
        f"Name: **{bot.user.name}**\n"  # type:ignore
        f"ID: `{bot.user.id}`\n"  # type:ignore
    )
    embed = discord.Embed(
        title="Yo mọi người!🚀 Mình vừa khởi động xong rồi đây 😎",
        description=message,
        color=discord.Color.from_str("#5865f2"),
    )

    channel_id = settings.TEST_CHANNEL_ID
    channel = bot.get_channel(channel_id)
    if channel and isinstance(channel, discord.TextChannel):
        print(embed.to_dict())
        await channel.send(embed=embed)
