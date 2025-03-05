import os
from pyrogram import Client, filters
from pyrogram.types import Message
from .helper.basic import edit_or_reply, get_text, get_user

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "@STORM_CHATZ")
SUDO_USERS = []  # Ensure this is populated somewhere

original_name = None
original_bio = None
original_photo = None


@on_message("clone", allow_stan=True)
async def clone(client: Client, message: Message):
    global original_name, original_bio, original_photo

    text = get_text(message)
    op = await edit_or_reply(message, "ᴄʟᴏɴɪɴɢ....")

    userk = get_user(message, text)[0]
    try:
        user_ = await client.get_users(userk)
    except:
        return await op.edit("ɪɴᴠᴀʟɪᴅ ᴜꜱᴇʀ. ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀɴᴀᴍᴇ/ID.")

    me = await client.get_me()
    original_name = me.first_name
    original_bio = (await client.get_chat(me.id)).bio
    photos = [p async for p in client.get_chat_photos("me")]
    original_photo = photos[0].file_id if photos else None

    f_name = user_.first_name
    get_bio = await client.get_chat(user_.id)
    c_bio = get_bio.bio if get_bio.bio else " "

    photo_id = user_.photo.big_file_id if user_.photo else None

    if photo_id:
        poto = await client.download_media(photo_id)
        await client.set_profile_photo(photo=poto)

    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )

    await op.edit(f"**ɴᴏᴡ ɪ'ᴍ** {f_name}")


