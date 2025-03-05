import os
import random
import time
import asyncio
from pyrogram import Client
from pyrogram.types import Message
from VXSTORM.helper.core import ReplyCheck
from VXSTORM import START_TIME
from VXSTORM.core import ENV
from VXSTORM.functions.formatter import readable_time
from VXSTORM.functions.images import generate_alive_image
from VXSTORM.functions.templates import alive_template
from VXSTORM.helper.basic import edit_or_reply
from . import Config, db, VXSTORM, on_message

alive_logo = "https://envs.sh/Pa1.mp4"

@on_message("alive", allow_stan=True)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "✨")
    await asyncio.sleep(1)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = readable_time((time.time() - START_TIME))
    man = (
        f"<blockquote><b>⧼ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ‌🪽 ⧽</b></blockquote>\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"<blockquote><b>• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ: 3.11.3</b>\n<b>• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ: v2.0</b>\n<b>• ᴜᴘᴛɪᴍᴇ:</b> {uptime}\n<b>• ᴜꜱᴇʀʙᴏᴛ ᴠ-ꜱᴛᴀᴛᴜꜱ: ᴠx 2.2@ᴘ+</b></blockquote>\n"
        f"➖➖➖➖➖➖➖➖➖➖➖\n"
        f"<blockquote><b>• ᴅᴇᴠ: [Kᴜɴᴀʟ !](https://t.me/ll_KEX_ll)</b>\n<b>• ᴘᴏᴡᴇʀᴇᴅ ʙʏ Ɵᴘᴜs</b></blockquote>\n"
        f"➖➖➖➖➖➖➖➖➖➖➖"
    )
    try:
      await sad(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            )
      await X.delete()
    except:
      await X.edit(man, disable_web_page_preview=True)
