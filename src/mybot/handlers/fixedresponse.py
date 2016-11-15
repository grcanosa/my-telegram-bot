#!/usr/bin/python3

from telegram import Bot;
from telegram import Update;
from telegram.ext import Dispatcher;
from telegram.ext import CommandHandler as CH;


class FixedResponse:
    def __init__(self,disp,cmd,resp,resptype,priority=10):
        self._cmd = cmd,
        self._resp = resp;
        self._type = resptype;
        disp.add_handler(CH(cmd,self.respond),priority);

    def is_cmd_ok(self,cmd_in):
        return self._cmd == cmd_in;

    def respond(self,bot,update):
        if self._type == "message":
            bot.send_message(chat_id=update.message.chat_id,text=self._resp);
        elif self._type == "gif":
            bot.send_document(chat_id=update.message.chat_id,document=self._resp);
        elif self._type == "voice":
            bot.sendVoice(chat_id=update.message.chat_id,voice=self._resp)
        elif self._type == "audio":
            bot.send_audio(chat_id=update.message.chat_id,audio=self._resp);
