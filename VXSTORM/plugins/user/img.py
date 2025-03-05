import os
from pyrogram import Client, filters
from pyrogram.types import *
from . import *

hl = "."

@on_message("nice", allow_stan=True)
async def self_media(client, message):
    replied = message.reply_to_message
    if not replied:
        return
    if not (replied.photo or replied.video):
        return
    fuck = await client.download_media(replied)
    await client.send_document("me", fuck)
    os.remove(fuck)
