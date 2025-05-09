import sys
#from .clients import VXSTORM
from .clients import VXSTORM
from .config import Config, Symbols
from .database import db
from .logger import LOGS


async def _AuthUsers() -> None:
    temp_list = []
    temp_list.append(Config.OWNER_ID)
    temp_list.extend([(await client.get_me()).id for client in VXSTORM.users])

    stan_users = await db.get_all_stans()
    for user in stan_users:
        temp_list.append(user["user_id"])

    users = list(set(temp_list))
    for user in users:
        Config.AUTH_USERS.add(user)

    temp_list = None
    LOGS.info(
        f"{Symbols.arrow_right * 2} ᴀᴅᴅᴇᴅ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜꜱᴇʀꜱ {Symbols.arrow_left * 2}"
    )


async def _StanUsers() -> None:
    users = await db.get_all_stans()
    for user in users:
        Config.STAN_USERS.add(user["user_id"])

    LOGS.info(f"{Symbols.arrow_right * 2} ᴀᴅᴅᴇᴅ ꜱᴛᴀɴ ᴜꜱᴇʀꜱ {Symbols.arrow_left * 2}")


async def _GbanUsers() -> None:
    users = await db.get_gban()
    for user in users:
        Config.BANNED_USERS.add(user["user_id"])

    LOGS.info(
        f"{Symbols.arrow_right * 2} ᴀᴅᴅᴇᴅ {len(users)} ɢʙᴀɴɴᴇᴅ ᴜꜱᴇʀꜱ {Symbols.arrow_left * 2}"
    )

    musers = await db.get_gmute()
    for user in musers:
        Config.MUTED_USERS.add(user["user_id"])

    LOGS.info(
        f"{Symbols.arrow_right * 2} ᴀᴅᴅᴇᴅ {len(musers)} ɢᴍᴜᴛᴇᴅ ᴜꜱᴇʀꜱ {Symbols.arrow_left * 2}"
    )


async def UserSetup() -> None:
    """ɪɴɪᴛɪᴀʟɪᴢᴇ ᴜꜱᴇʀꜱ ᴄᴏɴꜰɪɢ"""
    LOGS.info(f"{Symbols.bullet * 3} ꜱᴇᴛᴛɪɴɢ ᴜᴘ ᴜꜱᴇʀꜱ {Symbols.bullet * 3}")
    await _AuthUsers()
    await _StanUsers()
    await _GbanUsers()


async def ForcesubSetup() -> None:
    """ɪɴɪᴛɪᴀʟɪᴢᴇ ꜰᴏʀᴄᴇꜱᴜʙ ᴄᴏɴꜰɪɢ"""
    chats = await db.get_all_forcesubs()
    for chat in chats:
        if chat not in Config.FORCESUBS:
            Config.FORCESUBS.add(chat["chat"])


async def GachaBotsSetup() -> None:
    """ɪɴɪᴛɪᴀʟɪᴢᴇ ɢᴀᴄʜᴀʙᴏᴛꜱ ᴄᴏɴꜰɪɢ"""
    bots = await db.get_all_gachabots_id()
    for bot in bots:
        Config.GACHA_BOTS.add(bot)


async def TemplateSetup() -> None:
    """ɪɴɪᴛɪᴀʟɪᴢᴇ ᴛᴇᴍᴘʟᴀᴛᴇꜱ ᴄᴏɴꜰɪɢ"""
    module_name = "temp_module"
    module = sys.modules.get(module_name)
    if module is None:
        module = type(sys)(module_name)

    with open("VXSTORM/functions/templates.py", "r", encoding="utf-8") as file:
        exec(file.read(), module.__dict__)

    global_vars = module.__dict__

    var_n_value: dict[str, str] = {
        var_name: global_vars[var_name][0]
        for var_name in global_vars
        if var_name.isupper() and not callable(global_vars[var_name])
    }

    Config.TEMPLATES = var_n_value
