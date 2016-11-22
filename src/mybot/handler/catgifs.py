#/!usr/bin/python3

from .phraselist import PhraseList;


class CatGifList(PhraseList):
    def __init__(self,cmdget = "",
                      cmdadd="",
                      filename ="",
                      updater=None,
                      userR = None,
                      phrasetype="gif",
                      priority = 50):
        super().__init__(cmdget=cmdget,cmdadd=cmdadd,filename=filename,updater=updater,userR=userR,priority=priority,phrasetype=phrasetype);

    def get_max_cmd_response(self,update):
        text = "Miau.... "
        text += update.message.from_user.first_name.split()[0];
        return text,"message";
