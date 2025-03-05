from pyrogram import Client
from pyrogram.types import Message

from . import Config, db, VXSTORM, on_message
from VXSTORM.helper.basic import edit_or_reply

@on_message("sudolist", allow_stan=True)
async def stanUsers(client: Client, message: Message):
    Pbx = await edit_or_reply(message, "**ꜰᴇᴛᴄʜɪɴɢ ᴜꜱᴇʀꜱ...**")

    users = await db.get_stans(client.me.id)
    if not users:
        return await Pbx.edit("**0 ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ꜰᴏᴜɴᴅ**")

    text = f"**ꜱᴜᴅᴏʟɪꜱᴛ:** `{len(users)}`\n\n"
    for user in users:
        try:
            user = await client.get_users(user["user_id"])
            mention = user.mention
            userid = user.id
        except Exception:
            userid = user["user_id"]
            mention = "Unknown Peer"
        text += f"• {mention} (`{userid}`)\n"

    await Pbx.edit(text)


@on_message("addsudo", allow_stan=False)
async def addstan(client: Client, message: Message):
    if len(message.command) < 2:
        if not message.reply_to_message:
            return await edit_or_reply(
                message,
                "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴍᴇ ᴀ ᴜꜱᴇʀ ɪᴅ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ",
            )
        user = message.reply_to_message.from_user
    else:
        try:
            user = await client.get_users(message.command[1])
        except Exception:
            return await edit_or_reply(
                message, "ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀ ɪᴅ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ"
            )

    if user.id == client.me.id:
        return await edit_or_reply(message, "ɪ ᴄᴀɴ'ᴛ ᴀᴅᴅ ᴍʏꜱᴇʟꜰ")

    if await db.is_stan(client.me.id, user.id):
        return await edit_or_reply(message, "ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ɪɴ ꜱᴜᴅᴏʟɪꜱᴛ")

    await db.add_stan(client.me.id, user.id)
    await edit_or_reply(message, f"ᴀᴅᴅᴇᴅ {user.mention} ᴀꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")

    Config.AUTH_USERS.add(user.id)
    Config.STAN_USERS.add(user.id)
