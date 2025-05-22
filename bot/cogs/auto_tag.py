class AutoTagCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        added_roles = [role for role in after.roles if role not in before.roles]

        for role in added_roles:
            if role.id == ROLE_UNKNOWN_ID:
                channel1 = after.guild.get_channel(CHANNEL_PENDING_ID)
                if channel1:
                    await channel1.send(
                        f"Welcome {after.mention}! Please read the instructions here: {UNKNOWN_GUIDE_LINK}"
                    )

            elif role.id == ROLE_KHONG_RO_ID:
                channel2 = after.guild.get_channel(CHANNEL_CHO_DUYET_ID)
                if channel2:
                    await channel2.send(
                        f"Chào mừng {after.mention}! Vui lòng đọc hướng dẫn tại đây: {KHONG_RO_GUIDE_LINK}"
                    )

def setup(bot):
    bot.add_cog(AutoTagCog(bot))