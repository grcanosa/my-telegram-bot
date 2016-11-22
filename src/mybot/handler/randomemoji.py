#!/usr/bin/python3

import emoji
import random;
from .phraselist import PhraseList;
#from ..data.teletokens import CID;

from telegram import Bot,Update;


class RandomEmoji(PhraseList):
    def __init__(self,cmdget = "",
                      cmdadd="",
                      filename ="",
                      updater=None,
                      userR = None,
                      priority = 50):
        super().__init__(cmdget=cmdget,cmdadd=cmdadd,filename=filename,updater=updater,userR=userR,priority=priority);
        self._max_cmd_resp = "Quieres emoji?, pues toma dos ";
        self._max_cmd_resp += emoji.emojize(":coffee::coffee: \n",use_aliases=True);

        list = [];
        for l in self._list:
            e = emoji.emojize(l,use_aliases=True)
            list.append(e);
            self._max_cmd_resp += e.rstrip().lstrip();
        self._list = list;

    def get_max_cmd_response(self,update):
        return self._max_cmd_resp,"message";
