#/!usr/bin/python3

from ...handler.fixedresponse import FixedResponse;
import emoji;

class SaeiResp(FixedResponse):
    def __init__(self,
                updater=None,
                userR = None,
                priority = 50):
        super().__init__(cmd="saei",
                        response="",
                        updater=updater,
                        userR=userR,
                        phrasetype="message",
                        priority=priority);
        self._users = {}
        self._lips = 4* emoji.emojize(":lips:",use_aliases=True)

    def process(self,bot,update):
        self._userR.inc_cmd(update.message.from_user.id,self._cmd);
        if not update.message.from_user.id in self._users:
            self._users[update.message.from_user.id] = 1;
        else:
            self._users[update.message.from_user.id] += 1;
        if self._users[update.message.from_user.id] <= 2:
            bot.send_message(chat_id=update.message.chat_id,text=self._users[update.message.from_user.id]*self._lips);
        else:
            self._users[update.message.from_user.id] = 0;
            bot.send_message(chat_id=update.message.chat_id,text="Has invocado la furia de la Marian!!!");
            bot.send_message(chat_id=update.message.chat_id,text=100*self._lips);
