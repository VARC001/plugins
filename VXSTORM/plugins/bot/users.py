from pyrogram import Client, filters
from pyrogram.types import Message

from . import Config, Symbols, VXSTORM


@VXSTORM.bot.on_message(
    filters.command("auth") & Config.AUTH_USERS
)
async def addauth(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            return await message.reply_text(
                "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴍᴇ ᴀ ᴜꜱᴇʀɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀɴ ᴀᴜᴛʜ ᴜꜱᴇʀ!"
            )
        try:
            user = await client.get_users(message.command[1])
        except Exception:
            return await message.reply_text(
                "ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀɴ ᴀᴜᴛʜ ᴜꜱᴇʀ"
            )
    else:
        user = message.reply_to_message.from_user

    if user.is_self:
        return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴀᴅᴅ ᴍʏꜱᴇʟꜰ ᴀꜱ ᴀɴ ᴀᴜᴛʜ ᴜꜱᴇʀ!")

    if user.id in Config.AUTH_USERS:
        return await message.reply_text(f"**{user.mention} ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ**")

    Config.AUTH_USERS.add(user.id)
    await message.reply_text(f"**ᴀᴅᴅᴇᴅ {user.mention} ᴛᴏ ᴀᴜᴛʜ ᴜꜱᴇʀꜱ!**")


@VXSTORM.bot.on_message(
    filters.command("unauth") & Config.AUTH_USERS
)
async def delauth(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            return await message.reply_text(
                "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ ᴍᴇ ᴀ ᴜꜱᴇʀɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀɴ ᴀᴜᴛʜ ᴜꜱᴇʀ!"
            )
        try:
            user = await client.get_users(message.command[1])
        except Exception:
            return await message.reply_text(
                "ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍ ᴀꜱ ᴀɴ ᴀᴜᴛʜ ᴜꜱᴇʀ!"
            )
    else:
        user = message.reply_to_message.from_user

    if user.id in Config.AUTH_USERS:
        Config.AUTH_USERS.remove(user.id)
        await message.reply_text(f"**ʀᴇᴍᴏᴠᴇᴅ {user.mention} ꜰʀᴏᴍ ᴀᴜᴛʜ ᴜꜱᴇʀꜱ!**")
    else:
        await message.reply_text(f"**{user.mention} ɪꜱ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ**")


@VXSTORM.bot.on_message(
    filters.command("authlist") & Config.AUTH_USERS
)
async def authlist(client: Client, message: Message):
    text = "**🍀 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜꜱᴇʀꜱ:**\n\n"
    for i, userid in enumerate(Config.AUTH_USERS):
        try:
            user = await client.get_users(userid)
            text += f"    {Symbols.anchor} {user.mention} (`{user.id}`)\n"
        except:
            text += f"    {Symbols.anchor} ᴀᴜᴛʜ ᴜꜱᴇʀ #{i+1} (`{userid}`)\n"

    await message.reply_text(text)

