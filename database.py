import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

VX = getenv("VX", "mongodb+srv://strvortexcore:vortexcore0019@cluster0.fkb3o.mongodb.net/?retryWrites=true&w=majority")
