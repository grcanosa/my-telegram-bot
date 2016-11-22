#!/usr/bin/python3

import logging;

from ...users.userregistry import UserRegistry;

from ..tokens import TOKEN

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
        self._userR.install(self._updater);
        PiropoList(cmdget="piropo",cmdadd="addpiropo",
                    filename=self._datafolder+"/saei/piropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        CatGifList(cmdget="cat",cmdadd="",
                    filename=self._datafolder+"/saei/cats",
                    updater=self._updater,userR=self._userR,priority=50);



def main(*args, **kw):
    n = SaeibotBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
