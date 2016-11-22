#!/usr/bin/python3

import logging;
import random
import time;
import datetime;
import math;
from .cmdprocessor import CmdProcessor;

class TimeUntil(CmdProcessor):
    def __init__(self,cmd,timestamplist):
        super().__init__(cmd);
        self._timeL = sort(timestamplist);


    def get_str_diff(tnext,tnow):
        diffT = tnext - tnow;
        days = math.floor(diffT/(60*60*24));
        diffT -= days*60*60*24;
        hours = math.floor(diffT/(60*60));
        diffT -= hours*60*60;
        minutes = math.floor(diffT/60);
        diffT -= minutes*60;
        text = "";
        if days > 0: text += str(days)+" días, "
        if hours > 0: text += str(hours)+" horas, "
        if minutes > 0: text += str(minutes)+ " minutos, "
        if diffT > 0: text += str(diffT)+" segundos"
        return text;

    def process(self,userR,bot,update):
        ret = False;
        if self.cmd_ok(update.message.text):
            userR.inc_cmd(update.message.from_user.id,self._cmd);
            ret = True;
            tnow = time.time();
            tnext = 0;
            for t in self._timeL:
                if t > tnow:
                    tnext = t;
                    break;
            if tnext > 0:
                diffT = tnext - tnow;
                days = math.floor(diffT/(60*60*24));
                diffT -= days*60*60*24;
                hours = math.floor(diffT/(60*60));
                diffT -= hours*60*60;
                minutes = math.floor(diffT/60);
                diffT -= minutes*60;
                datetime.
            else:




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

    def process(self,userR,bot,update):
        ret = False;
        if self.cmd_ok(update.message.text):
            userR.inc_cmd(update.message.from_user.id,self._cmd);
            phrasetype = self._type;
            text = "";
            logging.debug("Cmd %s RECEIVED",self._cmd);
            if userR.inc_cmd(update.message.from_user.id,self._cmd):
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
            else:
                ret = False;
        return ret;
