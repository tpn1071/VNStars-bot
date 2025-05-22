def log_message(message: str) -> None:
    print(f"[LOG] {message}")

def format_user_mention(user) -> str:
    return f"{user.mention} ({user.name})"

def handle_error(error: Exception) -> None:
    log_message(f"Error occurred: {error}")

def is_valid_channel(channel) -> bool:
    return channel is not None and channel.permissions_for(channel.guild.me).send_messages

def get_role_by_id(guild, role_id) -> str:
    return discord.utils.get(guild.roles, id=role_id)