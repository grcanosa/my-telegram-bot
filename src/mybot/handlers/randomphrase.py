#!/usr/bin/python3

import random;
import logging;

import emoji
import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler as CH;
from ..data import peopleemoji as LPEOPLEEMOJI;


class RandomPhrase:
    def __init__(self,userReg):
        self._cmd_list = [];
        self._user_reg = userReg;


    def add_cmd(self,dispatcher,phraselist, priority=1):
        self._cmd_list.append(phraselist);
        dispatcher.add_handler(CH(phraselist.get_cmd(),self.proc_phrase),priority);

    def proc_phrase(self,bot,update):
        logging.debug("Received: %s",update.message.text);
        added = False;
        for phraselist in self._cmd_list:
            if phraselist.process(self._user_reg,bot,update):
                added = True;
                break;
        if not added:
            text = "Command not defined yet! ";
            catcry= emoji.emojize(":crying_cat_face:",use_aliases=True);
            text += (catcry*4)
            bot.send_message(chat_id=update.message.chat_id,text=text);
