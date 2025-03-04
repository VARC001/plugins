import os
import time
from platform import python_version

import heroku3
from pyrogram import __version__ as pyrogram_version

from .core import LOGS, Config

START_TIME = time.time()


__version__ = {
    "VXSTORM": "1.0",
    "pyrogram": pyrogram_version,
    "python": python_version(),
}


try:
    if Config.HEROKU_APIKEY is not None and Config.HEROKU_APPNAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_APIKEY).apps()[
            Config.HEROKU_APPNAME
        ]
    else:
        HEROKU_APP = None
except Exception as e:
    LOGS.error(f"ʜᴇʀᴏᴋᴜ ᴀᴘɪ - {e}")
    HEROKU_APP = None


if Config.API_HASH is None:
    LOGS.error("ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʏᴏᴜʀ ᴀᴘɪ_ʜᴀꜱʜ !")
    quit(1)

if Config.API_ID == 0:
    LOGS.error("ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʏᴏᴜʀ ᴀᴘɪ_ɪᴅ !")
    quit(1)

if Config.BOT_TOKEN is None:
    LOGS.error("ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʏᴏᴜʀ ʙᴏᴛ_ᴛᴏᴋᴇɴ !")
    quit(1)

if Config.DATABASE_URL is None:
    LOGS.error("ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʏᴏᴜʀ ᴅᴀᴛᴀʙᴀꜱᴇ_ᴜʀʟ !")
    quit(1)

if Config.LOGGER_ID == 0:
    LOGS.error("ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʏᴏᴜʀ ʟᴏɢɢᴇʀ_ɪᴅ !")
    quit(1)

if Config.OWNER_ID == 0:
    LOGS.error("ᴘʟᴇᴀꜱᴇ ꜱᴇᴛ ʏᴏᴜʀ ᴏᴡɴᴇʀ_ɪᴅ !")
    quit(1)

if not os.path.isdir(Config.DWL_DIR):
    os.makedirs(Config.DWL_DIR)

if not os.path.isdir(Config.TEMP_DIR):
    os.makedirs(Config.TEMP_DIR)
