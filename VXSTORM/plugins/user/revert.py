import os
from pyrogram import Client, filters
from pyrogram.types import Message
from VXSTORM.helper.basic import edit_or_reply
from . import VXSTORM, on_message

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "@STORM_CHATZ")

# Store original details
original_name = None
original_bio = None
original_photo = None

@on_message("save_profile", allow_stan=True)
async def save_profile(client: Client, message: Message):
    """Save the current profile details before making any changes."""
    global original_name, original_bio, original_photo

    me = await client.get_me()
    original_name = me.first_name  # Store current name
    original_bio = (await client.get_chat("me")).bio  # Store current bio

    photos = [p async for p in client.get_chat_photos("me")]
    if photos:
        original_photo = await client.download_media(photos[0].file_id)

    await edit_or_reply(message, "ᴘʀᴏꜰɪʟᴇ ᴅᴇᴛᴀɪʟꜱ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!")

@on_message("revert", allow_stan=True)
async def revert(client: Client, message: Message):
    """Revert the profile back to saved details."""
    global original_name, original_bio, original_photo

    await edit_or_reply(message, "ʀᴇᴠᴇʀᴛɪɴɢ....")

    if original_name:
        await client.update_profile(first_name=original_name)
    if original_bio:
        await client.update_profile(bio=original_bio)

    # Delete current profile photo
    photos = [p async for p in client.get_chat_photos("me")]
    if photos:
        await client.delete_profile_photos(photos[0].file_id)

    # Restore the original photo if it was saved
    if original_photo:
        await client.set_profile_photo(photo=original_photo)

    await edit_or_reply(message, "ɪ ᴀᴍ ʙᴀᴄᴋ....!")
