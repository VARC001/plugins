import asyncio
import random
import time
from pyrogram.types import Message
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram import filters, Client
from OPUSDB.data import HRAID
from . import *

@on_message("hiraid", allow_stan=True)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(HRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(HRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("ʜʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  
