import io
import re
import subprocess
import sys
import traceback

import bs4
import requests
from pyrogram import Client
from pyrogram.errors import MessageTooLong
from pyrogram.types import Message
from speedtest import Speedtest

from . import *


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


@on_message("eval", allow_stan=True)
async def runeval(client: Client, message: Message):
    if len(message.command) < 2:
        return await VXSTORM.delete(message, "ɴᴏ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇ ᴘʀᴏᴠɪᴅᴇᴅ!")
    reply_to = message.reply_to_message or message

    code = await VXSTORM.input(message)
    Pbx = await VXSTORM.edit(message, "ʀᴜɴɴɪɴɢ")

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(code, client, message)
    except Exception:
        exc = traceback.format_exc()

    evaluation = ""
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    heading = f"**ᴇᴠᴀʟ:**\n```ᴘʏᴛʜᴏɴ\n{code}```\n\n"
    output = f"**ᴏᴜᴛᴘᴜᴛ:**\n`{evaluation.strip()}`"
    final_output = heading + output

    try:
        await reply_to.reply_text(final_output, disable_web_page_preview=True)
    except MessageTooLong:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "eval.txt"
            await reply_to.reply_document(out_file, caption=heading)

    await Pbx.delete()


@on_message(["exec", "term"], allow_stan=True)
async def runterm(client: Client, message: Message):
    if len(message.command) < 2:
        return await VXSTORM.delete(message, "ɴᴏ ꜱʜᴇʟʟ ᴄᴏᴅᴇ ᴘʀᴏᴠɪᴅᴇᴅ!")

    reply_to = message.reply_to_message or message

    cmd = await VXSTORM.input(message)
    Pbx = await VXSTORM.edit(message, "ʀᴜɴɴɪɴɢ")

    if "\n" in cmd:
        code = cmd.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            except Exception as err:
                print(err)
                await Pbx.edit(f"**ᴇʀʀᴏʀ:** \n`{err}`")
            output += f"**{code}**\n"
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", cmd)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(exc_type, exc_obj, exc_tb)
            await Pbx.edit("**ᴇʀʀᴏʀ:**\n`{}`".format("".join(errors)))
            return
        output = process.stdout.read()[:-1].decode("utf-8")

    if str(output) == "\n":
        return await Pbx.edit(f"**ᴏᴜᴛᴘᴜᴛ:** ____")
    else:
        try:
            await reply_to.reply_text(
                f"**{client.me.id}@VXSTORM:~$** `{cmd}`\n\n**ᴏᴜᴛᴘᴜᴛ:**\n```\n{output}```"
            )
        except MessageTooLong:
            with io.BytesIO(str.encode(output)) as out_file:
                out_file.name = "exec.txt"
                await reply_to.reply_document(
                    out_file,
                    caption=f"**{client.me.id}@VXSTORM:~$** `{cmd}`",
                )

    await Pbx.delete()


@on_message(["sh", "shell"], allow_stan=True)
async def runshell(_, message: Message):
    if len(message.command) < 2:
        return await VXSTORM.delete(message, "ɴᴏ ꜱʜᴇʟʟ ᴄᴏᴅᴇ ᴘʀᴏᴠɪᴅᴇᴅ!")

    code = await VXSTORM.input(message)
    Pbx = await VXSTORM.edit(message, "ʀᴜɴɴɪɴɢ")

    result = subprocess.run(code, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr

    heading = f"**ꜱʜᴇʟʟ:**\n```sh\n{code}```\n\n"
    output = f"**ᴏᴜᴛᴘᴜᴛ:**\n`{output.strip()}`"
    final_output = heading + output

    try:
        await message.reply_text(final_output, disable_web_page_preview=True)
    except MessageTooLong:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "shell.txt"
            await message.reply_document(out_file, caption=heading)

    await Pbx.delete()


@on_message("fext", allow_stan=True)
async def file_extention(_, message: Message):
    BASE_URL = "https://www.fileext.com/file-extension/{0}.html"
    if len(message.command) < 2:
        return await VXSTORM.delete(message, "ɴᴏ ꜰɪʟᴇ ᴇxᴛᴇɴᴛɪᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ!")

    extention = message.command[1]
    Pbx = await VXSTORM.edit(message, "ɢᴇᴛᴛɪɴɢ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ...")

    response = requests.get(BASE_URL.format(extention))
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        details = soup.find_all("td", {"colspan": "3"})[-1].text
        await Pbx.edit(f"**ꜰɪʟᴇ ᴇxᴛᴇɴᴛɪᴏɴ:** `{extention}`\n\n**ᴅᴇᴛᴀɪʟꜱ:**\n`{details}`")
    else:
        await Pbx.edit(f"**ꜰɪʟᴇ ᴇxᴛᴇɴᴛɪᴏɴ:** `{extention}`\n\n**ᴅᴇᴛᴀɪʟꜱ:**\n`0`")


@on_message("pypi", allow_stan=True)
async def pypi(_, message: Message):
    BASE_URL = "https://pypi.org/pypi/{0}/json"
    if len(message.command) < 2:
        return await VXSTORM.delete(message, "ɴᴏ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ᴘʀᴏᴠɪᴅᴇᴅ!")

    package = message.command[1]
    Pbx = await VXSTORM.edit(message, "ʀᴜɴɴɪɴɢ")

    response = requests.get(BASE_URL.format(package))
    if response.status_code == 200:
        data = response.json()
        info = data["info"]
        name = info["name"]
        url = info["package_url"]
        version = info["version"]
        summary = info["summary"]
        await Pbx.edit(f"**ᴘᴀᴄᴋᴀɢᴇ:** [{name}]({url}) (`{version}`)\n\n**ᴅᴇᴛᴀɪʟꜱ:** `{summary}`")
    else:
        await Pbx.edit(f"**ᴘᴀᴄᴋᴀɢᴇ:** `{package}`\n\n**ᴅᴇᴛᴀɪʟꜱ:** `0`")
