import asyncio
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
    # Initialize the VXSTORM client
    client = VXSTORM()

    # Perform startup tasks
    await client.startup()  # Use the startup method
    await db.connect()
    await UserSetup()
    await ForcesubSetup()
    await GachaBotsSetup()
    await TemplateSetup()
    await Flood.updateFromDB()
    await BList.updateBlacklists()
    await TGraph.setup()
    await initialize_git(Config.PLUGINS_REPO)
    await client.start_message(__version__)

    # Keep the client running
    await idle()


if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
