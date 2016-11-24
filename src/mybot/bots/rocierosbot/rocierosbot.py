#!/usr/bin/python3

import logging;
import emoji;

from ...users.userregistry import UserRegistry;

from ..tokens import TOKEN,CID

from ..basebot import BaseBot;

from ...handler.admincmds import BroadcastCmd;
from ...handler.piropos import PiropoList;
from ...handler.fixedresponse import FixedResponse;
from ...handler.randomemoji import RandomEmoji;
from ...handler.timeuntil import TimeUntil;
from ...handler.catgifs import CatGifList;
from .sesioneslist import SesionesList

logger = logging.getLogger(__name__);



class RocierosBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN["ROCIEROSBOT"]);
        self._logFile = logfolder+"/rocieros.users.reg";
        self._datafolder = datafolder;
        self._userR = UserRegistry(self._logFile,admin_cid=CID["GONZALO"])
        self.install_handlers();

    def install_handlers(self):
        self._userR.install(self._updater);

        UserStats(cmd="stats",updater=self._updater,userR=self._userR,priority=50);

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

        FixedResponse(cmd="start",response="Soy RocierosBot, escribe /help para ver que puedo hacer!",
                        updater=self._updater,userR=self._userR,priority=50);

        RandomEmoji(cmdget="randomemoji",cmdadd="addemoji",
                    filename=self._datafolder+"/emojis.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        SesionesList(cmd="sesion",filename=self._datafolder+"/rocierosbot/sesiones.txt",
                    updater=self._updater,userR=self._userR,priority=50);



    def get_help(self):
        text = "Soy el bot oficial de los rocieros, y esto es lo que puedo hacer: \n";
        text += "/sesion - Información sobre las siguiente sesión \n"
        text += "/piropo - Pide un piropo o, añadiendo Nombre Apellidos, manda un piropo a otro usuario. Ejemplo: /piropo Gonzalo Rodriguez \n";
        #text += "/addpiropo - Añade un piropo a la lista. Ej: /piropo Que bien te veo! \n";
        text += "/randomemoji - Pide un emoji aleatorio \n";
        text += "/cat - !!! \n";
        text += "/help - Ayuda \n";
        return text;

def main(*args, **kw):
    n = RocierosBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
