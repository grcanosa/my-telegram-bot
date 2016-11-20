from telegram import Bot;
from .cmdprocessor import CmdProcessor;




class AdminCmd(CmdProcessor):
    def __init__(self,userR,cmd,admin_cid):
        super().__init__(cmd);
        self._admin_cid = admin_cid;
        self._userR = userR;

    def process(self,userR,bot,update):
        ret = True;
        if update.message.from_user.id == self._admin_cid:
            self._userR.inc_cmd(update.message.from_user.id,self._cmd);
            self.proc_admin_cmd(bot,update);
        else:
            bot.send_message(chat_id=update.message.chat_id,text="You are not authorized!!!");



class BroadcastCmd(AdminCmd):
    def __init__(self,userR,cmd,admin_cid):
        super().__init__(userR,cmd,admin_cid);

    def proc_admin_cmd(self,bot,update):
        print(update.message.text)
        text = update.message.text.split();
        text.pop(0);
        #print(text);
        text = ' '.join(text);
        for us in self._userR._users:
            bot.send_message(chat_id=us.get_id(),text=text);

class GenerateUserStats(AdminCmd):
    def __init__(self,userR,cmd,admin_cid):
        super().__init__(userR,cmd,admin_cid);

    def proc_admin_cmd(self,bot,update):
        self._userR.generate_file();
