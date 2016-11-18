from telegram import Bot;
from .cmdprocessor import CmdProcessor;




class AdminCmd(CmdProcessor):
    def __init__(self,cmd,admin_cid):
        super().__init__(cmd);
        self._admin_cid = admin_cid;

    def process(self,userR,bot,update):
        ret = False;
        if self.cmd_ok(update.message.text):
            ret = True;
            if update.message.from_user.id == self._admin_cid:
                userR.inc_cmd(update.message.from_user.id,self._cmd);
                self.proc_admin_cmd(userR,bot,update);
            else:
                bot.send_message(chat_id=update.message.chat_id,text="You are not authorized!!!");
        return ret;




class BroadcastCmd(AdminCmd):
    def __init__(self,cmd,admin_cid):
        super().__init__(cmd,admin_cid);

    def proc_admin_cmd(self,userR,bot,update):
        print(update.message.text)
        text = update.message.text.split();
        text.pop(0);
        #print(text);
        text = ' '.join(text);
        for us in userR._users:
            bot.send_message(chat_id=us.get_id(),text=text);
