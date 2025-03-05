import asyncio
import glob
import importlib
import os
import sys
from pathlib import Path

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .config import Config, Symbols, ENV
from .database import db
from .logger import LOGS


class PbxClient(Client):
    def __init__(self) -> None:
        self.users: list[Client] = []
        self.bot: Client = Client(
            name="VXSTORM 1.0",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="VXSTORM.plugins.bot"),
        )
        # Initialize the dispatcher for the bot
        self.dispatcher = self.bot.dispatcher

    async def start_bot(self) -> None:
        """Start the bot client."""
        await self.bot.start()
        me = await self.bot.get_me()
        LOGS.info(
            f"{Symbols.arrow_right * 2} ꜱᴛᴀʀᴛᴇᴅ VXSTORM ᴄʟɪᴇɴᴛ: '{me.username}' {Symbols.arrow_left * 2}"
        )

    async def start_user(self) -> None:
        """Start user clients."""
        sessions = await db.get_all_sessions()
        for i, session in enumerate(sessions):
            try:
                client = Client(
                    name=f"VXUser#{i + 1}",
                    api_id=Config.API_ID,
                    api_hash=Config.API_HASH,
                    session_string=session["session"],
                )
                await client.start()
                me = await client.get_me()
                self.users.append(client)
                LOGS.info(
                    f"{Symbols.arrow_right * 2} ꜱᴛᴀʀᴛᴇᴅ ᴜꜱᴇʀ {i + 1}: '{me.first_name}' {Symbols.arrow_left * 2}"
                )
                is_in_logger = await self.validate_logger(client)
                if not is_in_logger:
                    LOGS.warning(
                        f"ᴄʟɪᴇɴᴛ #{i+1}: '{me.first_name}' ɪꜱ ɴᴏᴛ ɪɴ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ! ᴄʜᴇᴄᴋ ᴀɴᴅ ᴀᴅᴅ ᴍᴀɴᴜᴀʟʟʏ ꜰᴏʀ ᴘʀᴏᴘᴇʀ ꜰᴜɴᴄᴛɪᴏɴɪɴɢ."
                    )
                try:
                    await client.join_chat("https://t.me/STORM_CORE")
                except:
                    pass
                try:
                    await client.join_chat("https://t.me/STORM_TECHH")
                except:
                    pass
            except Exception as e:
                LOGS.error(f"{i + 1}: {e}")
                continue

    async def load_plugin(self) -> None:
        """Load user plugins."""
        count = 0
        files = glob.glob("VXSTORM/plugins/user/*.py")
        unload = await db.get_env(ENV.unload_plugins) or ""
        unload = unload.split(" ")
        for file in files:
            with open(file) as f:
                path = Path(f.name)
                shortname = path.stem.replace(".py", "")
                if shortname in unload:
                    os.remove(Path(f"VXSTORM/plugins/user/{shortname}.py"))
                    continue
                if shortname.startswith("__"):
                    continue
                fpath = Path(f"VXSTORM/plugins/user/{shortname}.py")
                name = "VXSTORM.plugins.user." + shortname
                spec = importlib.util.spec_from_file_location(name, fpath)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["VXSTORM.plugins.user." + shortname] = load
                count += 1
            f.close()
        LOGS.info(
            f"{Symbols.bullet * 3} ʟᴏᴀᴅᴇᴅ ᴜꜱᴇʀ ᴘʟᴜɢɪɴ: '{count}' {Symbols.bullet * 3}"
        )

    async def validate_logger(self, client: Client) -> bool:
        """Validate if the client is in the logger group."""
        try:
            await client.get_chat_member(Config.LOGGER_ID, "me")
            return True
        except Exception:
            return await self.join_logger(client)

    async def join_logger(self, client: Client) -> bool:
        """Join the logger group."""
        try:
            invite_link = await self.bot.export_chat_invite_link(Config.LOGGER_ID)
            await client.join_chat(invite_link)
            return True
        except Exception:
            return False

    async def start_message(self, version: dict) -> None:
        """Send a startup message to the logger group."""
        await self.bot.send_message(
            Config.LOGGER_ID,
            f"**{Symbols.triangle_right}  ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ** `{version['pyrogram']}`\n"
            f"**{Symbols.triangle_right}  ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** `{version['python']}`\n\n",
            parse_mode=ParseMode.MARKDOWN,
            disable_notification=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/STORM_CORE"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/STORM_TECHH"),
                    ]
                ]
            ),
        )

    async def startup(self) -> None:
        """Start the bot and user clients."""
        LOGS.info(
            f"{Symbols.bullet * 3} ꜱᴛᴀʀᴛɪɴɢ VXSTORM ᴄʟɪᴇɴᴛ & ᴜꜱᴇʀ {Symbols.bullet * 3}"
        )
        await self.start_bot()
        await self.start_user()
        await self.load_plugin()


class CustomMethods(PbxClient):
    async def input(self, message: Message) -> str:
        """Get input from the user."""
        if len(message.command) < 2:
            output = ""
        else:
            try:
                output = message.text.split(" ", 1)[1].strip() or ""
            except IndexError:
                output = ""
        return output

    async def edit(
        self,
        message: Message,
        text: str,
        parse_mode: ParseMode = ParseMode.DEFAULT,
        no_link_preview: bool = True,
    ) -> Message:
        """Edit or reply to a message, if possible."""
        if message.from_user and message.from_user.id in Config.STAN_USERS:
            if message.reply_to_message:
                return await message.reply_to_message.reply_text(
                    text,
                    parse_mode=parse_mode,
                    disable_web_page_preview=no_link_preview,
                )
            return await message.reply_text(
                text, parse_mode=parse_mode, disable_web_page_preview=no_link_preview
            )
        return await message.edit_text(
            text, parse_mode=parse_mode, disable_web_page_preview=no_link_preview
        )

    async def _delete(self, message: Message, delay: int = 0) -> None:
        """Delete a message after a certain period of time."""
        await asyncio.sleep(delay)
        await message.delete()

    async def delete(
        self, message: Message, text: str, delete: int = 10, in_background: bool = True
    ) -> None:
        """Edit a message and delete it after a certain period of time."""
        to_del = await self.edit(message, text)
        if in_background:
            asyncio.create_task(self._delete(to_del, delete))
        else:
            await self._delete(to_del, delete)

    async def error(self, message: Message, text: str, delete: int = 10) -> None:
        """Edit an error message and delete it after a certain period of time if mentioned."""
        to_del = await self.edit(message, f"{Symbols.cross_mark} **ᴇʀʀᴏʀ:** \n\n{text}")
        if delete:
            asyncio.create_task(self._delete(to_del, delete))

    async def _log(self, tag: str, text: str, file: str = None) -> None:
        """Log a message to the logger group."""
        msg = f"**#{tag.upper()}**\n\n{text}"
        try:
            if file:
                try:
                    await self.bot.send_document(Config.LOGGER_ID, file, caption=msg)
                except:
                    await self.bot.send_message(
                        Config.LOGGER_ID, msg, disable_web_page_preview=True
                    )
            else:
                await self.bot.send_message(
                    Config.LOGGER_ID, msg, disable_web_page_preview=True
                )
        except Exception as e:
            raise Exception(f"{Symbols.cross_mark} ʟᴏɢᴇʀʀ: {e}")

    async def check_and_log(self, tag: str, text: str, file: str = None) -> None:
        """Check if:
        \n-> The logger group is available
        \n-> Logging is enabled"""
        status = await db.get_env(ENV.is_logger)
        if status and status.lower() == "true":
            await self._log(tag, text, file)


VXSTORM = CustomMethods()
