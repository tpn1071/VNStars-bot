import discord
from discord.ext import commands
from bot.config import settings  # settings.GREETING_CHANNEL_ID


def is_vietnamese(text: str) -> bool:
    vietnamese_chars = (
        "ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    )
    text_lower = text.lower()
    return any(c in vietnamese_chars for c in text_lower)


def is_english(text: str) -> bool:
    # Kiểm tra text chỉ gồm ký tự tiếng Anh (a-z) và space
    return all(c.isalpha() or c.isspace() for c in text) and not is_vietnamese(text)


def setup_on_presence_update(bot: commands.Bot):
    @bot.event
    async def on_presence_update(  # type:ignore
        before: discord.Member, after: discord.Member
    ):
        if (
            before.status == discord.Status.offline
            and after.status == discord.Status.online
        ):
            channel_ids = settings.GREETING_CHANNEL_IDS
            if not channel_ids:
                return

            for channel_id in channel_ids:
                channel = after.guild.get_channel(channel_id)
                if channel and isinstance(channel, discord.TextChannel):
                    await channel.send(f"👋 Hi {after.mention}!")
