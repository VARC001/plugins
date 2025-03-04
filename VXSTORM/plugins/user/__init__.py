from pyrogram.enums import ChatType

from VXSTORM.core.clients import VXSTORM
from VXSTORM.core.config import Config, Symbols
from VXSTORM.core.database import db
from VXSTORM.plugins.decorator import custom_handler, on_message
#from VXSTORM.plugins.help import HelpMenu

handler = Config.HANDLERS[0]
bot = VXSTORM

spam_chats = []

bot_only = [ChatType.BOT]
group_n_channel = [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]
group_only = [ChatType.GROUP, ChatType.SUPERGROUP]
private_n_bot = [ChatType.PRIVATE, ChatType.BOT]
private_only = [ChatType.PRIVATE]
