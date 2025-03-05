from pyrogram import Client
from pyrogram.types import Message

from . import Config, db, VXSTORM, on_message


@on_message("sudolist", allow_stan=True)
async def stanUsers(client: Client, message: Message):
    Pbx = await VXSTORM.edit(message, "**ꜰᴇᴛᴄʜɪɴɢ ᴜꜱᴇʀꜱ**")

    users = await db.get_stans(client.me.id)
    if not users:
        return await VXSTORM.delete(Pbx, "**0 ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ꜰᴏᴜɴᴅ**")

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
            return await VXSTORM.delete(
                message,
                "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴍᴇ ᴀ ᴜꜱᴇʀ ɪᴅ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ",
            )
        user = message.reply_to_message.from_user
    else:
        try:
            user = await client.get_users(message.command[1])
        except Exception:
            return await VXSTORM.delete(
                message, "ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀ ɪᴅ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ"
            )

    if user.id == client.me.id:
        return await VXSTORM.delete(message, "ɪ ᴄᴀɴ'ᴛ ʙᴇ ᴀ ᴀᴅᴅ ᴍʏꜱᴇʟꜰ")

    if await db.is_stan(client.me.id, user.id):
        return await VXSTORM.delete(message, "ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ɪɴ ꜱᴜᴅᴏʟɪꜱᴛ")

    await db.add_stan(client.me.id, user.id)
    await VXSTORM.delete(message, f"ᴀᴅᴅᴇᴅ {user.mention} ᴀꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ")

    Config.AUTH_USERS.add(user.id)
    Config.STAN_USERS.add(user.id)
