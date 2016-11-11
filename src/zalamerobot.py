#!/usr/bin/python3

import logging
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram
import listapiropos
import grcanosasettings as GRS;
import emoiji

def start(bot : telegram.Bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

    



def get_piropo():
    return random.choice(listapiropos.PIROPOSLIST)


def resp_piropo(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text=get_piropo());


def resp_trafico(bot,update):
    bot.sendMessage(chat_id=GRS.cid_gonzalo,text=emoji.emojize(':car:', use_aliases=True))
    bot.sendMessage(chat_id=GRS.cid_sara,text=emoji.emojize(':car:', use_aliases=True))




log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_format,level=logging.INFO)

updater = Updater(token=GRS.TOKEN)

dispatcher = updater.dispatcher

h_start = CommandHandler('start', start)
h_piropo = CommandHandler('dimealgobonito',resp_piropo)
h_trafico = CommandHandler('trafico',resp_trafico)

dispatcher.add_handler(h_start)
dispatcher.add_handler(h_piropo)
dispatcher.add_handler(h_trafico)

updater.start_polling()
updater.idle()
