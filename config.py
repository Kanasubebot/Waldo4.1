import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Waldo Music Bot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "EngrJuanMala")
ALIVE_NAME = getenv("ALIVE_NAME", "Lourd")
BOT_USERNAME = getenv("BOT_USERNAME", "Wlkjn_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BaldoMusicAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LucidSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LucidSupportChanne;")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/fd0ecfe33be9c49017c38.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/HairyPotah02/Waldo4.1")
IMG_1 = getenv("IMG_1", "https://telegra.ph//file/2145fd804f1002ee1e63a.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/61eed61fcd41034cca67a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph//file/74f1ebd48469e6509e1c0.jpg")
