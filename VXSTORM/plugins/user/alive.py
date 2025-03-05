import os
import random
import time

from pyrogram import Client
from pyrogram.types import Message

from VXSTORM import START_TIME
from VXSTORM.core import ENV
from VXSTORM.functions.formatter import readable_time
from VXSTORM.functions.images import generate_alive_image
from VXSTORM.functions.templates import alive_template

from . import Config, db, VXSTORM, on_message

ALIVE_PIC = "https://envs.sh/Pa1.mp4"

@on_message("alive", allow_stan=True)
async def alive(x: Client, msg: Message):
    bot_user = await x.get_me()
    KEX = f"""**⧼ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ‌🪽 ⧽**
➖➖➖➖➖➖➖➖➖➖➖
**• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ: 3.11.3**
**• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ: v2.0**
**• ᴜꜱᴇʀʙᴏᴛ ᴠ-ꜱᴛᴀᴛᴜꜱ: ᴠx 2.2@ᴘ+**
➖➖➖➖➖➖➖➖➖➖➖
**• ᴅᴇᴠ: [Kᴜɴᴀʟ !](https://t.me/ll_KEX_ll)**
**• ᴘᴏᴡᴇʀᴇᴅ ʙʏ Ɵᴘᴜs**
➖➖➖➖➖➖➖➖➖➖➖
"""
    if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
        await x.send_photo(msg.chat.id, ALIVE_PIC, caption=KEX)
    elif ".mp4" in ALIVE_PIC or ".MP4" in ALIVE_PIC:
        await x.send_video(msg.chat.id, ALIVE_PIC, caption=KEX)
