import random
import asyncio

from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType as MET, ChatAction as CA
from pyrogram.types import Message

from . import *
from OPUSDB.data import RAID

que = []
def is_reply_raid(func):
    async def get_userss(c: Client, m: Message):
        if not m.from_user:
            return
        if m.from_user.id not in que:
            return
        else:
            return await func(c,m)
    return get_userss

@custom_handler(filters.all,group=-18)
@is_reply_raid
async def _(c: Client,m: Message):
    message = random.choice(RAID)
    await c.send_chat_action(m.chat.id, CA.TYPING)
    await asyncio.sleep(1)
    await m.reply_text(message)
    await c.send_chat_action(m.chat.id, CA.CANCEL)

@on_message("replyraid", allow_stan=True)
async def activate_reply_raid(c: Client,m: Message):
    global que
    if m.forward_from:
        return
    if m.reply_to_message_id:
        repl_to = m.reply_to_message.from_user
        if not repl_to:
            await m.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ")
            return
        u_id = repl_to.id
        username = f"@{repl_to.username}" if repl_to.username else repl_to.mention
        Pbx = await m.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛɪɴɢ....")
        if u_id not in que:
            que.append(u_id)
            await Pbx.edit_text(f"ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ {username}")
        else:
            await Pbx.edit_text("ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ ꜱᴛᴀʀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ꜰᴏʀ ᴛʜɪꜱ ᴜꜱᴇʀ")
    else:
        try:
            user = int(m.command[1])
        except ValueError:
            user = m.command[1]
            if m.entities[1].type == MET.TEXT_MENTION:
                user = m.entities[1].user.id
        except:
            await m.reply_text("ᴇɪᴛʜᴇʀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴍᴇ ᴀɴᴅ ᴜꜱᴇʀ ɪᴅ")
        try:
            user = await c.get_users(user)
        except Exception:
            to_del = await m.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰᴇᴛᴄʜ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴇɴᴛɪᴛʏ")
            await asyncio.sleep(10)
            await m.delete(True)
            await to_del.delete(True)
            return
        Pbx = await m.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛɪɴɢ....")
        u_id = user.id
        username = f"@{user.username}" if user.username else user.mention
        if u_id not in que:
            que.append(u_id)
            await Pbx.edit_text(f"ᴇᴘʟʏ ʀᴀɪᴅ ʜᴀꜱ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ {username}")
        else:
            await Pbx.edit_text("ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ ꜱᴛᴀʀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ꜰᴏʀ ᴛʜɪꜱ ᴜꜱᴇʀ")


@on_message("dreplyraid", allow_stan=True)
async def deactivate_reply_raid(c: Client, m: Message):
    global que
    if m.forward_from:
        return
    if m.reply_to_message:
        reply_to = m.reply_to_message.from_user
        if not reply_to:
            await m.reply_text("ʀʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ")
            return
        u_id = reply_to.id
        username = f"@{reply_to.username}" if reply_to.username else reply_to.mention
        Pbx = await m.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛɪɴɢ....")
        try:
            if u_id in que:
                que.remove(u_id)
                await Pbx.edit_text(f"ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ {username}")
                return
            await Pbx.edit_text("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ꜱᴛᴀʀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ꜰᴏʀ ᴛʜɪꜱ ᴜꜱᴇʀ")
        except Exception:
            await Pbx.edit_text("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ꜰᴏʀ ᴛʜɪꜱ ᴜꜱᴇʀ")
            return
        
    else:
        try:
            user = int(m.command[1])
        except ValueError:
            user = m.command[1]
            if m.entities[1].type == MET.TEXT_MENTION:
                user = m.entities[1].user.id
        try:
            user = await c.get_users(user)
        except Exception:
            to_del = await m.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰᴇᴛᴄʜ")
            await asyncio.sleep(10)
            await m.delete(True)
            await to_del.delete(True)
            return
        Pbx = await m.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛɪɴɢ....")
        u_id = user.id
        username = f"@{user.username}" if user.username else user.mention
        try:
            if u_id in que:
                que.remove(u_id)
                await Pbx.edit_text(f"ʀᴇᴘʟʏ ʀᴀɪᴅ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ {username}")
                return
            await Pbx.edit_text("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ꜱᴛᴀʀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ꜰᴏʀ ᴛʜɪꜱ ᴜꜱᴇʀ")
        except Exception:
            await Pbx.edit_text("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏ ʀᴀɪᴅ ꜰᴏʀ ᴛʜɪꜱ ᴜꜱᴇʀ")
            return
