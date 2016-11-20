#!/usr/bin/python3

import emoji
import random;
from .phraselist import PhraseList;
from ..data.teletokens import CID;

from telegram import Bot,Update;


class PiropoList(PhraseList):
    def __init__(self,cmdget,cmdadd,HD):
        super().__init__(userR,cmdget,cmdadd,HD);

    def get_max_cmd_response(self,update):
        text= update.message.from_user.first_name.split()[0];
        text +=", no seas presumid@, deja de pedir piropos";
        #return "BQADBAADKgAD15TmAAFDS0IqiyCZgwI","audio"
        #return "AwADBAADJwAD15TmAAG3Lbh5kdhR6QI","voice"
        return text,"message";




e_smilekiss = emoji.emojize(":kissing_heart:",use_aliases=True);
e_lovecat = emoji.emojize(":heart_eyes_cat::kissing_cat:",use_aliases=True);
e_heartsmile = emoji.emojize(":heart_eyes::kissing_closed_eyes::smile:",use_aliases=True);



SARALIST = [
"Te quiero mogollón, que lo sepas",
"En nada nos vemos!",
(10*e_smilekiss),
(10*e_lovecat),
"Me encanta tu risa",
"Estás más buena que el pan",
(9*e_heartsmile),
"Cuando te vea voy a .... y a ....., arufffffff"
 ]


class SaraPiropoList(PhraseList):
    def __init__(self,userR,cmd):
        super().__init__(userR,cmd,"","message");
        self._cid = CID["SARA"];
        self._list = SARALIST;


    def process(self,bot,update):
        userR.inc_cmd(update.message.from_user.id,self._cmd);
        if self._cid == update.message.chat_id:
            bot.send_message(chat_id=self._cid,text="Claro que si lovechu, a ti te mando lo que me pidas!");
            #bot.send_message(chat_id=self._cid,text=self.get_random_phrase());
            bot.send_message(chat_id=self._cid,text=random.choice(SARALIST));
        else:
            bot.send_message(chat_id=update.message.chat_id,text="Lo siento, las cosas realmente bonitas solo se las digo a una persona...");


    def get_max_cmd_response(self,update):
        return "","";
