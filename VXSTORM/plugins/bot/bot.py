import heroku3
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
import asyncio
import os
from VXSTORM import HEROKU_APP
from VXSTORM.core import LOGS
from VXSTORM.functions.tools import restart

from ..btnsG import start_button
from . import START_MSG, Config, VXSTORM


@VXSTORM.on_message(filters.command("start"))
async def start_pm(_, message: Message):
    btns = start_button()

    await message.reply_text(
        START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(btns),
    )


@VXSTORM.on_message(filters.command("update") & Config.AUTH_USERS)
async def restart_clients(_, message: Message):
    response = await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
    
    try:
        if HEROKU_APP:
            try:
                heroku = heroku3.from_key(Config.HEROKU_APIKEY)
                app = heroku.apps()[Config.HEROKU_APPNAME]
                app.restart()
            except:
                await restart()
        else:
            await restart()
    except Exception as e:
        LOGS.error(e)

    os.system(f"kill -9 {os.getpid()} && bash start.sh")
    

@VXSTORM.on_message(filters.command("stop") & Config.AUTH_USERS)
async def stop_bot(_, message: Message):
    response = await message.reply_text("sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ...")
    
    try:
        # Kill the current process
        os.system(f"kill -9 {os.getpid()}")
    except Exception as e:
        LOGS.error(e)
        await response.edit_text(f"ғᴀɪʟᴇᴅ ᴛᴏ sᴛᴏᴘ ʙᴏᴛ: {e}")
