from pyrogram import Client, filters
from pyrogram.types import Message
from VXSTORM.helper.basic import edit_or_reply
from . import *

hl = "."
HELP_PIC = "https://envs.sh/Pa1.mp4"  # Ensure this is a valid image/video URL if needed

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
**🔹 ᴠᴄ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpvc`  
**🔹 ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}helpfun`  
**🔹 ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ 2:** `{hl}helpfuntwo`
"""

@on_message("help", allow_stan=True)
async def help(client: Client, message: Message):
    if HELP_PIC.endswith((".jpg", ".png")):
        await client.send_photo(message.chat.id, HELP_PIC, caption=FIRST_TEXT)
    elif HELP_PIC.endswith((".mp4", ".MP4")):
        await client.send_video(message.chat.id, HELP_PIC, caption=FIRST_TEXT)
    else:
        await edit_or_reply(message, FIRST_TEXT)  # Using edit_or_reply for text response
