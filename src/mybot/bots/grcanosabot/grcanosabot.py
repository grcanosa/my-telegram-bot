#!/usr/bin/python3

import logging;

from ...users.userregistry import UserRegistry;
from ...users.userstats import UserStats;

from ..tokens import TOKEN,CID

from ..basebot import BaseBot;

from ...handler.piropos import PiropoList;
from ...handler.fixedresponse import FixedResponse;
from ...handler.randomemoji import RandomEmoji;
from ...handler.catgifs import CatGifList;
from .sarapiropos import SaraPiropoList

logger = logging.getLogger(__name__);



class GrcanosaBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN["GRCANOSABOT"]);
        self._logFile = logfolder+"/grcanosa.users.reg";
        self._datafolder = datafolder;
        self._userR = UserRegistry(self._logFile,admin_cid=CID["GONZALO"])
        self.install_handlers();

    def install_handlers(self):
        self._userR.install(self._updater);

        UserStats(cmd="stats",updater=self._updater,userR=self._userR,priority=50);

        PiropoList(cmdget="dimealgobonito",cmdadd="addpiropo",
                    filename=self._datafolder+"/grcanosabot/piropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        CatGifList(cmdget="cat",cmdadd="",
                    filename=self._datafolder+"/cats",
                    updater=self._updater,userR=self._userR,priority=50);

        SaraPiropoList(cmdget="dimealgorealmentebonito",cmdadd="addpiroposara",
                    filename=self._datafolder+"/grcanosabot/sarapiropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        RandomEmoji(cmdget="randomemoji",cmdadd="addemoji",
                    filename=self._datafolder+"/emojis.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        FixedResponse(cmd="help",response=self.get_help(),
                        updater=self._updater,userR=self._userR,priority=50);



    def get_help(self):
        text = "Soy grcanosabot, y esto es lo que puedo hacer: \n";
        text += "/dimealgobonito - Pide un piropo \n";
        text += "/dimealgobonito Nombre Apellidos - Manda un piropo a otro usuario del bot. \n"
        text += "/addpiropo PIROPO A AÑADIR -  Añade un piropo a la lista \n";
        text += "/randomemoji - Pide un emoji aleatorio \n";
        text += "/addemoji EMOJI A AÑADIR -  Añade un emoji a la lista \n";
        text += "/cat - Pide un gato!! \n";
        return text;



def main(*args, **kw):
    n = GrcanosaBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
