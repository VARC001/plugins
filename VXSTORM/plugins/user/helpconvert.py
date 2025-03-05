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
hl = "."

@on_message("helpconvert", allow_stan=True)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "✨")
    await asyncio.sleep(1)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    man = (
    f"<b>•─╼⃝𖠁 ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ 𖠁⃝╾─•</b>\n\n"
    f"🔹 <code>{hl}tts</code> » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ\n"
    f"🔹 <code>{hl}quotly</code> » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ Qᴜᴏᴛᴇ\n"
    f"🔹 <code>{hl}clone</code> » ᴄʟᴏɴᴇ ᴛᴏ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ\n"
    f"🔹 <code>{hl}revert</code> » ᴛᴏ ʀᴇᴠᴇʀᴛ ʏᴏᴜʀ ᴄʟᴏɴᴇ\n"
    f"🔹 <code>{hl}save_profile</code> » ᴛᴏ ꜱᴀᴠᴇ ʏᴏᴜʀ ᴘʀᴏꜰɪʟᴇ\n"        
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
