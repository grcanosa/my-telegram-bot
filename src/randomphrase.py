#!/usr/bin/python3

import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler as CH;
import random;

class PhraseList:
    def __init__(self,cmd,list):
        self._cmd = cmd;
        self._list = list;

    def get_random_phrase(self):
        return random.choice(self._list);

    def cmd_ok(self,text):
        return self._cmd in text;

    def get_cmd(self):
        return self._cmd;



class RandomPhrase:
    def __init__(self):
        self._cmd_list = [];


    def add_cmd(self,dispatcher,phraselist, priority=1):
        self._cmd_list.append(phraselist);
        dispatcher.add_handler(CH(phraselist.get_cmd,self.proc_phrase),priority);

    def proc_phrase(self,bot,update):
        text = update.message.from_user.first_name.split()[0]+": ";
        added = False;
        for phraselist in self._cmd_list:
            if phraselist.cmd_ok(update.message.text):
                text+=phraselist.get_random_phrase();
                added = True;
                break;
        if not added:
            text += "NOT UNDERSTAND";
        bot.send_message(chat_id=update.message.chat_id,text=text);
