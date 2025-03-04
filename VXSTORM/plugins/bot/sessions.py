from pyrogram import Client, filters
from pyrogram.errors import SessionPasswordNeeded
from pyrogram.types import WebAppInfo
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardRemove,
)

from ..btnsG import gen_inline_keyboard, start_button
from ..btnsK import session_keyboard
from . import START_MSG, Config, Symbols, db, VXSTORM


# Existing session menu command
@VXSTORM.bot.on_message(
    filters.command("session") & Config.AUTH_USERS & filters.private
)
async def session_menu(_, message: Message):
    await message.reply_text(
        "**➡️ ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ʟɪꜱᴛ ʙᴇʟᴏᴡ:**",
        reply_markup=session_keyboard(),
    )


# New command to add session string manually
@VXSTORM.bot.on_message(filters.command("add") & Config.AUTH_USERS & filters.private)
async def add_session(_, message: Message):
    parts = message.text.split(" ", 1)
    if len(parts) < 2 or not parts[1]:
        return await message.reply_text("**[ᴇʀʀᴏʀ] ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ.**")
    
    session_string = parts[1]
    try:
        client = Client(
            name="VXSTORM 1.0",
            session_string=session_string,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            in_memory=True,
        )
        await client.connect()
        user_id = (await client.get_me()).id
        await db.update_session(user_id, session_string)
        await client.disconnect()
        await message.reply_text(
            "***✅ ꜱᴜᴄᴄᴇꜱꜱ: ꜱᴇꜱꜱɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴅᴀᴛᴀʙᴀꜱᴇ. ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ ᴜꜱᴇ ᴠxꜱᴛᴏʀᴍ 1.0 ᴀꜰᴛᴇʀ ꜱᴏᴍᴇᴛɪᴍᴇ.*\n\n**🔒 ɴᴏᴛᴇ: ɴᴏ ᴏɴᴇ, ɪɴᴄʟᴜᴅɪɴɢ ᴏᴜʀ ʙᴏᴛ, ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ʏᴏᴜʀ ꜱᴇꜱꜱɪᴏɴ ꜱᴛʀɪɴɢ.**"
        )
    except Exception as e:
        await message.reply_text(f"**[ᴇʀʀᴏʀ]** {e}")

# Existing command to create a new session
@VXSTORM.bot.on_message(filters.regex(r"ʀᴇɢɪꜱᴛᴇʀ ɴᴇᴡ 🔗") & Config.AUTH_USERS & filters.private)
async def new_session(_, message: Message):
    await message.reply_text(
        "**ꜱᴇᴛᴜᴘ ᴀ ɴᴇᴡ ꜱᴇꜱꜱɪᴏɴ**",
        reply_markup=ReplyKeyboardRemove(),
    )

    buttons = [
        [
            InlineKeyboardButton(
                "ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", 
                web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user")
            ),
        ]
    ]

    await message.reply_text(
        "**ꜱᴇᴛᴜᴘ ᴀ ꜱᴇꜱꜱɪᴏɴ**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


# Existing delete session command
@VXSTORM.bot.on_message(
    filters.regex(r"ᴅᴇʟᴇᴛᴇ 🗑️") & Config.AUTH_USERS & filters.private
)
async def delete_session(_, message: Message):
    all_sessions = await db.get_all_sessions()
    if not all_sessions:
        return await message.reply_text("ɴᴏ ꜱᴇꜱꜱɪᴏɴ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ")

    collection = []
    for i in all_sessions:
        collection.append((i["user_id"], f"rm_session:{i['user_id']}"))

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("❌", "auth_close")])

    await message.reply_text(
        "**ᴄʜᴏᴏꜱᴇ ᴀ ꜱᴇꜱꜱɪᴏɴ ᴛᴏ ᴅᴇʟᴇᴛᴇ**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


# Existing callback query handler to remove session
@VXSTORM.bot.on_callback_query(filters.regex(r"rm_session"))
async def rm_session_cb(client: Client, cb: CallbackQuery):
    collection = []
    user_id = int(cb.data.split(":")[1])
    all_sessions = await db.get_all_sessions()

    if not all_sessions:
        return await cb.message.delete()

    try:
        owner = await client.get_users(Config.OWNER_ID)
        owner_id = owner.id
        owner_name = owner.first_name
    except:
        owner_id = Config.OWNER_ID
        owner_name = "ᴏᴡɴᴇʀ"
    if cb.from_user.id not in [user_id, owner_id]:
        return await cb.answer(
            f"ᴏɴʟʏ {owner_name} ᴀɴᴅ ꜱᴇꜱꜱɪᴏɴ ᴄʟɪᴇɴᴛ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ꜱᴇꜱꜱɪᴏɴ.",
            show_alert=True,
        )

    await db.rm_session(user_id)
    await cb.answer("**ꜱᴇꜱꜱɪᴏɴ ᴅᴇʟᴇᴛᴇᴅ ꜰʀᴏᴍ ᴏʀ ᴅᴀᴛᴀʙᴀꜱᴇ**")

    for i in all_sessions:
        collection.append((i["user_id"], f"rm_session:{i['user_id']}"))

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("❌", "auth_close")])

    await cb.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

@VXSTORM.bot.on_message(filters.regex(r"ʜᴏᴍᴇ 📲") & filters.private & Config.AUTH_USERS)
async def go_home(_, message: Message):
    await message.reply_text(
        START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(start_button()),
    )

@VXSTORM.bot.on_message(filters.regex(r"ᴄᴏɴɴᴇᴄᴛ ꜱᴇꜱꜱɪᴏɴ 📡") & Config.AUTH_USERS & filters.private)
async def session_add(_, message: Message):
    await message.reply_text("/add {ᴘᴀsᴛᴇ ʏᴏᴜʀ sᴇssɪᴏɴ}")  
    
