#!/usr/bin/python3

import logging;
import random
import os;

from telegram.ext import CommandHandler;

logger = logging.getLogger(__name__):

class PhraseList:
    def __init__(self,cmdget = "",cmdadd="",filename ="",updater=None,userR = None,phrasetype = "message",priority = 50):
        super().__init__(cmdget);
        self._cmdadd = cmdadd;
        self._cmdget = cmdget;
        self._list = [];
        self._filename = filename;
        self._type = phrasetype;
        self._userR = userR;
        self._up = updater;
        self._priority = priority;
        self.load_data();
        self.install_handler();


    def load_data(self):
        if self._type == "messsage":
            if os._exists(self._filename):
                with open(self._filename,'r') as f:
                    for l in f:
                        self._list.append(l);
        elif self._type == "gif":
            if os.path.isdir(self._filename):
                for file in os.listdir(self._filename):
                    if file.endswith(".mp4"):
                        self._list.append(self._filename+"/"+file);

    def install_handler(self):
        if self._cmdadd is not "":
            self._up.dispatcher.add_handler(CommandHandler(self._cmdadd,self.proccess_add),self._priority);
        if self._cmdget is not "":
            self._up.dispatcher.add_handler(CommandHandler(self._cmdget,self.proccess_get),self._priority);

    def get_random_phrase(self):
        return random.choice(self._list);

    def add_phrase(self,phrase):
        self._list.append(phrase);
        with open(self._filename,'a') as f:
            f.write(phrase);

    def proccess_get(self,bot,update):
        self._userR.inc_cmd(update.message.from_user.id,self._cmdget);
        msgspli = update.message.text.split();
        if len(msgspli) > 1:
            msgspli.pop(0);
            us = self._userR.get_user(name=msgspli);
            if us is not None:
                bot.send_message(chat_id=update.message.chat_id,text="Send to "+msgspli+" correct");
                bot.send_message(chat_id=us.get_id(),text=self._userR.get_user(user_id=update.message.from_user.id).get_name()+" sends this to you:")
                self.send_random(bot,us.get_id());
            else:
                bot.send_message(chat_id=update.message.chat_id,text="User "+msgspli+" not recognized");
        else:
            logger.debug("Giving something to own user");
            if self._userR.is_cmd_max_num(update.message.from_user.id,self._cmdget):
                self.send_random(bot,update.message.chat_id);
            else:
                text, phrasetype = self.get_max_cmd_response(update);
                if phrasetype == "message":
                    bot.send_message(chat_id=update.message.chat_id,text=text);

    def process_add(self,bot,update):
        self._userR.inc_cmd(update.message.from_user.id,self._cmdadd);
        msgspli = update.message.text.split();
        msgspli.pop(0);
        if self._type == "message":
            self.add_phrase(msgspli);
            bot.send_message(chat_id=update.message.chat_id,text="Your suggestion has beed added!!");


    def send_random(self,bot,user_id):
        if self._type == "message":
            bot.send_message(chat_id=user_id,text=self.get_random_phrase());
        elif self._type == "gif":
            bot.send_document(chat_id=user_id,document=open(self.get_random_phrase());


    # def process(self,bot,update):
    #     self._userR.inc_cmd(update.message.from_user.id,self._cmd);
    #     phrasetype = self._type;
    #     text = "";
    #     logger.debug("Cmd %s RECEIVED",self._cmd);
    #     if self._userR.is_cmd_max_num(update.message.from_user.id,self._cmd):
    #         text+=self.get_random_phrase();
    #     else:
    #         text, phrasetype = self.get_max_cmd_response(update);
    #     ret = True;
    #     if phrasetype == "message":
    #         bot.send_message(chat_id=update.message.chat_id,text=text);
    #     elif phrasetype == "gif":
    #         bot.send_document(chat_id=update.message.chat_id,document=text);
    #     elif phrasetype == "voice":
    #         bot.sendVoice(chat_id=update.message.chat_id,voice=text)
    #     elif phrasetype == "audio":
    #         bot.send_audio(chat_id=update.message.chat_id,audio=text);
