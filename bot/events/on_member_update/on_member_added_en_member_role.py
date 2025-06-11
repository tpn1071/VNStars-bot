import discord
from discord.ext import commands
from bot.config import settings
from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


@catch_all_errors
@log_function_call
async def on_member_added_en_member_role(
    bot: commands.Bot, before: discord.Member, after: discord.Member
):
    forum = await bot.fetch_channel(settings.EN_HALL_FORUM_CHANNEL_ID)

    if not forum or not isinstance(forum, discord.ForumChannel):
        return

    # Tìm tag (giả sử tag tên "Giới thiệu")
    tags = [tag for tag in forum.available_tags if tag.id == 1374806903485628517]
    channel = await bot.fetch_channel(1377738308494299248)
    message = None
    if channel and isinstance(channel, discord.TextChannel):
        message = await channel.fetch_message(1377741542424580127)

    if not message:
        return

    embed = discord.Embed(
        title="Welcom!",
        description=f"{message.content}",
    )

    embed.set_image(
        url="https://media.discordapp.net/attachments/1375008555593371738/1375008818370576474/English_ChatGPT_Image_May_20_2025_08_56_56_PM.png?ex=68395ac0&is=68380940&hm=b2b958722bad4ba1cb6f485a8a92417dbf13f63808d0c79d6fdd6d497c290897&=&format=webp&quality=lossless&width=744&height=744"
    )

    await forum.create_thread(
        name=f"Welcom {after.display_name}",
        content=None,
        applied_tags=tags,
        embeds=[embed],
    )
