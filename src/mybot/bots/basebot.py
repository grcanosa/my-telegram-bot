#!/usr/bin/python3

#TELEGRAM IMPORTS
from telegram.ext import Updater;




class BaseBot:
    def __init__(self,token):
        self._token = token;
        self._up = Updater(self._token);
        self._disp = self._up.dispatcher;
        self._bot = self._up.bot;

    def start(self):
        self._up.start_polling();

    def stop(self):
        self._up.stop();

    def idle(self):
        self._up.idle();
