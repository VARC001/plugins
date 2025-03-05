import asyncio

from random import choice

from pyrogram import filters, Client
from pyrogram.types import Message

from OPUSDB.data import RAID, STORMS
from from . import Config
from VXSTORM.helper.basic import edit_or_reply
from . import VXSTORM, on_message

@on_message("dmraid", allow_stan=True)
async def dmraid(x: Client, message: Message):
    kex = message.text.split(" ")

    if len(kex) == 3:
        ok = await x.get_users(kex[2])
        id = ok.id

        if id in STORMS:
            await edit_or_reply(message, "ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
        elif id in SUDO_USERS:
            await edit_or_reply(message, "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
        else:
            counts = int(kex[1])
            await edit_or_reply(message, "ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
            for _ in range(counts):
                reply = choice(RAID)
                await x.send_message(id, reply)
                await asyncio.sleep(0.1)

    elif message.reply_to_message and (len(kex) == 2):
        user_id = message.reply_to_message.from_user.id
        ok = await x.get_users(user_id)
        id = ok.id

        if id in STORMS:
            await edit_or_reply(message, "ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
        elif id in SUDO_USERS:
            await edit_or_reply(message, "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
        else:
            counts = int(kex[1])
            await edit_or_reply(message, "ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
            for _ in range(counts):
                reply = choice(RAID)
                await x.send_message(id, reply)
                await asyncio.sleep(0.1)

    else:
        await edit_or_reply(message, ".ᴅᴍʀᴀɪᴅ 13 <ᴜꜱᴇʀ ɪᴅ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
