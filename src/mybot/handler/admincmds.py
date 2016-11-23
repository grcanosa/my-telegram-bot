from telegram import Bot;
from telegram.ext import CommandHandler

import logging

logger = logging.getLogger(__name__);



class AdminCmd:
    def __init__(self,userR=None,updater=None,cmd="",admin_cid=0,priority=50):
        self._admin_cid = admin_cid;
        self._userR = userR;
        self._updater = updater;
        self._cmd = cmd;
        self._priority = priority;
        if self._updater is not None and self._userR is not None:
            self.install();
        else:
            logger.error("Problem installing %s",self._cmd);


    def install(self):
        if not self._cmd == "":
            ch = CommandHandler(self._cmd,self.process);
            self._updater.dispatcher.add_handler(ch,self._priority)

    def process(self,bot,update):
        if update.message.from_user.id == self._admin_cid:
            self.proc_admin_cmd(bot,update);
        else:
            bot.send_message(chat_id=update.message.chat_id,text="You are not authorized!!!");



class BroadcastCmd(AdminCmd):
    def __init__(self,updater=None,userR=None,admin_cid=0,priority=50):
        super().__init__(userR=userR,
                        updater=updater,
                        cmd="broadcast",
                        admin_cid=admin_cid,
                        priority=priority);

    def proc_admin_cmd(self,bot,update):
        logger.debug("Received: %s",update.message.text)
        text = update.message.text.split();
        text.pop(0);
        #print(text);
        text = ' '.join(text);
        for us in self._userR._users:
            bot.send_message(chat_id=us.get_id(),text="Broadcast from God: ");
            bot.send_message(chat_id=us.get_id(),text=text);
