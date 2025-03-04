from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

from VXSTORM.core import Config, db, VXSTORM
from VXSTORM.functions.admins import is_user_admin


def on_message(
    command: str | list[str],
    group: int = 0,
    chat_type: list[ChatType] = None,
    admin_only: bool = False,
    allow_stan: bool = False,
):
    if allow_stan:
        _filter = (
            filters.command(command, Config.HANDLERS)
            & (filters.me | Config.STAN_USERS)
            & ~filters.forwarded
            & ~filters.via_bot
        )
    else:
        _filter = (
            filters.command(command, Config.HANDLERS)
            & filters.me
            & ~filters.forwarded
            & ~filters.via_bot
        )

    def decorator(func):
        async def wrapper(client: Client, message: Message):
            if client.me.id != message.from_user.id:
                if not await db.is_stan(client.me.id, message.from_user.id):
                    return

            if admin_only and not message.chat.type == ChatType.PRIVATE:
                if not await is_user_admin(message.chat, client.me.id):
                    return await VXSTORM.edit(message, "ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʜᴇʀᴇ !")

            if chat_type and message.chat.type not in chat_type:
                return await VXSTORM.edit(message, "ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴍᴅ ʜᴇʀᴇ !!")

            await func(client, message)
            message.continue_propagation()

        for user in VXSTORM.users:
            user.add_handler(MessageHandler(wrapper, _filter), group)

        return wrapper

    return decorator


def custom_handler(filters: filters.Filter, group: int = 0):
    def decorator(func):
        async def wrapper(client: Client, message: Message):
            await func(client, message)
            message.continue_propagation()

        for user in VXSTORM.users:
            user.add_handler(MessageHandler(wrapper, filters), group)

        return wrapper

    return decorator
