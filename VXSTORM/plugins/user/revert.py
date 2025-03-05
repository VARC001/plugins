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

@Client.on_message(filters.command(["revert"], ".") & (filters.me | filters.user(SUDO_USERS)))
async def revert(client: Client, message: Message):
    global original_name, original_bio, original_photo

    await message.edit("ʀᴇᴠᴇʀᴛɪɴɢ....")

    r_bio = original_bio if original_bio is not None else BIO
    r_name = original_name if original_name is not None else OWNER

    await client.update_profile(
        first_name=r_name,
        bio=r_bio,
    )

    photos = [p async for p in client.get_chat_photos("me")]
    if photos:
        await client.delete_profile_photos(photos[0].file_id)

    if original_photo:
        await client.set_profile_photo(photo=original_photo)

    await message.edit("ɪ ᴀᴍ ʙᴀᴄᴋ....!")
