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
    BOT_TOKEN = "5926143600:AAHcqLwRHwIQ1GKFjTlCrxRM75eCyaw8tns"
    API_ID = 13191216
    API_HASH = "7d38e4760cb8717cd434e8f449d65b16"
    USERBOT_PREFIX = "."
    SESSION_STRING ="BQB2tODQ2kwkDumoh1K-hUSF158y24uTn9fsQah2AdNUwYxXpHmzppkPpzzlJ0ToNQTeUGXgKgt1Hn0tb6DlmqmxTD_nx9UkpNC7cdUejKYM3XncNTgLQSPUGUZg9hJqunhBkXvh8pt0vajh6I9KOO0eMKmxvZNMaURez08t1etNaCzTT8Mq4RFzhur7qxMGBt66KfqklNrMP8oNQFciaNwmHv-N-zhksJf404i1Udax2MFl_Mk6ndPgwJgTDSCXb0Syx4qA_GG9oyLltkUoH_EbmOTkHA5dZxLM8AzTXgFtVonTstNbj73EySdMmN9zoNjT9k284d-wS3hV3l4k7roDAAAAAHaTQnQA"
    PHONE_NUMBER = "+919095330555"
    SUDO_USERS_ID = [
        1930954213,
        1930954213,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001657538863
    GBAN_LOG_GROUP_ID = -1001657538863
    MESSAGE_DUMP_CHAT = -1001657538863
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://ZAID:ZAID@cluster0.8smkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "JGAGCN-IRAJKY-PTPEXD-FCDGHX-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = False
