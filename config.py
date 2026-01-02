# ============================================================
#Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("API_ID", 20815998))
API_HASH = os.getenv("API_HASH", "761766072a8594ad2cd13d9f4f3e99fd")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8452366963:AAHgRmkmRBKfJ-Dly1TOkJTtT_xqPID1u8Q")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = int(os.getenv("890658285", 0))
BOT_USERNAME = os.getenv("BOT_USERNAME", "ALottGroupHelpbot")

# Links and visuals
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/LBotsupportgroup")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/botsupdateschannels")
START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/vatrf9.jpg")
