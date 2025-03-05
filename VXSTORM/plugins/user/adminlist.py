from pyrogram import Client, filters, enums
from . import on_message
from VXSTORM.helper.basic import edit_or_reply

@on_message(["admins", "adminlist", "staff"], allow_stan=True)
async def allstaff(client, message):
    creator = None
    admins = []
    bots = []
    deleted = []

    ok = await edit_or_reply(message, "ꜰᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴꜱ...")

    async for x in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if x.user.is_bot:
            bots.append(x.user.mention)
        elif x.status.name == "OWNER":
            creator = x.user.mention
        elif x.user.is_deleted:
            deleted.append(x.user.mention)
        else:
            admins.append(x.user.mention)

    txt = f"**{message.chat.title} ꜱᴛᴀꜰꜰ :**\n\n"
    txt += " 👑 **ᴄʀᴇᴀᴛᴏʀ:**\n"
    txt += f" • {creator}\n"

    if admins:
        txt += "\n 👨‍💻 **ᴀᴅᴍɪɴꜱ:**\n"
        txt += "\n".join(f" • {adm}" for adm in admins)

    if bots:
        txt += "\n\n 🤖 **ʙᴏᴛꜱ:**\n"
        txt += "\n".join(f" • {bot}" for bot in bots)

    if deleted:
        txt += "\n\n 👻 **ᴅᴇʟᴇᴛᴇᴅ ᴀᴅᴍɪɴꜱ:**\n"
        txt += "\n".join(" • **None**" for _ in deleted)

    try:
        await ok.edit(txt)
    except:
        await message.reply(txt)
