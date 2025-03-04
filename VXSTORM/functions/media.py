import os
from typing import Union

import requests
from pyrogram import Client
from pyrogram.file_id import FileId
from pyrogram.raw.functions.messages import UploadMedia
from pyrogram.raw.types import (
    DocumentAttributeFilename,
    InputDocument,
    InputMediaUploadedDocument,
)
from pyrogram.types import Animation, Audio, Document, Message, Photo, Sticker, Video

from VXSTORM.core import Symbols


async def get_metedata(media: Union[Animation, Audio, Document, Photo, Sticker, Video]):
    output = "📄 ᴍᴇᴛᴀᴅᴀᴛᴀ:\n\n"
    if isinstance(media, Animation):
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɪᴅ:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴡɪᴅᴛʜ:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} ʜᴇɪɢʜᴛ:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴜʀᴀᴛɪᴏɴ:</b> <code>{media.duration}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɴᴀᴍᴇ:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} �ɪᴍᴇ ᴛʏᴘᴇ:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ꜱɪᴢᴇ:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴀᴛᴇ:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ᴛʏᴘᴇ:</b> <code>ᴀɴɪᴍᴀᴛɪᴏɴ</code>\n"
    elif isinstance(media, Audio):
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɪᴅ:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴜʀᴀᴛɪᴏɴ:</b> <code>{media.duration}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴘᴇʀꜰᴏʀᴍᴇʀ:</b> <code>{media.performer}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴛɪᴛʟᴇ:</b> <code>{media.title}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɴᴀᴍᴇ:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴍɪᴍᴇ ᴛʏᴘᴇ:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ꜱɪᴢᴇ:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴀᴛᴇ:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ᴛʏᴘᴇ:</b> <code>ᴀᴜᴅɪᴏ</code>\n"
    elif isinstance(media, Document):
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɪᴅ:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɴᴀᴍᴇ:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴍɪᴍᴇ ᴛʏᴘᴇ:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ꜱɪᴢᴇ:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴀᴛᴇ:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ᴛʏᴘᴇ:</b> <code>ᴅᴏᴄᴜᴍᴇɴᴛ</code>\n"
    elif isinstance(media, Photo):
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɪᴅ:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} �ɪᴅᴛʜ:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} ʜᴇɪɢʜᴛ:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɴᴀᴍᴇ:</b> <code>ᴘʜᴏᴛᴏ.ᴊᴘɢ</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴍɪᴍᴇ ᴛʏᴘᴇ:</b> <code>ɪᴍᴀɢᴇ/ᴊᴘᴇɢ</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ꜱɪᴢᴇ:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴀᴛᴇ:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ᴛʏᴘᴇ:</b> <code>ᴘʜᴏᴛᴏ</code>\n"
    elif isinstance(media, Sticker):
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɪᴅ:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴡɪᴅᴛʜ:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} ʜᴇɪɢʜᴛ:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɴᴀᴍᴇ:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴍɪᴍᴇ ᴛʏᴘᴇ:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ꜱɪᴢᴇ:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴀᴛᴇ:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴇᴍᴏᴊɪ:</b> <code>{media.emoji}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜱᴇᴛ ɴᴀᴍᴇ:</b> <code>{media.set_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ᴛʏᴘᴇ:</b> <code>ꜱᴛɪᴄᴋᴇʀ</code>\n"
    elif isinstance(media, Video):
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɪᴅ:</b> <code>{media.file_id}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴡɪᴅᴛʜ:</b> <code>{media.width}</code>\n"
        output += f"<b>{Symbols.diamond_2} ʜᴇɪɢʜᴛ:</b> <code>{media.height}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴜʀᴀᴛɪᴏɴ:</b> <code>{media.duration}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ɴᴀᴍᴇ:</b> <code>{media.file_name}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴍɪᴍᴇ ᴛʏᴘᴇ:</b> <code>{media.mime_type}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ꜱɪᴢᴇ:</b> <code>{media.file_size}</code>\n"
        output += f"<b>{Symbols.diamond_2} ᴅᴀᴛᴇ:</b> <code>{media.date}</code>\n"
        output += f"<b>{Symbols.diamond_2} ꜰɪʟᴇ ᴛʏᴘᴇ:</b> <code>ᴠɪᴅᴇᴏ</code>\n"
    else:
        return None

    return output


def get_media_text_ocr(filename: str, api_key: str, language: str = "eng") -> dict:
    payload = {
        "isOverlayRequired": False,
        "apikey": api_key,
        "language": language,
    }

    with open(filename, "rb") as f:
        r = requests.post(
            "https://api.ocr.space/parse/image",
            files={filename: f},
            data=payload,
        )

    return r.json()


async def upload_media(client: Client, chat_id: int, file: str) -> InputDocument:
    media = await client.invoke(
        UploadMedia(
            peer=(await client.resolve_peer(chat_id)),
            media=InputMediaUploadedDocument(
                file=(await client.save_file(file)),
                mime_type=client.guess_mime_type(file) or "application/zip",
                attributes=[
                    DocumentAttributeFilename(file_name=os.path.basename(file))
                ],
                force_file=True,
            ),
        ),
    )

    return InputDocument(
        id=media.document.id,
        access_hash=media.document.access_hash,
        file_reference=media.document.file_reference,
    )


async def get_media_from_id(file_id: str) -> InputDocument:
    file = FileId.decode(file_id)

    return InputDocument(
        id=file.media_id,
        access_hash=file.access_hash,
        file_reference=file.file_reference,
    )


async def get_media_fileid(message: Message) -> str | None:
    file_id = None
    if message.photo:
        file_id = message.photo.file_id
    elif message.animation:
        file_id = message.animation.file_id
    elif message.audio:
        file_id = message.audio.file_id
    elif message.document:
        file_id = message.document.file_id
    elif message.video:
        file_id = message.video.file_id
    elif message.sticker:
        file_id = message.sticker.file_id
    elif message.video_note:
        file_id = message.video_note.file_id
    elif message.voice:
        file_id = message.voice.file_id
    return file_id
