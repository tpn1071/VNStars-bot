import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

# ===== TẠO WEB SERVER GIỮ BOT SỐNG =====
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# ===== TẢI BIẾN MÔI TRƯỜNG =====
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # Lấy token từ biến môi trường

# ===== CẤU HÌNH ROLE & KÊNH =====
ROLE_UNKNOWN_ID = 1373737799093715014
ROLE_KHONG_RO_ID = 1373741381369069568

CHANNEL_PENDING_ID = 1373712993761886400
CHANNEL_CHO_DUYET_ID = 1373593067667329034

UNKNOWN_GUIDE_LINK = "https://discord.com/channels/1373260056530911296/1373712993761886400/1373779221666594876"
KHONG_RO_GUIDE_LINK = "https://discord.com/channels/1373260056530911296/1373593067667329034/1373778884008611919"

# ===== KHỞI TẠO BOT =====
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập với tên {bot.user}")

# ===== CLONE ROLE GUI =====
class RoleNameModal(discord.ui.Modal, title="Nhập tên role mới"):
    def __init__(self, role: discord.Role):
        super().__init__()
        self.role = role
        self.new_name_input = discord.ui.TextInput(label="Tên role mới", placeholder="VD: Mod 2", required=False)
        self.add_item(self.new_name_input)

    async def on_submit(self, interaction: discord.Interaction):
        new_name = self.new_name_input.value or f"{self.role.name} Clone"
        try:
            cloned = await interaction.guild.create_role(
                name=new_name,
                permissions=self.role.permissions,
                colour=self.role.colour,
                hoist=self.role.hoist,
                mentionable=self.role.mentionable,
                reason=f"Cloned from {self.role.name} by {interaction.user}"
            )
            await interaction.response.send_message(f"✅ Đã clone role **{self.role.name}** thành **{cloned.name}**", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ Bot không đủ quyền để clone role này.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Lỗi: {e}", ephemeral=True)

class RoleDropdown(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=60)
        self.add_item(RoleSelect(roles))

class RoleSelect(discord.ui.Select):
    def __init__(self, roles):
        options = [
            discord.SelectOption(label=role.name, value=str(role.id))
            for role in roles
        ]
        super().__init__(placeholder="Chọn role cần clone", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        role_id = int(self.values[0])
        role = discord.utils.get(interaction.guild.roles, id=role_id)
        if role:
            await interaction.response.send_modal(RoleNameModal(role))

@bot.command()
@commands.has_permissions(manage_roles=True)
async def clonerolegui(ctx):
    roles = [
        r for r in ctx.guild.roles
        if r != ctx.guild.default_role and r.position < ctx.guild.me.top_role.position
    ]
    if not roles:
        await ctx.send("❌ Không có role nào để clone.")
        return

    await ctx.send("🧩 Chọn role để clone:", view=RoleDropdown(roles))

# ===== TỰ ĐỘNG GỬI THÔNG BÁO KHI GÁN ROLE =====
@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
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

# ===== CHẠY WEB SERVER VÀ BOT =====
keep_alive()
bot.run(TOKEN)
