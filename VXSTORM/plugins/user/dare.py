import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from OPUSDB.data import DARE
from VXSTORM.helper.basic import edit_or_reply
from . import VXSTORM, on_message

@on_message("dare", allow_stan=True)
async def dare(x: Client, e: Message):
    reply = choice(DARE)
    await edit_or_reply(e, reply)
