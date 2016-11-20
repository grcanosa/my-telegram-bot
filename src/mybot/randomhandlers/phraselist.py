#!/usr/bin/python3

import logging;
import random
import os;
from .cmdprocessor import CmdProcessor;

logger = logging.getLogger(__name__):

class PhraseList(CmdProcessor):
    def __init__(self,cmdget,cmdadd,data):
        super().__init__(cmdget);
        self._cmdadd = cmdadd;
        self._list = [];
        self._filename = filename;
        if os._exists(filename):
            with open(filename,'r') as f:
                for l in f: self._list.append(l);
        self._type = phrasetype;
        self._userR = userR;

    def get_random_phrase(self):
        return random.choice(self._list);

    def add_phrase(self,phrase):
        self._list.append(phrase);
        with open(self._filename,'a') as f:
            f.write(phrase);


    def process(self,bot,update):
        self._userR.inc_cmd(update.message.from_user.id,self._cmd);
        phrasetype = self._type;
        text = "";
        logger.debug("Cmd %s RECEIVED",self._cmd);
        if self._userR.is_cmd_max_num(update.message.from_user.id,self._cmd):
            text+=self.get_random_phrase();
        else:
            text, phrasetype = self.get_max_cmd_response(update);
        ret = True;
        if phrasetype == "message":
            bot.send_message(chat_id=update.message.chat_id,text=text);
        elif phrasetype == "gif":
            bot.send_document(chat_id=update.message.chat_id,document=text);
        elif phrasetype == "voice":
            bot.sendVoice(chat_id=update.message.chat_id,voice=text)
        elif phrasetype == "audio":
            bot.send_audio(chat_id=update.message.chat_id,audio=text);
