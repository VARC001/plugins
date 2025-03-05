from pyrogram import Client, filters
from . import *
from bs4 import BeautifulSoup
from googlesearch import search
import requests
from pyrogram.types import Message

def googlesearch(query):
    co = 1
    returnquery = {}

    for j in search(query, num_results=10):  # Removed 'tld' and updated syntax
        url = str(j)
        
        try:
            response = requests.get(url, timeout=5)  # Added timeout
            response.raise_for_status()
        except requests.exceptions.RequestException:
            continue  # Skip if request fails

        soup = BeautifulSoup(response.text, "html.parser")
        site_title = soup.title.string if soup.title else "ɴᴏ ᴛɪᴛʟᴇ"

        meta_description = "ɴᴏ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ."
        meta_tag = soup.find("meta", attrs={"name": "description"})
        if meta_tag and "content" in meta_tag.attrs:
            meta_description = meta_tag.attrs["content"]

        returnquery[co] = {
            "title": site_title,
            "metadata": meta_description,
            "url": j,
        }
        co += 1

    return returnquery

@on_message(["gs", "google"], allow_stan=True)
async def gs(client: Client, message: Message):
    Man = await message.edit("🔍 **ꜱᴇᴀʀᴄʜɪɴɢ...**")
    msg_txt = message.text.strip()
    
    if " " not in msg_txt:
        await Man.edit("❌ **ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ꜱᴇᴀʀᴄʜ ǫᴜᴇʀʏ!**")
        return

    query = msg_txt.split(" ", 1)[1]
    results = googlesearch(query)

    returnmsg = ""
    for i in range(1, 11):  # Loop for 10 results
        presentquery = results.get(i, {})
        presenttitle = presentquery.get("title", "ɴᴏ ᴛɪᴛʟᴇ")
        presentmeta = presentquery.get("metadata", "ɴᴏ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ.")
        presenturl = presentquery.get("url", "")

        returnmsg += f"🔹 [{presenttitle}]({presenturl})\n➡️ {presentmeta}\n\n"

    if not returnmsg:
        returnmsg = "❌ **ɴᴏ ʀᴇꜱᴜʟᴛꜱ ꜰᴏᴜɴᴅ.**"

    await Man.edit(returnmsg, disable_web_page_preview=True)
