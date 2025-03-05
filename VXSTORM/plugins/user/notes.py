import asyncio
import random
import time
from pyrogram.types import Message
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram import filters, Client
from OPUSDB.data import PORM
from . import *

@on_message("pornspam", allow_stan=True)
async def prns(client: Client, message: Message):
    r = await message.reply_text("⌛")
    quantity = message.command[1]
    failed = 0
    quantity = int(quantity)
    await r.delete()
    if int(message.chat.id) in GROUP:
        await message.reply_text("ʏᴏᴜ ᴄᴀɴɴᴏᴛ ᴘᴏʀɴꜱᴘᴀᴍ ɪɴ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴄʜᴀᴛꜱ!")
        return
    for _ in range(quantity):
        try:
            file = random.choice(PORM)            
            await client.send_video(chat_id=message.chat.id, video=file)
        except FloodWait as e:
            await asyncio.sleep(e.x)
