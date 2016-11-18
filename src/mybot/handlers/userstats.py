#!/usr/bin/python3

from telegram import Bot;
from .cmdprocessor import CmdProcessor;

class UserStats(CmdProcessor):
    def __init__(self,disp,cmd):
        super().__init__(cmd);

    def process(self,userR,bot,update):
        ret = False;
        if self.cmd_ok(update.message.text):
            userR.inc_cmd(update.message.from_user.id,self._cmd);
            ret = True;
            text = "";
            u = userR.get_user(update.message.from_user.id);
            text += "Eres "+u.get_name()+ " con número de usuario telegram: "+str(u.get_id())+"\n";
            text += "Esto es lo que me has pedido desde que te conozc: \n";
            for cmd,num in u.get_cmds().items():
                text += '{0:<5}'.format(num)+" - "+cmd+"\n";
            bot.send_message(chat_id=update.message.chat_id,text=text);
        return ret;
