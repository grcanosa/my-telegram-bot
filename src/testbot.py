#!/usr/bin/python3

import sys
import logging

import emoji

import telegram
from telegram.ext import Updater;
from telegram.ext import CommandHandler as CH;
from telegram.ext import MessageHandler,Filters;
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

from mybot.data import piropos as LPIROPOS
from mybot.data import chistes as LCHISTES
from mybot.data import peopleemoji as LEMOJI
from mybot.data import teletokens as BS
from mybot.data import catgifs as LCATGIFS;

from mybot.handlers.randomphrase import RandomPhrase,PhraseList
from mybot.handlers import userregistry

#from mwt import MWT


class ZalameroBot:
    def __init__(self,TOKEN):
        self._token = TOKEN;
        self._nopiropo = BS.users_nopiropos;
        self._userR = userregistry.UserRegistry("zalamero.user.reg");
        self._randomP = RandomPhrase(self._userR);


    def is_from_admin(self,user_id):
        if user_id == BS.cid_gonzalo:
            return True;
        else:
            return False;

    def init(self):
        self._up = Updater(token=self._token);
        self._disp = self._up.dispatcher;
        self._bot = self._up.bot;
        self.install_handlers();



    def install_handlers(self):
        #self._disp.add_handler(CH('dimealgobonito',self.resp_dimealgobonito));
        #self._disp.add_handler(CH('dimealgorealmentebonito',self.resp_dimealgorealmentebonito));
        self._userR.install_handler(self._disp);
        self._randomP.add_cmd(self._disp,PhraseList('dimealgobonito',LPIROPOS.LIST),10);
        self._randomP.add_cmd(self._disp,PhraseList('dimealgodivertido',LCHISTES.LIST),10);
        self._randomP.add_cmd(self._disp,PhraseList('randomemoji',LEMOJI.LIST),10);
        self._randomP.add_cmd(self._disp,PhraseList('cat',LCATGIFS.LIST,"gif"),10);
        self._disp.add_handler(CH('sipiropo',self.resp_sipiropo,pass_args=True),1);
        self._disp.add_handler(CH('nopiropo',self.resp_nopiropo,pass_args=True),1);
        self._disp.add_handler(CH('pruebacmd',self.resp_prueba),1);
        self._disp.add_handler(MessageHandler(Filters.command, self._randomP.proc_phrase),1);
        #inline_caps_handler = InlineQueryHandler(self.inline_caps)
        #self._disp.add_handler(inline_caps_handler)

    def resp_prueba(self,bot,up):
        self._bot.send_message(chat_id=BS.cid_gonzalo,text="Llega comando prueba");
        self._bot.send_photo(chat_id=BS.cid_gonzalo,photo="AgADBAADA6kxG9eU5gABGrw2vLyFUcYeb2QZAAQzoyHMI_ZMOO-7AAIC");
        #self._bot.send_video(chat_id=BS.cid_gonzalo,video="BQADBAADdgMAAuAYZAdM22FCusLMPQI");
        self._bot.send_document(chat_id=BS.cid_gonzalo,document="BQADBAADdgMAAuAYZAdM22FCusLMPQI");



    def resp_sipiropo(self,bot,up,args):
        if self.is_from_admin(up.message.chat_id):
            if args[0] in self._nopiropo:
                self._nopiropo.remove(args[0]);
            self._bot.send_message(chat_id=up.message.chat_id,text=emoji.emojize("OK  :smile:",use_aliases=True));
        else:
            self._bot.send_message(chat_id=up.message.chat_id,text=emoji.emojize("NOT AUTHORIZED!!! :angry:",use_aliases=True))

    def resp_nopiropo(self,bot,up,args):
        if self.is_from_admin(up.message.chat_id):
            if not args[0] in self._nopiropo:
                self._nopiropo.append(args[0]);
            self._bot.send_message(chat_id=up.message.chat_id,text=emoji.emojize("OK  :smile:",use_aliases=True));
        else:
            self._bot.send_message(chat_id=up.message.chat_id,text=emoji.emojize("NOT AUTHORIZED!!! :angry:",use_aliases=True))



    def resp_dimealgobonito(self,bot,update : telegram.Update,use_name=True):
        text =""
        if update.message.from_user.username in self._nopiropo:
            text+= update.message.from_user.first_name.split()[0] + ", no seas presumido, deja de pedir piropos.";
        else:
            if use_name:
                text += update.message.from_user.first_name.split()[0] + ": ";
            text += LP.get_random_piropo();
        self._bot.send_message(chat_id=update.message.chat_id,text=text);

    def resp_dimealgorealmentebonito(self,bot,up):
        if up.message.chat_id == BS.cid_sara:
            self._bot.send_message(chat_id=BS.cid_sara,text="Claro que si lovechu, para ti lo que sea")
            self.resp_dimealgobonito(bot,up,False);
        else:
            self._bot.send_message(chat_id=up.message.chat_id,text="Las cosas realmente bonitas sólo se las digo a una persona ");

    def resp_unkown(self,bot,update : telegram.Update):
        text = "Lo siento "+update.message.from_user.first_name+ ", no entendí";
        text += emoji.emojize(':disappointed_relieved:', use_aliases=True);
        self._bot.send_message(chat_id=update.message.chat_id,text=text);

    def inline_caps(self,bot, update):
        query = update.inline_query.query
        if not query:
            return
        results = list()
        results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
         )
        )
        bot.answerInlineQuery(update.inline_query.id, results)




def main(argv):
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_format,level=logging.DEBUG)
    zal = ZalameroBot(BS.NEXTCALL_TOKEN);
    zal.init();
    zal.start();
    zal.idle();



if __name__ == "__main__":
  sys.exit(main(sys.argv));



  #dimealgobonito - Piropéame!
  #dimealgorealmentebonito - Súperpiropo!

























import logging
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram
import listapiropos
import grcanosasettings as GRS;
import emoiji

def start(bot : telegram.Bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")





def get_piropo():
    return random.choice(listapiropos.PIROPOSLIST)


def resp_piropo(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text=get_piropo());


def resp_trafico(bot,update):
    bot.sendMessage(chat_id=GRS.cid_gonzalo,text=emoji.emojize(':car:', use_aliases=True))
    bot.sendMessage(chat_id=GRS.cid_sara,text=emoji.emojize(':car:', use_aliases=True))




log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_format,level=logging.INFO)

updater = Updater(token=GRS.TOKEN)

dispatcher = updater.dispatcher

h_start = CommandHandler('start', start)
h_piropo = CommandHandler('dimealgobonito',resp_piropo)
h_trafico = CommandHandler('trafico',resp_trafico)

dispatcher.add_handler(h_start)
dispatcher.add_handler(h_piropo)
dispatcher.add_handler(h_trafico)

updater.start_polling()
updater.idle()
