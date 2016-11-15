#!/usr/bin/python3

#TELEGRAM IMPORTS
from telegram.ext import Updater;

from ...data.teletokens import TOKEN;
from ...data.peopleemoji import PeopleEmoji;

from ...handlers.userregistry import UserRegistry;
from ...handlers.ramdomphrase import RandomPhrase;
from ..basebot import BaseBot;




class NextCallBot(BaseBot):
    def __init__(self):
        super().__init__( TOKEN["NEXTCALL_BOT"]);
        self._userR = UserRegistry("log/nextcall.users.reg")
        self._randomP = RandomPhrase(self._userR);
        self.install_handlers();

    def install_handlers():
        self._userR.install_handler(self._disp);
        self._randomP.add_cmd(self._disp,PeopleEmoji(),10)
