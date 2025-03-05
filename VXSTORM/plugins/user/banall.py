from pyrogram import Client, filters
from . import on_message
from VXSTORM.helper.basic import edit_or_reply

@on_message("banall", allow_stan=True)
async def banall(client, message):
    if not message.from_user:
        return

    ok = await edit_or_reply(message, "ɢᴇᴛᴛɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")

    mem = []
    async for x in client.get_chat_members(message.chat.id):
        mem.append(x.user.id)

    await ok.edit("ʙᴀɴɴɪɴɢ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀꜱ....")

    a, b = 0, 0
    for y in mem:
        try:
            await client.ban_chat_member(message.chat.id, y)
            a += 1
        except:
            b += 1
            pass

    await ok.edit(f"**ᴅᴏɴᴇ ✅**\n\n{a} ᴍᴇᴍʙᴇʀꜱ ʙᴀɴɴᴇᴅ..!!\n{b} ꜰᴀɪʟᴇᴅ..!!")
