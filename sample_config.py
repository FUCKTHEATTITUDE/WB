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
    BOT_TOKEN = "5165959972:AAEXWdylwty0pVDz6X_8hZw1NL8EqTfNByk"
    API_ID = 13191216
    API_HASH = "7d38e4760cb8717cd434e8f449d65b16"
    USERBOT_PREFIX = "."
    SESSION_STRING ="BQDhkcIAsuOS32EqZ09uSdXlvChpOh4leOsbhoOCtsEQ4bw5uS4FO5xUPemkLKfP93NC0hNOeoLU8QB2EcUcqx2fA10ePVSFMDr4wDPrUDHXoYhxyxlFdCMeqMfKGYMfsDJqFl7ebMdWJRdeRi5vv3xEgZWtHPSJkTc6VT9SnArfprvgXtDUB4i_7hGBvSxS54k2B4nziG1KiUy4PrA_jS8sxVZF_fLagB0Y5SBDu1DF6qKvuWFhiUnCnxI1w--1SdvT5P3z2a8qeFgKfCxvdgQ89c1j7eapf0wk_EulsJ1eZqE3dWIJMuA8aeX0IDovR5PPTJpg1mlgDAJeVeuTXvupC65stQAAAAE-8Cl3AA"
    PHONE_NUMBER = "+918903192810"
    SUDO_USERS_ID = [
        5938516793,
        1930954213,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001657538863
    GBAN_LOG_GROUP_ID = -1001657538863
    MESSAGE_DUMP_CHAT = -1001657538863
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://ZAID:ZAID@cluster0.8smkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "IDYNEY-SLKMLF-YMTCWU-TTTRIW-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = False
