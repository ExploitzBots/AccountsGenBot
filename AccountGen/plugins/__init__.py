#    AccountsGenBot
#    Copyright (C) 2021 xditya

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/xditya/AccountsGenBot/blob/master/LICENSE > 
#    for the license.

from telethon import events, Button
from .. import *
from AccountGen import *
import requests
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest

with open('hits.txt') as f:
    xd = f.read().splitlines()
    sed = random.choice(xd)
    email, password = sed.split(":")

async def check_user(id):
    if CHANNEL is None:     # incase no join check is needed
        return True
    ok = True
    try:
        await BotzHub(GetParticipantRequest(channel=CHANNEL, user_id=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok

if CHANNEL.startswith('@'):
    x = CHANNEL.split('@')[1]
    ltc = f"https://t.me/{x}"
else:
    ltc = CHANNEL
