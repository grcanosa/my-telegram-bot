#!/usr/bin/python3

#TELEGRAM IMPORTS
from telegram.ext import Updater;
from telegram.ext import MessageHandler,Filters

from ...data.teletokens import TOKEN;
from ...data.peopleemoji import PeopleEmoji;
from ...data.piropos import PiropoList,SaraPiropoList;
from ...data.catgifs import CatGifList;

from ...handlers.userregistry import UserRegistry;
from ...handlers.cmdcollection import CmdCollection;
from ...handlers.fixedresponse import FixedResponse;
from ...handlers.userstats import UserStats;
from ..basebot import BaseBot;




class NextCallBot(BaseBot):
    def __init__(self,logfolder):
        super().__init__(TOKEN["NEXTCALL_BOT"]);
        self._logFile = logfolder+"/nextcall.users.reg";
        self._userR = UserRegistry(self._logFile)
        self._cmdC10 = CmdCollection(self._userR,10);
        self.install_handlers();

    def install_handlers(self):
        self._userR.install_handler(self._disp);

        self._cmdC10.add_cmd(self._disp,FixedResponse(self._disp,"help","AwADBAADJwAD15TmAAG3Lbh5kdhR6QI","voice"));
        self._cmdC10.add_cmd(self._disp,FixedResponse(self._disp,"start","Hola, soy NextCallBot, usa un comando para probarme","message"));
        self._cmdC10.add_cmd(self._disp,UserStats(self._disp,"stats"));
        self._cmdC10.add_cmd(self._disp,PeopleEmoji("randomemoji"));
        self._cmdC10.add_cmd(self._disp,PiropoList("dimealgobonito"));
        self._cmdC10.add_cmd(self._disp,SaraPiropoList("dimealgorealmentebonito"));
        self._cmdC10.add_cmd(self._disp,CatGifList("cat"));
        self._disp.add_handler(MessageHandler(Filters.command, self._cmdC10.proc_phrase),10);






def main(logfolder = ""):
    n = NextCallBot(logfolder);
    n.start();
    n.idle();
