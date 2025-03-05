from pyrogram import Client
from pyrogram.types import Message
import asyncio
from . import VXSTORM, on_message
from VXSTORM.helper.basic import edit_or_reply

@on_message(["cheart", "colourheart"], allow_stan=True)
async def chearts(client: Client, message: Message):
    heart_sequences = [
        "❤️🧡💛💚💙💜🖤",
        "🧡❤️💛💚💙💜🖤",
        "💛🧡❤️💚💙💜🖤",
        "💚💛🧡❤️💙💜🖤",
        "💙💚💛🧡❤️💜🖤",
        "💜💙💚💛🧡❤️🖤",
        "🖤💜💙💚💛🧡❤️",
        "❤️🧡💛💚💙💜🖤",
        "🖤💜💙💚💛🧡❤️",
        "❤️🧡💙💜💛💚🖤",
    ]

    for hearts in heart_sequences:
        await edit_or_reply(message, hearts)
        await asyncio.sleep(0.5)
