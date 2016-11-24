#/!usr/bin/python3

from ...handler.timeuntil import TimeUntil;
import emoji;
import logging;
import datetime;

logger = logging.getLogger(__name__)

class MiniMari(TimeUntil):
    def __init__(self,
                updater=None,
                userR = None,
                filename="",
                priority = 50):
        super().__init__(cmdget="minimari",
                        updater=updater,
                        userR=userR,
                        filename=filename,
                        priority=priority);



    def get_response_text(self,t,tnow):
        logger.debug("Getting next text for timestamp %d",t);
        text= "";
        diffS = t-tnow;
        months = diffS // (24*3600*30);
        baby = emoji.emojize(":baby:",use_aliases=True);
        wedding = emoji.emojize(":wedding::bride_with_veil::couple::couplekiss:",use_aliases=True);
        bell = emoji.emojize(":bell:",use_aliases=True);
        balloon = emoji.emojize(":balloon:",use_aliases=True);
        tada = emoji.emojize(":tada:",use_aliases=True);
        confetti = emoji.emojize(":confetti_ball:",use_aliases=True);
        happy = 4*baby+4*(2*tada+balloon+2*confetti)+4*baby;
        text += happy + "\n \n";
        text += "En "+str(int(months))+" meses aproximadamente llegará la MiniMari (a.k.a Alejandra)!!!";
        text += "\n \n";
        text += happy;
        return text;
