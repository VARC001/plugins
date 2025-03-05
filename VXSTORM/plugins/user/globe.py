from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from . import *

@on_message("globe", allow_stan=True)
async def globe(client: Client, message: Message):
    await message.edit("🌏")
    await asyncio.sleep(0.5)
    await message.edit("🌏")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
    await asyncio.sleep(0.5)
    await message.edit("🌎")
    await asyncio.sleep(0.5)
    await message.edit("🌎")
    await asyncio.sleep(0.5)
    await message.edit("🌎")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
    await asyncio.sleep(0.5)
    await message.edit("🌏")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
