#/!usr/bin/python3

from ...handler.timeuntil import TimeUntil;
import emoji;
import logging;
import datetime;

logger = logging.getLogger(__name__)

class BodaResp(TimeUntil):
    def __init__(self,
                updater=None,
                userR = None,
                name="",
                filename="",
                priority = 50,alt_resp=False):
        super().__init__(cmdget="boda"+name.lower(),
                        updater=updater,
                        userR=userR,
                        filename=filename,
                        priority=priority);
        self._name = name;
        self._alt_resp = alt_resp;


    def get_response_text(self,t,tnow):
        logger.debug("Getting next text for timestamp %d",t);
        text= "";
        wedding = emoji.emojize(":wedding::bride_with_veil::couple::couplekiss:",use_aliases=True);
        bell = emoji.emojize(":bell:",use_aliases=True);
        balloon = emoji.emojize(":balloon:",use_aliases=True);
        tada = emoji.emojize(":tada:",use_aliases=True);
        confetti = emoji.emojize(":confetti_ball:",use_aliases=True);
        happy = 3*bell+5*(2*tada+balloon+2*confetti)+3*bell;
        text += happy + "\n \n";
        #text += "     "+wedding;
        #text += "\n";
        if self._alt_resp:
            text += "¡¡¡Todavía no sabemos cuando es la boda de "+self._name;
            text += ", pero lo celebraremos igual!!! \n";
        else:
            text += " La boda de "+self._name+ " es el ";
            text += datetime.datetime.fromtimestamp(t).strftime("%d de ");
            text += TimeUntil.MONTH[datetime.datetime.fromtimestamp(t).month]
            text += datetime.datetime.fromtimestamp(t).strftime(" a las %H:%M");
            text += "!!! "
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
        text += 2*"\n";
        text += happy;
        return text;
