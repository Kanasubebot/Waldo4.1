import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "EngrJuanMala")
ALIVE_NAME = getenv("ALIVE_NAME", "Lourd")
BOT_USERNAME = getenv("BOT_USERNAME", "ImgMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "IMGAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "imagineitsreal")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "IMXSIC")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/fd0ecfe33be9c49017c38.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/HairyPotah02/ImagineMusic1.0")
IMG_1 = getenv("IMG_1", "https://telegra.ph//file/8cba811eafda966cd367e.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph//file/35069708993e65d8d981a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph//file/b8c87edb21e7dd39cd5e2.jpg")
