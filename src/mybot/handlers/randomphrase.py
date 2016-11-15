#!/usr/bin/python3

import random;
import logging;

import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler as CH;
from ..data import peopleemoji as LPEOPLEEMOJI;


class PhraseList:
    def __init__(self,cmd,list,phrasetype="message"):
        self._cmd = cmd;
        self._list = list;
        self._type = phrasetype;

    def get_random_phrase(self):
        return random.choice(self._list);

    def cmd_ok(self,text):
        return self._cmd in text;

    def get_cmd(self):
        return self._cmd;



class RandomPhrase:
    def __init__(self,userReg):
        self._cmd_list = [];
        self._user_reg = userReg;


    def add_cmd(self,dispatcher,phraselist, priority=1):
        self._cmd_list.append(phraselist);
        dispatcher.add_handler(CH(phraselist.get_cmd,self.proc_phrase),priority);

    def proc_phrase(self,bot,update):
        logging.debug("Received: %s",update.message.text);
        text = "";
        added = False;
        for phraselist in self._cmd_list:
            if phraselist.cmd_ok(update.message.text):
                added = True;
                phrasetype = phraselist._type;
                logging.debug("Cmd %s RECEIVED",phraselist._cmd);
                if self._user_reg.inc_cmd(update.message.from_user.id,phraselist._cmd):
                    text+=phraselist.get_random_phrase();
                else:
                    text += update.message.from_user.first_name.split()[0]
                    text+=", no hay que ser cansino..."
                    text+= LPEOPLEEMOJI.get_random();
                    phrasetype = "message";
                    break;
        if not added:
            text += "Command not defined yet! ";
            text += emoji.emojize(":crying_cat_face:",use_aliases=True);
            phrasetype="message";
        if phrasetype == "message":
            bot.send_message(chat_id=update.message.chat_id,text=text);
        elif phrasetype == "gif":
            bot.send_document(chat_id=update.message.chat_id,document=text);
