import random

from VXSTORM import __version__
from VXSTORM.core import ENV, db

ALIVE_TEMPLATES = [
    (
"⧼ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ‌🪽 ⧽\n"
"➖➖➖➖➖➖➖➖➖➖➖\n"
"• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ: 3.11.3\n"
"• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ: {pyrogram}\n"
"• ᴜᴘᴛɪᴍᴇ: {uptime}\n"
"• ᴜꜱᴇʀʙᴏᴛ ᴠ-ꜱᴛᴀᴛᴜꜱ: ᴠx 2.2@ᴘ+\n"
"➖➖➖➖➖➖➖➖➖➖➖\n"
"• ᴅᴇᴠ: [Kᴜɴᴀʟ !](https://t.me/ll_KEX_ll)\n"  
"• ᴘᴏᴡᴇʀᴇᴅ ʙʏ Ɵᴘᴜs\n"
"➖➖➖➖➖➖➖➖➖➖➖\n"                     
        ),
]

PING_TEMPLATES = [
    """**❏ ꜱ ᴛ ᴏ ʀ ᴍ ⚡**
**├•** **ꜱᴛᴀᴛᴜꜱ: ᴀᴄᴛɪᴠᴇ**
**├•** **ʀᴇꜱᴘᴏɴꜱᴇ ᴛɪᴍᴇ:** {speed} ᴍꜱ
**├•** **ᴜᴘᴛɪᴍᴇ:** {uptime}
**├•** **ᴏᴡɴᴇʀ:** {owner} 
**├•** **ᴠᴇʀꜱɪᴏɴ:** ᴠx 2.2@ᴘ+
**└•** **ᴘᴏᴡᴇʀᴇᴅ ʙʏ Ɵᴘᴜs 🤖**""",
]

HELP_MENU_TEMPLATES = [
    """**•─╼⃝𖠁 ᴠx ʜᴇʟᴘ ᴍᴇɴᴜ 𖠁⃝╾─•**

**📃 ʟᴏᴀᴅᴇᴅ**{plugins} ᴍᴏᴅᴜʟᴇꜱ**
**✨ ᴛᴏᴛᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ**{commands}

**📑 ᴘᴀɢᴇ:** __{current}/{last}__""",
]

COMMAND_MENU_TEMPLATES = [
    """**ᴘʟᴜɢɪɴ ꜰɪʟᴇ:** `{file}`
**ᴘʟᴜɢɪɴ ɪɴꜰᴏ:** __{info} 🍀__

**📃 ʟᴏᴀᴅᴇᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{commands}`""",
]

ANIME_TEMPLATES = [
    """
{name}

╭────────────────•
╰• **ꜱᴄᴏʀᴇ:** `{score}`
╰• **ꜱᴏᴜʀᴄᴇ:** `{source}`
╰• **ᴛʏᴘᴇ:** `{mtype}`
╰• **ᴇᴘɪꜱᴏᴅᴇꜱ:** `{episodes}`
╰• **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration} ᴍɪɴᴜᴛᴇꜱ`
╰• **ꜱᴛᴀᴛᴜꜱ:** `{status}`
╰• **ꜰᴏʀᴍᴀᴛ:** `{format}`
╰• **ɢᴇɴʀᴇ:** `{genre}`
╰• **ᴛᴀɢꜱ:** `{tags}`
╰• **ᴀᴅᴜʟᴛ ʀᴀᴛᴇᴅ:** `{isAdult}`
╰• **ꜱᴛᴜᴅɪᴏ:** `{studio}`
╰• **ᴛʀᴀɪʟᴇʀ:** {trailer}
╰• **ᴡᴇʙꜱɪᴛᴇ:** {siteurl}
╰• **ꜱʏɴᴏᴘꜱɪꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({description})
╰────────────────•
"""
]

MANGA_TEMPLATES = [
    """
{name}

╭────────────────•
╰• **ꜱᴄᴏʀᴇ:** `{score}`
╰• **ꜱᴏᴜʀᴄᴇ:** `{source}`
╰• **ᴛʏᴘᴇ:** `{mtype}`
╰• **ᴄʜᴀᴘᴛᴇʀꜱ:** `{chapters}`
╰• **ᴠᴏʟᴜᴍᴇꜱ:** `{volumes}`
╰• **ꜱᴛᴀᴛᴜꜱ:** `{status}`
╰• **ꜰᴏʀᴍᴀᴛ:** `{format}`
╰• **ɢᴇɴʀᴇ:** `{genre}`
╰• **ᴀᴅᴜʟᴛ ʀᴀᴛᴇᴅ:** `{isAdult}`
╰• **ᴡᴇʙꜱɪᴛᴇ:** {siteurl}
╰• **ꜱʏɴᴏᴘꜱɪꜱ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({description})
╰────────────────•
"""
]

CHARACTER_TEMPLATES = [
    """
{name}

╭────────────────•
╰• **ɢᴇɴᴅᴇʀ:** `{gender}`
╰• **ᴅᴀᴛᴇ ᴏꜰ ʙɪʀᴛʜ:** `{date_of_birth}`
╰• **ᴀɢᴇ:** `{age}`
╰• **ʙʟᴏᴏᴅ ᴛʏᴘᴇ:** `{blood_type}`
╰• **ꜰᴀᴠᴏᴜʀɪᴛᴇꜱ:** `{favorites}`
╰• **ᴡᴇʙꜱɪᴛᴇ:** {siteurl}{role_in}
╰────────────────•
{description}
"""
]

AIRING_TEMPLATES = [
    """
{name}

╭────────────────•
╰• **ꜱᴛᴀᴛᴜꜱ:** `{status}`
╰• **ᴇᴘɪꜱᴏᴅᴇ:** `{episode}`
╰────────────────•{airing_info}
"""
]

ANILIST_USER_TEMPLATES = [
    """
**💫 {name}**

╭──── ᴀɴɪᴍᴇ ─────•
╰• **ᴄᴏᴜɴᴛ:** `{anime_count}`
╰• **ꜱᴄᴏʀᴇ:** `{anime_score}`
╰• **ᴍɪɴᴜᴛᴇꜱ ꜱᴘᴇɴᴛ:** `{minutes}`
╰• **ᴇᴘɪꜱᴏᴅᴇꜱ ᴡᴀᴛᴄʜᴇᴅ:** `{episodes}`
╰────────────────•
╭──── ᴍᴀɴɢᴀ ─────•
╰• **ᴄᴏᴜɴᴛ:** `{manga_count}`
╰• **ꜱᴄᴏʀᴇ:** `{manga_score}`
╰• **ᴄʜᴀᴘᴛᴇʀꜱ:** `{chapters}`
╰• **ᴠᴏʟᴜᴍᴇꜱ:** `{volumes}`
╰────────────────•

ᴡᴇʙꜱɪᴛᴇ: {siteurl}
"""
]

CLIMATE_TEMPLATES = [
    """
🌆 {city_name}, {country}

╭────────────────•
╰• **ᴡᴇᴀᴛʜᴇʀ:** {weather}
╰• **ᴛɪᴍᴇᴢᴏɴᴇ:** {timezone}
╰• **ꜱᴜɴʀɪꜱᴇ:** {sunrise}
╰• **ꜱᴜɴꜱᴇᴛ:** {sunset}
╰• **ᴡɪɴᴅ:** {wind}
╰• **ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ:** {temperature}°C
╰• **ꜰᴇᴇʟꜱ ʟɪᴋᴇ:** {feels_like}°C
╰• **ᴍɪɴɪᴍᴜᴍ:** {temp_min}°C
╰• **ᴍᴀxɪᴍᴜᴍ:** {temp_max}°C
╰• **ᴘʀᴇꜱꜱᴜʀᴇ:** {pressure} ʜPᴀ
╰• **ʜᴜᴍɪᴅɪᴛʏ:** {humidity}%
╰• **ᴠɪꜱɪʙɪʟɪᴛʏ:** {visibility} ᴍ
╰• **ᴄʟᴏᴜᴅꜱ:** {clouds}%
╰────────────────•
"""
]

AIR_POLLUTION_TEMPLATES = [
    """
🌆 {city_name}

╭────────────────•
╰• **ᴀQɪ:** {aqi}
╰• **ᴄᴀʀʙᴏɴ ᴍᴏɴᴏxɪᴅᴇ:** {co}
╰• **ɴᴏɪᴛʀᴏɢᴇɴ ᴍᴏɴᴏxɪᴅᴇ:** {no}
╰• **ɴɪᴛʀᴏɢᴇɴ ᴅɪᴏxɪᴅᴇ:** {no2}
╰• **ᴏᴢᴏɴᴇ:** {o3}
╰• **ꜱᴜʟᴘʜᴜʀ ᴅɪᴏxɪᴅᴇ:** {so2}
╰• **ᴀᴍᴍᴏɴɪᴀ:** {nh3}
╰• **ꜰɪɴᴇ ᴘᴀʀᴛɪᴄʟᴇꜱ (PM{sub2_5}):** {pm2_5}
╰• **ᴄᴏᴀʀꜱᴇ ᴘᴀʀᴛɪᴄʟᴇꜱ (PM{sub10}):** {pm10}
╰────────────────•
"""
]

GITHUB_USER_TEMPLATES = [
    """
🍀 {username} ({git_id})

╭──────── {id_type} ────────•
╰• **ɴᴀᴍᴇ:** [{name}]({profile_url})
╰• **ʙʟᴏɢ:** {blog}
╰• **ᴄᴏᴍᴘᴀɴʏ:** {company}
╰• **ᴇᴍᴀɪʟ:** {email}
╰• **ʟᴏᴄᴀᴛɪᴏɴ:** {location}
╰• **ʀᴇᴘᴏ:** {public_repos}
╰• **ɢɪꜱᴛꜱ:** {public_gists}
╰• **ꜰᴏʟʟᴏᴡᴇʀꜱ:** {followers}
╰• **ꜰᴏʟʟᴏᴡɪɴɢ:** {following}
╰• **ᴀᴄᴄᴏᴜɴᴛ ᴄʀᴇᴀᴛᴇᴅ:** {created_at}
╰────────────────•

**💫 ʙɪᴏ:** {bio}
"""
]

STATISTICS_TEMPLATES = [
    """
🍀 {name}

╭──────── ᴄʜᴀɴɴᴇʟꜱ ────────•
╰• **ᴛᴏᴛᴀʟ:** `{channels}`
╰• **ᴀᴅᴍɪɴ:** `{ch_admin}`
╰• **ᴏᴡɴᴇʀ:** `{ch_owner}`

╭──────── ɢʀᴏᴜᴘꜱ ────────•
╰• **ᴛᴏᴛᴀʟ:** `{groups}`
╰• **ᴀᴅᴍɪɴ:** `{gc_admin}`
╰• **ᴏᴡɴᴇʀ:** `{gc_owner}`

╭──────── ᴏᴛʜᴇʀꜱ ────────•
╰• **ᴘʀɪᴠᴀᴛᴇ:** `{users}`
╰• **ʙᴏᴛꜱ:** `{bots}`
╰• **ᴜɴʀᴇᴀᴅ ᴍᴇꜱꜱᴀɢᴇꜱ:** `{unread_msg}`
╰• **ᴜɴʀᴇᴀᴅ ᴍᴇɴᴛɪᴏɴꜱ:** `{unread_mention}`

⌛ **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** `{time_taken}`
"""
]

GBAN_TEMPLATES = [
    """
╭──────── {gtype} ────────•
╰• **ᴠɪᴄᴛɪᴍ:** {name}
╰• **ꜱᴜᴄᴄᴇꜱꜱ:** {success}
╰• **ꜰᴀɪʟᴇᴅ:** {failed}
╰• **ʀᴇᴀꜱᴏɴ:** {reason}
╰────────────────•
"""
]

USAGE_TEMPLATES = [
    """
**📝 ᴅɪꜱᴋ & ᴅʏɴᴏ ᴜꜱᴀɢᴇ:**

**• ᴅʏɴᴏ ᴜꜱᴀɢᴇ ꜰᴏʀ** `{appName}`
    • __{appHours}ʜʀꜱ {appMinutes}ᴍɪɴꜱ__ | __{appPercentage}%__

**• ᴅʏɴᴏ ʀᴇᴍᴀɪɴɪɴɢ ᴛʜɪꜱ ᴍᴏɴᴛʜ:**
    • __{hours}ʜʀꜱ {minutes}ᴍɪɴꜱ__ | __{percentage}%__

**• ᴅɪꜱᴋ ᴜꜱᴀɢᴇ:**
    • __{diskUsed}ɢʙ__ / __{diskTotal}ɢʙ__ | __{diskPercent}%__

**• ᴍᴇᴍᴏʀʏ ᴜꜱᴀɢᴇ:**
    • __{memoryUsed}ɢʙ__ / __{memoryTotal}ɢʙ__ | __{memoryPercent}%__
"""
]

USER_INFO_TEMPLATES = [
    """
**🍀 ᴜꜱᴇʀ ɪɴꜰᴏ ᴏꜰ {mention}:**

**• ꜰɪʀꜱᴛ ɴᴀᴍᴇ:** `{firstName}`
**• ʟᴀꜱᴛ ɴᴀᴍᴇ:** `{lastName}`
**• ᴜꜱᴇʀɪᴅ:** `{userId}`

**• ᴄᴏᴍᴍᴏɴ ɢʀᴏᴜᴘꜱ:** `{commonGroups}`
**• ᴅᴄ-ɪᴅ:** `{dcId}`
**• ᴘɪᴄᴛᴜʀᴇꜱ:** `{totalPictures}`
**• ʀᴇꜱᴛʀɪᴄᴛᴇᴅ:** `{isRestricted}`
**• ᴠᴇʀɪꜰɪᴇᴅ:** `{isVerified}`
**• ʙᴏᴛ:** `{isBot}`
**• ʙɪᴏ:** `{bio}`

**@VXSTORM_BOT**
"""
]

CHAT_INFO_TEMPLATES = [
    """
**🍀 ᴄʜᴀᴛ ɪɴꜰᴏ:**

**• ᴄʜᴀᴛ ɴᴀᴍᴇ:** `{chatName}`
**• ᴄʜᴀᴛ ɪᴅ:** `{chatId}`
**• ᴄʜᴀᴛ ʟɪɴᴋ:** {chatLink}
**• ᴏᴡɴᴇʀ:** {chatOwner}
**• ᴅᴄ-ɪᴅ:** `{dcId}`
**• ᴍᴇᴍʙᴇʀꜱ:** `{membersCount}`
**• ᴀᴅᴍɪɴꜱ:** `{adminsCount}`
**• ʙᴏᴛꜱ:** `{botsCount}`
**• ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ:** `{description}`

**@VXSTORM_BOT**
"""
]


async def alive_template(owner: str, uptime: str) -> str:
    template = await db.get_env(ENV.alive_template)
    if template:
        message = template
    else:
        message = random.choice(ALIVE_TEMPLATES)
    return message.format(
        owner=owner,
        pyrogram=__version__["pyrogram"],
        VXSTORM=__version__["VXSTORM"],
        python=__version__["python"],
        uptime=uptime,
    )


async def ping_template(speed: float, uptime: str, owner: str) -> str:
    template = await db.get_env(ENV.ping_template)
    if template:
        message = template
    else:
        message = random.choice(PING_TEMPLATES)
    return message.format(speed=speed, uptime=uptime, owner=owner)


async def help_template(
    owner: str, cmd_n_plgn: tuple[int, int], page: tuple[int, int]
) -> str:
    template = await db.get_env(ENV.help_template)
    if template:
        message = template
    else:
        message = random.choice(HELP_MENU_TEMPLATES)
    return message.format(
        owner=owner,
        commands=cmd_n_plgn[0],
        plugins=cmd_n_plgn[1],
        current=page[0],
        last=page[1],
    )


async def command_template(file: str, info: str, commands: str) -> str:
    template = await db.get_env(ENV.command_template)
    if template:
        message = template
    else:
        message = random.choice(COMMAND_MENU_TEMPLATES)
    return message.format(file=file, info=info, commands=commands)


async def anime_template(**kwargs) -> str:
    template = await db.get_env(ENV.anime_template)
    if template:
        message = template
    else:
        message = random.choice(ANIME_TEMPLATES)
    return message.format(**kwargs)


async def manga_templates(**kwargs) -> str:
    template = await db.get_env(ENV.manga_template)
    if template:
        message = template
    else:
        message = random.choice(MANGA_TEMPLATES)
    return message.format(**kwargs)


async def character_templates(**kwargs) -> str:
    template = await db.get_env(ENV.character_template)
    if template:
        message = template
    else:
        message = random.choice(CHARACTER_TEMPLATES)
    return message.format(**kwargs)


async def airing_templates(**kwargs) -> str:
    template = await db.get_env(ENV.airing_template)
    if template:
        message = template
    else:
        message = random.choice(AIRING_TEMPLATES)
    return message.format(**kwargs)


async def anilist_user_templates(
    name: str, anime: tuple, manga: tuple, siteurl: str
) -> str:
    template = await db.get_env(ENV.anilist_user_template)
    if template:
        message = template
    else:
        message = random.choice(ANILIST_USER_TEMPLATES)
    return message.format(
        name=name,
        anime_count=anime[0],
        anime_score=anime[1],
        minutes=anime[2],
        episodes=anime[3],
        manga_count=manga[0],
        manga_score=manga[1],
        chapters=manga[2],
        volumes=manga[3],
        siteurl=siteurl,
    )


async def climate_templates(**kwargs) -> str:
    template = await db.get_env(ENV.climate_template)
    if template:
        message = template
    else:
        message = random.choice(CLIMATE_TEMPLATES)
    return message.format(**kwargs)


async def airpollution_templates(**kwargs) -> str:
    template = await db.get_env(ENV.airpollution_template)
    if template:
        message = template
    else:
        message = random.choice(AIR_POLLUTION_TEMPLATES)
    return message.format(**kwargs)


async def statistics_templates(**kwargs) -> str:
    template = await db.get_env(ENV.statistics_template)
    if template:
        message = template
    else:
        message = random.choice(STATISTICS_TEMPLATES)
    return message.format(**kwargs)


async def github_user_templates(**kwargs) -> str:
    template = await db.get_env(ENV.github_user_template)
    if template:
        message = template
    else:
        message = random.choice(GITHUB_USER_TEMPLATES)
    return message.format(**kwargs)


async def gban_templates(**kwargs) -> str:
    template = await db.get_env(ENV.gban_template)
    if template:
        message = template
    else:
        message = random.choice(GBAN_TEMPLATES)
    return message.format(**kwargs)


async def usage_templates(**kwargs) -> str:
    template = await db.get_env(ENV.usage_template)
    if template:
        message = template
    else:
        message = random.choice(USAGE_TEMPLATES)
    return message.format(**kwargs)


async def user_info_templates(**kwargs) -> str:
    template = await db.get_env(ENV.user_info_template)
    if template:
        message = template
    else:
        message = random.choice(USER_INFO_TEMPLATES)
    return message.format(**kwargs)


async def chat_info_templates(**kwargs) -> str:
    template = await db.get_env(ENV.chat_info_template)
    if template:
        message = template
    else:
        message = random.choice(CHAT_INFO_TEMPLATES)
    return message.format(**kwargs)
