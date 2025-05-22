# filepath: d:\Project\DiscordBot\VNStars-bot\bot\config.py

ROLE_UNKNOWN_ID = 1373737799093715014  # Role "Member" → unknown
ROLE_KHONG_RO_ID = 1373741381369069568  # Role "Hội Viên" → không rõ

CHANNEL_PENDING_ID = 1373712993761886400  # ID của kênh gửi thông báo
CHANNEL_CHO_DUYET_ID = 1373593067667329034  # ID của kênh gửi thông báo

UNKNOWN_GUIDE_LINK = "https://discord.com/channels/1373260056530911296/1373712993761886400/1373779221666594876"
KHONG_RO_GUIDE_LINK = "https://discord.com/channels/1373260056530911296/1373593067667329034/1373778884008611919"

def get_role_ids():
    return {
        "unknown": ROLE_UNKNOWN_ID,
        "khong_ro": ROLE_KHONG_RO_ID
    }

def get_channel_ids():
    return {
        "pending": CHANNEL_PENDING_ID,
        "cho_duyet": CHANNEL_CHO_DUYET_ID
    }

def get_guide_links():
    return {
        "unknown": UNKNOWN_GUIDE_LINK,
        "khong_ro": KHONG_RO_GUIDE_LINK
    }