#!/usr/bin/python3

from telegram import Bot;
from telegram import Update;
from telegram.ext import Dispatcher;
from telegram.ext import CommandHandler as CH;

from .cmdprocessor import CmdProcessor;

class FixedResponse(CmdProcessor):
    def __init__(self,userR,cmd,resp,resptype):
        super().__init__(cmd);
        self._resp = resp;
        self._type = resptype;
        self._userR = userR;

    def process(self,bot,update):
        userR.inc_cmd(update.message.from_user.id,self._cmd);
        ret = True;
        if self._type == "message":
            bot.send_message(chat_id=update.message.chat_id,text=self._resp);
        elif self._type == "gif":
            bot.send_document(chat_id=update.message.chat_id,document=self._resp);
        elif self._type == "voice":
            bot.sendVoice(chat_id=update.message.chat_id,voice=self._resp)
        elif self._type == "audio":
            bot.send_audio(chat_id=update.message.chat_id,audio=self._resp);
