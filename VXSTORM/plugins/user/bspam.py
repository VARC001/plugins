import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from OPUSDB.data import STORMS, BDAY
from . import on_message
from VXSTORM.helper.basic import edit_or_reply

@on_message("bspam", allow_stan=True)
async def bspam(x: Client, e: Message):
    kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(kex) == 2:
        try:
            ok = await x.get_users(kex[1])
            counts = int(kex[0])
            await edit_or_reply(e, f"**ʙꜱᴘᴀᴍ ꜱᴛᴀʀᴛᴇᴅ**\n**ᴜꜱᴇʀ:** {ok.first_name}\n**ᴄᴏᴜɴᴛ:** {counts}")
            
            for _ in range(counts):
                reply = choice(BDAY)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

        except Exception as err:
            await edit_or_reply(e, f"**ᴇʀʀᴏʀ:** {err}")

    elif e.reply_to_message:
        try:
            user_id = e.reply_to_message.from_user.id
            ok = await x.get_users(user_id)
            counts = int(kex[0])
            await edit_or_reply(e, f"**ʙꜱᴘᴀᴍ ꜱᴛᴀʀᴛᴇᴅ**\n**ᴜꜱᴇʀ:** {ok.first_name}\n**ᴄᴏᴜɴᴛ:** {counts}")

            for _ in range(counts):
                reply = choice(BDAY)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

        except Exception as err:
            await edit_or_reply(e, f"**ᴇʀʀᴏʀ:** {err}")

    else:
        await edit_or_reply(e, "**ᴜꜱᴀɢᴇ:** `.ʙꜱᴘᴀᴍ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>`")
