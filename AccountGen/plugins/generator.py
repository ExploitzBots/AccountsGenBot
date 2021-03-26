#    AccountsGenBot
#    Copyright (C) 2021 xditya

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/xditya/AccountsGenBot/blob/master/LICENSE > 
#    for the license.

import random
from . import *
from telethon.tl.functions.users import GetFullUserRequest

@BotzHub.on(events.callbackquery.CallbackQuery(data="gen"))
async def gen(event):
    if not (await check_user(event.sender_id)):
        return await event.reply(f"{strt}\n\nOops! You need to join my channel so as to use me!", buttons=[Button.url("Join My Channel", url=ltc)])
    acc = random.choice(listofaccs)
    accn, pasw = acc.split(":")
    xxx = await BotzHub(GetFullUserRequest(event.sender_id))
    botname = (await BotzHub.get_me()).username
    if ACC_NAME is None:
        acnme = ""
    else:
        acnme = ACC_NAME
    await event.edit("""
**Here is your {} account!**

**User** - `{}`
**Password** - `{}`

**Generated by** `{}` **via @{}**""".format(acnme, accn, pasw, xxx.user.first_name, botname),
buttons=[
    [Button.url("Channel", url=ltc), Button.url("Bot", url=f"https://t.me/{botname}")],
])
