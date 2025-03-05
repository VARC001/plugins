import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from OPUSDB.data import EMOJI
from VXSTORM.helper.basic import edit_or_reply
from . import VXSTORM, on_message

@on_message("emoji", allow_stan=True)
async def dare(x: Client, e: Message):
    args = e.text.split()  # Extract arguments from message
    count = 1  # Default to 1 dare
    
    if len(args) > 1 and args[1].isdigit():
        count = min(int(args[1]), 20)  # Limit max to 20

    for _ in range(count):
        reply = choice(EMOJI)
        await edit_or_reply(e, reply)
        await asyncio.sleep(1)  # Optional delay to prevent spam
