import random
from pyrogram import Client, filters
from . import Config, db, VXSTORM, on_message
from VXSTORM.helper.basic import edit_or_reply


@on_message("chance", allow_stan=True)
async def chance(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(message, "ɢɪᴠᴇ ᴍᴇ ꜱᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴄʜᴀɴᴄᴇ ꜰᴏʀ.")
    
    text = message.text.split(maxsplit=1)[1]
    chance_percentage = random.randint(1, 100)
    await edit_or_reply(message, f"**{text}**\n\n**ᴄʜᴀɴᴄᴇ**: {chance_percentage}%")
