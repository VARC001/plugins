from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from . import *

@on_message("football", allow_stan=True)
async def football(_, e: Message):       
      Fuk = await e.reply("⚽️")
