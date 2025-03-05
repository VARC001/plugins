import os
import random
import time

from pyrogram import Client
from pyrogram.types import Message

from VXSTORM import START_TIME
from VXSTORM.core import ENV
from VXSTORM.functions.formatter import readable_time
from VXSTORM.functions.templates import ping_template

from . import Config, db, VXSTORM, on_message

@on_message("ping", allow_stan=True)
async def ping(client: Client, message: Message):
    start_time = time.time()
    x = await VXSTORM.edit(message, "⚡")
    uptime = readable_time(time.time() - START_TIME)
    img = await db.get_env(ENV.ping_pic)
    end_time = time.time()
    speed = end_time - start_time
    caption = await ping_template(round(speed, 3), uptime, client.me.mention)
    if img:
        PIC = "./VXSTORM/resources/alive.png"
        img = random.choice(img.split(" "))
        if img.endswith(".mp4"):
            await message.reply_video(
                img,
                caption=caption,
            )
        else:
            await message.reply_photo(
                img,
                caption=caption,
            )
        return
    await VXSTORM.edit(x, caption, no_link_preview=True)
