#!/usr/bin/python3


import telegram
import listapiropos


TOKEN='299955644:AAEBQY-7kb0PkC4LOfpirIzKi71RGnDoIBw'

bot=telegram.Bot(token=TOKEN)

chat_id=15111383

bot.sendMessage(chat_id=chat_id, text="PIROPO"+listapiropos.PIROPOSLIST[1])

updates = bot.getUpdates()

print([u.message.chat_id for u in updates])