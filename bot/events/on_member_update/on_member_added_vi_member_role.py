import discord
from discord.ext import commands
from bot.config import settings


async def on_member_added_vi_member_role(
    bot: commands.Bot, before: discord.Member, after: discord.Member
):
    forum = await bot.fetch_channel(settings.VI_HALL_FORUM_CHANNEL_ID)

    if not forum or not isinstance(forum, discord.ForumChannel):
        return

    # Tìm tag (giả sử tag tên "Giới thiệu")
    tags = [tag for tag in forum.available_tags if tag.id == 1374807061686255647]

    channel = await bot.fetch_channel(1377738308494299248)
    message = None
    title = None
    if channel and isinstance(channel, discord.TextChannel):
        title = await channel.fetch_message(1377741520311947304)
        message = await channel.fetch_message(1377741542424580127)

    if not message:
        return
    if not title:
        return

    embed = discord.Embed(
        title="",
        description=f"{message.content}",
    )

    embed.set_image(
        url="https://media.discordapp.net/attachments/1375008555593371738/1375008817938698250/ChatGPT_Image_May_20_2025_08_44_01_PM.png?ex=68395ac0&is=68380940&hm=00939925bba80857ed2a25b63cd421a1cbd61d3715af2faf24e88e8f7a01c813&=&format=webp&quality=lossless&width=744&height=744"
    )

    await forum.create_thread(
        name=f"{title.content}",
        content=None,
        applied_tags=tags,
        embeds=[embed],
    )
