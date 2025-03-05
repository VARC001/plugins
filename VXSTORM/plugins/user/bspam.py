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
        ok = await x.get_users(kex[1])
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(BDAY)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await x.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await x.get_users(user_id)
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(BDAY)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await x.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await edit_or_reply(Message, ".ʙꜱᴘᴀᴍ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")
