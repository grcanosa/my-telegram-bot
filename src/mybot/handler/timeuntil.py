#!/usr/bin/python3

import logging;
import random
import os;
import datetime;

from telegram.ext import CommandHandler;

logger = logging.getLogger(__name__)

class TimeUntil:
    def __init__(self,cmdget = "",filename ="",
            updater=None,userR = None,priority = 50):
        self._cmdget = cmdget;
        self._timestamps = [];
        self._filename = filename;
        self._userR = userR;
        self._up = updater;
        self._priority = priority;
        logger.debug("Creating time until list for get: "+self._cmdget);
        self.load_data();
        self.install_handler();

    MONTH = { 1: 'Enero', 2 : 'Febrero', 3:'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
              7 : 'Julio', 8 : 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'};

    def load_data(self):
        logger.debug("Trying to read from file %s",self._filename)
        if os.path.isfile(self._filename):
            with open(self._filename,'r') as f:
                for l in f:
                    try:
                        l = l.rstrip('\n');
                        d = datetime.datetime.strptime(l,"%Y-%m-%d %H:%M:%S")
                        self._timestamps.append(d.timestamp());
                    except ValueError:
                        logger.error("Date %s not valid",l);
        else:
            logger.error("File %s not found",self._filename);
        logger.debug("Added %d elements to list",len(self._timestamps));
        self._timestamps.sort();


    def install_handler(self):
        if self._cmdget is not "":
            self._up.dispatcher.add_handler(CommandHandler(self._cmdget,self.process_get),self._priority);

    def get_response_text(self,t,tnow):
        logger.debug("Getting next text for timestamp %d",t);
        text = "La próxima cita es el ";
        text += datetime.datetime.fromtimestamp(t).strftime("%d del %b a las %H:%M.");
        text += " Quedan ";
        diffS = t-tnow;
        days = diffS // (24*3600);
        hours = (diffS-days*24*3600) // 3600;
        minutes = (diffS-days*24*3600-hours*3600) // 60;
        seconds = (diffS -days*24*3600 -hours *3600 -minutes * 60);
        if days > 0: text += str(int(days))+ " días, ";
        if hours > 0: text += str(int(hours))+ " horas, ";
        if minutes > 0: text += str(int(minutes))+ " minutos, "
        text += "y "+str(int(seconds))+" segundos para la próxima cita";
        return text;


    def process_get(self,bot,update):
        tnow = datetime.datetime.now().timestamp();
        send = False;
        for t in self._timestamps:
            if t > tnow:
                send = True;
                bot.send_message(chat_id=update.message.chat_id,text=self.get_response_text(t,tnow));
                break;
        if not send:
            bot.send_message(chat_id=update.message.chat_id,text="No hay eventos a la vista...");
