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

@on_message("helpbot", allow_stan=True)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "✨")
    await asyncio.sleep(1)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    man = (
    f"<b>•─╼⃝𖠁 ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ 𖠁⃝╾─•</b>\n\n"
    f"🔹 <code>{hl}ping</code> » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴘɪɴɢ ᴀɴᴅ ᴜᴘᴛɪᴍᴇ\n"
    f"🔹 <code>{hl}alive</code> » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ\n"
    f"🔹 <code>{hl}repo</code> » ᴛᴏ ɢᴇᴛ ʙᴏᴛ ʀᴇᴘᴏ\n"
    f"🔹 <code>{hl}id</code> » ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟɪᴇᴅ ᴜꜱᴇʀ_ɪᴅ\n"
    f"🔹 <code>{hl}addsudo</code> » ᴛᴏ ᴀᴅᴅ ꜱᴜᴅᴏ\n"
    f"🔹 <code>{hl}sudolist</code> » ᴛᴏ ɢᴇᴛ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ʟɪꜱᴛ\n"
    f"🔹 <code>{hl}hping</code> » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ'ꜱ ᴘɪɴɢ\n"
    f"🔹 <code>{hl}eval</code> » ᴛᴏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ꜰᴜɴᴄᴛɪᴏɴs\n"
    f"🔹 <code>{hl}mystats</code> » ᴛᴏ ᴄʜᴋ ᴄʟɪᴇɴᴛ ꜱᴛᴀᴛꜱ\n"
    f"🔹 <code>{hl}bstats</code> » ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛꜱ\n"
    f"🔹 <code>{hl}join</code> » ᴛᴏ ᴊᴏɪɴ ᴄʜᴀᴛ\n"
    f"🔹 <code>{hl}leave</code> » ᴛᴏ ʟᴇᴀᴠᴇ ᴄʜᴀᴛ\n"
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
