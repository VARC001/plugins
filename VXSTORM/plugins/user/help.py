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

@on_message("help", allow_stan=True)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "✨")
    await asyncio.sleep(1)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    man = (
    f"✨ <b>•─╼⃝𖠁 ʙᴏᴛ ʜᴇʟᴘ 𖠁⃝╾─•</b> ✨\n\n"
    f"<b><a href='https://t.me/ll_KEX_ll'>ᴠx ꜱᴛᴏʀᴍ ᴠ2.0ᴘ+</a> ʜᴇʟᴘ ᴍᴇɴᴜ</b> 🥀\n\n"
    f"<b>ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/VXSTORM_BOT'>ᴏᴘᴜꜱ</a></b> ✨\n\n"
    f"<b>ᴄʜᴀɴɴᴇʟ:</b> <a href='https://t.me/STORM_TECHH'>ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳</a>\n\n"
    f"🔹 <b>ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpbot</code>\n"
    f"🔹 <b>ʀᴀɪᴅ/ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpspam</code>\n"
    f"🔹 <b>ᴘᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helppm</code>\n"
    f"🔹 <b>ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helplove</code>\n"
    f"🔹 <b>ɪɴᴛᴇʀɴᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpinternet</code>\n"
    f"🔹 <b>ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpconvert</code>\n"
    f"🔹 <b>ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpinfo</code>\n"
    f"🔹 <b>ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpcreate</code>\n"
    f"🔹 <b>ᴘʀᴏꜰɪʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpprofile</code>\n"
    f"🔹 <b>ᴡɪꜱʜ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpwish</code>\n"
    f"🔹 <b>ᴠᴄ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpvc</code>\n"
    f"🔹 <b>ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:</b> <code>{hl}helpfun</code>\n"
    f"🔹 <b>ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ 2:</b> <code>{hl}helpfuntwo</code>\n"
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
