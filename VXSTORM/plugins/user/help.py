import os
import asyncio
from pyrogram import Client
from pyrogram.types import Message
from VXSTORM.helper.core import ReplyCheck
from VXSTORM.core import ENV
from VXSTORM.helper.basic import edit_or_reply
from . import Config, db, VXSTORM, on_message

help_logo = "https://envs.sh/help.mp4"  # Change to an actual help image/video URL

hl = "."
FIRST_TEXT = f"""
✨ **•─╼⃝𖠁 ʙᴏᴛ ʜᴇʟᴘ 𖠁⃝╾─•** ✨

**[ᴠx ꜱᴛᴏʀᴍ ᴠ2.0ᴘ+](https://t.me/ll_KEX_ll) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ᴏᴘᴜꜱ](https://t.me/VXSTORM_BOT)** ✨

**ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳](https://t.me/STORM_TECHH)**

**🔹 ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpbot`  
**🔹 ʀᴀɪᴅ/ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpspam`  
**🔹 ᴘᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helppm`  
**🔹 ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helplove`  
**🔹 ɪɴᴛᴇʀɴᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpinternet`  
**🔹 ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpconvert`  
**🔹 ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpinfo`  
**🔹 ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpcreate`  
**🔹 ᴘʀᴏꜰɪʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpprofile`  
**🔹 ᴡɪꜱʜ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpwish`  
**🔹 ꜰ-ᴀᴄᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpfaction`  
**🔹 ᴠᴄ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpvc`  
**🔹 ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpfun`  
**🔹 ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ 2:** `{hl}helpfuntwo`
"""

@on_message("help", allow_stan=True)
async def help(client: Client, message: Message):
    X = await edit_or_reply(message, "✨")
    await asyncio.sleep(1)
    
    send_media = client.send_video if help_logo.endswith(".mp4") else client.send_photo

    try:
        await send_media(
            message.chat.id,
            help_logo,
            caption=FIRST_TEXT,
            reply_to_message_id=ReplyCheck(message),
        )
        await X.delete()
    except:
        await X.edit(FIRST_TEXT, disable_web_page_preview=True)
