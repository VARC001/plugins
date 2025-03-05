import asyncio

from random import choice

from pyrogram import filters, Client
from pyrogram.types import Message

from OPUSDB.data import RAID, STORMS
from VXSTORM.core.config import STAN_USERS as SUDO_USERS
from VXSTORM.helper.basic import edit_or_reply
from . import VXSTORM, on_message

@on_message("dmspam", allow_stan=True)
async def dmspam(client: Client, message: Message):
    kex = message.text.split(" ", 3)

    if len(kex) == 4:
        uid = int(kex[2])
        if uid in STORMS:
            await edit_or_reply(message, "ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
        elif uid in SUDO_USERS:
            await edit_or_reply(message, "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
        else:
            quantity, spam_text = int(kex[1]), kex[3]
            await edit_or_reply(message, "ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(kex) == 3):
        id = message.reply_to_message.from_user.id

        if id in STORMS:
            await edit_or_reply(message, "ᴠᴇʀɪꜰɪᴇᴅ ʙʏ ꜱᴛᴏʀᴍ ✅")
        elif id in SUDO_USERS:
            await edit_or_reply(message, "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs sᴜᴅᴏ ᴜsᴇʀ 💗")
        else:
            quantity = int(kex[1])
            spam_text = kex[2]
            await edit_or_reply(message, "ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ⚠️")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await edit_or_reply(message, ".ᴅᴍꜱᴘᴀᴍ 13 <ᴜꜱᴇʀ ɪᴅ> <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ> ꜱᴛᴏʀᴍ")
