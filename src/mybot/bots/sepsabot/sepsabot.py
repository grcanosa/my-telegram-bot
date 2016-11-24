#!/usr/bin/python3

import logging;
import emoji;
from ...users.userregistry import UserRegistry;

from ..tokens import TOKEN,CID

from ..basebot import BaseBot;

from ...handler.admincmds import BroadcastCmd;
from ...handler.piropos import PiropoList;
from ...handler.fixedresponse import FixedResponse;
from ...handler.catgifs import CatGifList;
from .sepsianadas import SepsianadaList;
from ...users.userstats import UserStats;


logger = logging.getLogger(__name__);



class SepsaBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN["SEPSABOT"]);
        self._logFile = logfolder+"/sepsabot.users.reg";
        self._datafolder = datafolder;
        self._userR = UserRegistry(self._logFile,admin_cid=CID["GONZALO"])
        self.install_handlers();

    def install_handlers(self):
        self._userR.install(self._updater);

        UserStats(cmd="stats",updater=self._updater,userR=self._userR,priority=50);

        BroadcastCmd(updater=self._updater,userR=self._userR,admin_cid=CID["GONZALO"],
                    priority=50);

        PiropoList(cmdget="piropo",cmdadd="addpiropo",
                    filename=self._datafolder+"/sepsabot/piropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        SepsianadaList(cmdget="sepsianada",cmdadd="addsepsianada",
                    filename=self._datafolder+"/sepsabot/sepsianadas.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        CatGifList(cmdget="cat",cmdadd="",
                    filename=self._datafolder+"/cats",
                    updater=self._updater,userR=self._userR,priority=50);

        FixedResponse(cmd="help",response=self.get_help(),
                        updater=self._updater,userR=self._userR,priority=50);

        FixedResponse(cmd="sepsa",response=emoji.emojize(":hocho::sweat_smile::speech_balloon: SEPSA, el mejor lugar para trabajar!!",use_aliases=True),
                        updater=self._updater,userR=self._userR,priority=50);




    def get_help(self):
        text = "Soy sepsabot, y esto es lo que puedo hacer: \n";
        text += "/sepsa - Para saber más... \n";
        text += "/sepsianada - Sepsianada al azar"
        text += "/addsepsianada - Añadir sepsianada a la lista \n";
        text += "/piropo - Pide o manda un piropo. Para mandar escribe /piropo Nombre Apellidos. \n";
        text += "/cat - Pide un gato!! \n";
        return text;

def main(*args, **kw):
    n = SepsaBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
