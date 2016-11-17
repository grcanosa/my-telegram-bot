#!/usr/bin/python3

import random;
import logging;

import emoji
import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler as CH;
from ..data import peopleemoji as LPEOPLEEMOJI;


class CmdCollection:
    def __init__(self,userReg,priority = 50):
        self._cmd_list = [];
        self._user_reg = userReg;
        self._priority = priority;


    def add_cmd(self,dispatcher,cmdprocessor):
        self._cmd_list.append(cmdprocessor);
        dispatcher.add_handler(CH(cmdprocessor.get_cmd(),self.proc_phrase),self._priority);

    def proc_phrase(self,bot,update):
        logging.debug("Received: %s",update.message.text);
        added = False;
        for cmdproc in self._cmd_list:
            if cmdproc.process(self._user_reg,bot,update):
                added = True;
                break;
        if not added:
            text = "Command not defined yet! ";
            catcry= emoji.emojize(":crying_cat_face:",use_aliases=True);
            text += (catcry*4)
            bot.send_message(chat_id=update.message.chat_id,text=text);
