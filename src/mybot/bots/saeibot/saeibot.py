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

from ...handler.piropos import PiropoList;
from .catgifs import CatGifList;

logger = logging.getLogger(__name__);



class SaeibotBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN["SAEIIIIBOT"]);
        self._logFile = logfolder+"/saeii.users.reg";
        self._datafolder = datafolder;
        self._userR = UserRegistry(self._logFile)
        self.install_handlers();

    def install_handlers(self):
        self._userR.install(self._up);
        PiropoList(cmdget="piropo",cmdadd="addpiropo",
                    filename=self._datafolder+"/saei/piropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        PiropoList(cmdget="cat",cmdadd="",
                    filename=self._datafolder+"/saei/cats",
                    updater=self._updater,userR=self._userR,priority=50);



def main(*args, **kw):
    n = SaeibotBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
