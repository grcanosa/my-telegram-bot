#!/usr/bin/python3

import logging;

from ...users.userregistry import UserRegistry;

from ..tokens import TOKEN,CID

from ..basebot import BaseBot;

from ...handler.admincmds import BroadcastCmd;
from ...handler.piropos import PiropoList;
from ...handler.fixedresponse import FixedResponse;
from ...handler.randomemoji import RandomEmoji;
from ...handler.catgifs import CatGifList;

logger = logging.getLogger(__name__);



class NextcallBot(BaseBot):
    def __init__(self,logfolder,datafolder):
        super().__init__(TOKEN["NEXTCALL_BOT"]);
        self._logFile = logfolder+"/grcanosa.users.reg";
        self._datafolder = datafolder;
        self._userR = UserRegistry(self._logFile,admin_cid=CID["GONZALO"])
        self.install_handlers();

    def install_handlers(self):
        self._userR.install(self._updater);

        UserStats(cmd="stats",updater=self._updater,userR=self._userR,priority=50);

        BroadcastCmd(updater=self._updater,userR=self._userR,admin_cid=CID["GONZALO"],
                    priority=50);

        PiropoList(cmdget="piropo",cmdadd="addpiropo",
                    filename=self._datafolder+"/grcanosabot/piropos.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        CatGifList(cmdget="cat",cmdadd="",
                    filename=self._datafolder+"/cats",
                    updater=self._updater,userR=self._userR,priority=50);

        RandomEmoji(cmdget="randomemoji",cmdadd="addemoji",
                    filename=self._datafolder+"/emojis.txt",
                    updater=self._updater,userR=self._userR,priority=50);

        FixedResponse(cmd="help",response=self.get_help(),
                        updater=self._updater,userR=self._userR,priority=50);

        FixedResponse(cmd="start",response="Hola, soy nextcall_bot, escribe /help para ver que puedo hacer",
                        updater=self._updater,userR=self._userR,priority=50);



    def get_help(self):
        text = "Soy nextcall_bot, y esto es lo que puedo hacer: \n";
        text += "/piropo - Pide un piropo, o seguido de Nombre Apellidos manda un piropo a otra persona \n";
        text += "/addpiropo PIROPO A AÑADIR -  Añade un piropo a la lista \n";
        text += "/randomemoji - Pide un emoji aleatorio \n";
        #text += "/addemoji EMOJI A AÑADIR -  Añade un emoji a la lista \n";
        text += "/cat - Pide un gato!! \n";
        text += "/help - Ayuda \n";
        return text;



def main(*args, **kw):
    n = NextcallBot(kw["logfolder"],kw["datafolder"]);
    n.start();
    n.idle();
