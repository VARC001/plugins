import os
import random
import time

from pyrogram import Client
from pyrogram.types import Message

from VXSTORM import START_TIME
from VXSTORM.core import ENV
from VXSTORM.functions.formatter import readable_time
from VXSTORM.functions.images import generate_alive_image
from VXSTORM.functions.templates import alive_template

from . import Config, db, VXSTORM, on_message


@on_message("alive", allow_stan=True)
async def alive(client: Client, message: Message):
    x = await VXSTORM.edit(message, "✨")

    img = await db.get_env(ENV.alive_pic)
    if not img:
        if message.from_user.photo:
            user_pfp = await client.download_media(message.from_user.photo.big_file_id)
            del_path = True
        else:
            user_pfp = "https://envs.sh/Pa1.mp4"
            del_path = False
        img = [
            generate_alive_image(
                message.from_user.first_name, user_pfp, del_path, Config.FONT_PATH
            )
        ]
    else:
        img = img.split(" ")

    img = random.choice(img)
    uptime = readable_time(time.time() - START_TIME)
    caption = await alive_template(client.me.first_name, uptime)

    if img.endswith(".mp4"):
        await message.reply_video(img, caption=caption)
    else:
        await message.reply_photo(img, caption=caption)
    await x.delete()

    try:
        os.remove(img)
    except:
        pass
