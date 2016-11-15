#!/usr/bin/python3

import logging;
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

    def get_max_cmd_response(self,update):
        text = update.message.from_user.first_name.split()[0]
        text+=", no hay que ser cansino..."
        text+= LPEOPLEEMOJI.get_random();
        return text,"message";
