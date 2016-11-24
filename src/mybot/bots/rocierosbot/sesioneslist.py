#/!usr/bin/python3

from ...handler.timeuntil import TimeUntil;
import emoji;
import logging;
import datetime;

logger = logging.getLogger(__name__)

class SesionesList(TimeUntil):
    def __init__(self,
                updater=None,
                userR = None,
                cmd="",
                filename="",
                priority = 50):
        super().__init__(cmdget=cmd,
                        updater=updater,
                        userR=userR,
                        filename=filename,
                        priority=priority);
        self._name = name;


    def get_response_text(self,t,tnow):
        logger.debug("Getting next text for timestamp %d",t);
        text= "";
        text += " La próxima sesión es el ";
        text += datetime.datetime.fromtimestamp(t).strftime("%d del %m a las %H:%M");
        text += ".\n "
        # text += "\n";
        # text += happy;
        text += "\n";
        text += " Quedan ";
        diffS = t-tnow;
        days = diffS // (24*3600);
        hours = (diffS-days*24*3600) // 3600;
        minutes = (diffS-days*24*3600-hours*3600) // 60;
        seconds = (diffS -days*24*3600 -hours *3600 -minutes * 60);
        if days > 0: text += str(int(days))+ " días, ";
        if hours > 0: text += str(int(hours))+ " horas, ";
        if minutes > 0: text += str(int(minutes))+ " minutos, "
        text += "y "+str(int(seconds))+" segundos";
        return text;
