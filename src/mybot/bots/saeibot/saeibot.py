#!/usr/bin/python3

import logging;

from ...users.userregistry import UserRegistry;

from ..tokens import TOKEN,CID

from ..basebot import BaseBot;

from ...handler.admincmds import BroadcastCmd;
from ...handler.piropos import PiropoList;
from ...handler.fixedresponse import FixedResponse;
from ...handler.randomemoji import RandomEmoji;
from .catgifs import CatGifList;
from .saeiresp import SaeiResp;

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

        BroadcastCmd(updater=self._updater,userR=self._userR,admin_cid=CID["GONZALO"],
                    priority=50);

        PiropoList(cmdget="piropo",cmdadd="addpiropo",
                    filename=self._datafolder+"/saei/piropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        CatGifList(cmdget="cat",cmdadd="",
                    filename=self._datafolder+"/cats",
                    updater=self._updater,userR=self._userR,priority=50);

        FixedResponse(cmd="help",response=self.get_help(),
                        updater=self._updater,userR=self._userR,priority=50);

        RandomEmoji(cmdget="randomemoji",cmdadd="addemoji",
                    filename=self._datafolder+"/emojis.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        SaeiResp(updater=self._updater,userR=self._userR,priority=50);

    def get_help(self):
        text = "Soy saeiiiiibot, y esto es lo que puedo hacer: \n";
        text += "/saei - ¿? ;) \n"
        text += "/piropo - Pide un piropo o, añadiendo Nombre Apellidos, manda un piropo a otro usuario. Ejemplo: /piropo Gonzalo Rodriguez \n";
        text += "/addpiropo - Añade un piropo a la lista. Ej: /piropo Que bien te veo! \n";
        text += "/randomemoji - Pide un emoji aleatorio \n";
        text += "/cat - !!! \n";
        return text;

def main(*args, **kw):
    n = SaeibotBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
