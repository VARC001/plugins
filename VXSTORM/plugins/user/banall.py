from pyrogram import Client, filters
from . import on_message


@on_message("banall", allow_stan=True)
async def banall(client, message):
    if not message.from_user:
        return
    ok = await message.edit("ɢᴇᴛᴛɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")
    mem = []
    async for x in client.get_chat_members(message.chat.id):
        mem.append(x.user.id)
    try:
        await ok.edit("ʙᴀɴɴɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")
    except:
        await message.reply("ʙᴀɴɴɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")
    a = 0
    b = 0
    for y in mem:
        try:
            await client.ban_chat_member(message.chat.id, y)
            a += 1
        except:
            b += 1
            pass
    try:
        await ok.edit(f"**ᴅᴏɴᴇ ✅**\n\n{a} ʙᴀɴɴᴇᴅ..!!\n \n{b} ꜰᴀɪʟᴇᴅ..!!")
    except:
        await message.reply(f"ᴅᴏɴᴇ ✅\n\n{a} ʙᴀɴɴᴇᴅ..!!\n \n {b} ꜰᴀɪʟᴇᴅ..!!")
