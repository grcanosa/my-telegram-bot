#!/usr/bin/python3

#TELEGRAM IMPORTS
from telegram.ext import Updater;
from telegram.ext import MessageHandler,Filters

from ...data.teletokens import TOKEN;
from ...data.peopleemoji import PeopleEmoji;
from ...data.piropos import PiropoList,SaraPiropoList;
from ...data.catgifs import CatGifList;

from ...handlers.userregistry import UserRegistry;
from ...handlers.randomphrase import RandomPhrase;
from ...handlers.fixedresponse import FixedResponse;
from ..basebot import BaseBot;




class NextCallBot(BaseBot):
    def __init__(self):
        super().__init__( TOKEN["NEXTCALL_BOT"]);
        self._userR = UserRegistry("log/nextcall.users.reg")
        self._randomP = RandomPhrase(self._userR);
        self._fixedResp = [];
        self.install_handlers();

    def install_handlers(self):
        self._userR.install_handler(self._disp);
        self._fixedResp.append(FixedResponse(self._disp,"help","AwADBAADJwAD15TmAAG3Lbh5kdhR6QI","voice",10))
        self._fixedResp.append(FixedResponse(self._disp,"start","Hola, soy NextCallBot, usa un comando para probarme","message",10))
        self._randomP.add_cmd(self._disp,PeopleEmoji("randomemoji"),10);
        self._randomP.add_cmd(self._disp,PiropoList("dimealgobonito"),10);
        self._randomP.add_cmd(self._disp,SaraPiropoList("dimealgorealmentebonito"),10);
        self._randomP.add_cmd(self._disp,CatGifList("cat"),10);
        self._disp.add_handler(MessageHandler(Filters.command, self._randomP.proc_phrase),10);






def main():
    n = NextCallBot();
    n.start();
    n.idle();
