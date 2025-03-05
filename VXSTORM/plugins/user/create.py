from pyrogram import Client, filters
from pyrogram.types import Message
from . import VXSTORM, on_message
from VXSTORM.helper.basic import edit_or_reply

@on_message("create", allow_stan=True)
async def gcch(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit(f".ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ")
    
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    bunny = await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ....")
    
    fuk = """ʙʏ - @STORM_CHATZ

- ɢɪᴠᴇ ʀᴇꜱᴘᴇᴄᴛ ᴛᴀᴋᴇ ʀᴇꜱᴘᴇᴄᴛ

- ᴅᴏɴ'ᴛ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ

- ᴅᴏɴ'ᴛ ᴜꜱᴇ 18+ ᴄᴏɴᴛᴇɴᴛꜱ

- ᴜʀɢᴇɴᴛ ᴄᴀʟʟ ᴏɴʟʏ

- ɴᴏ ꜱᴇʟʟɪɴɢ ᴏʀ ʙᴜʏɪɴɢ

- ᴅᴏɴ'ᴛ ᴜꜱᴇ ꜱʟᴀɴɢ ʟᴀɴɢᴜᴀɢᴇ ᴡʜɪʟᴇ ᴛᴀʟᴋɪɴɢ ɪɴ ɢʀᴏᴜᴘ"""
    
    if group_type == "group": 
        _id = await client.create_supergroup(group_name, fuk)
        await bunny.edit(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ....",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":  
        _id = await client.create_channel(group_name, fuk)
        await bunny.edit(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ....",
            disable_web_page_preview=True,
        )
