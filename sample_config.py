from os import environ

from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = bool(
    environ.get("DYNO")
)  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_URL = environ.get("MONGO_URL", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", None)))
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", None)))
else:
    BOT_TOKEN = "5477183241:AAG6Ea9Nm2jsPqFl5VUq9t3buzSZVg20l5k"
    API_ID = 14782914
    API_HASH = "3aa2fabe1074632cf6e2b01da083a2c6"
    USERBOT_PREFIX = "."
    SESSION_STRING =""
    SUDO_USERS_ID = [
        1930954213,
        1930954213,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001635517276
    GBAN_LOG_GROUP_ID = -1001635517276
    MESSAGE_DUMP_CHAT = -1001635517276
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://Alanwalker:20092001@cluster0.nwbeo.mongodb.net/?retryWrites=true&w=majority"
    ARQ_API_KEY = "JGAGCN-IRAJKY-PTPEXD-FCDGHX-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = False
