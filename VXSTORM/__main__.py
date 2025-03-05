from pyrogram import idle

from VXSTORM import __version__
from VXSTORM.core import (
    Config,
    ForcesubSetup,
    GachaBotsSetup,
    TemplateSetup,
    UserSetup,
    db,
    VXSTORM,
)
from VXSTORM.functions.tools import initialize_git
from VXSTORM.functions.utility import BList, Flood, TGraph


async def main():
    await VXSTORM.startup()  # Use the startup method
    await db.connect()
    await UserSetup()
    await ForcesubSetup()
    await GachaBotsSetup()
    await TemplateSetup()
    await Flood.updateFromDB()
    await BList.updateBlacklists()
    await TGraph.setup()
    await initialize_git(Config.PLUGINS_REPO)
    await VXSTORM.start_message(__version__)
    await idle()


if __name__ == "__main__":
    VXSTORM.run(main)  # Pass the coroutine function, not the result of calling it
