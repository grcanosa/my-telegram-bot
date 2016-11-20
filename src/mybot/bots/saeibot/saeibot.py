#!/usr/bin/python3

import logging;

#TELEGRAM IMPORTS
# from telegram.ext import Updater;
# from telegram.ext import MessageHandler,Filters
#
# from ...data.teletokens import TOKEN,CID;
# from ...data.peopleemoji import PeopleEmoji;
# from ...data.piropos import PiropoList,SaraPiropoList;
# from ...data.catgifs import CatGifList;
#
# from ...handlers.userregistry import UserRegistry;
# from ...handlers.cmdcollection import CmdCollection;
# from ...handlers.fixedresponse import FixedResponse;
# from ...handlers.userstats import UserStats;
# from ...handlers.admincmds import BroadcastCmd;
# from ..basebot import BaseBot;

from ..basebot import BaseBot;

from ...randomhanlders.piropos import PiropoList;

logger = logging.getLogger(__name__);



class SaeibotBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN["SAEIIIIBOT"]);
        self._logFile = logfolder+"/saeii.users.reg";
        self._datafolder = datafolder;
        self._userR = UserRegistry(self._logFile)
        self.handlers = [];
        self._HD.up = self._up;
        self._HD.userR = self._userR;
        self._HD.datafolder = self._datafolder;
        self.install_handlers();

    def install_handlers(self):
        self._userR.install(self._up);
        #self._userR.install_handler(self._disp);

        self.handlers.append(PiropoList("get","add",self._HD));




def main(*args, **kw):
    n = SaeibotBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
