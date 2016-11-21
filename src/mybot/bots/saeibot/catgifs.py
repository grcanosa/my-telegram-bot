#/!usr/bin/python3

from ...handler.phraselist import PhraseList;


class CatGifList(PhraseList):
    def __init__(self,cmdget = "",
                      cmdadd="",
                      filename ="",
                      updater=None,
                      userR = None,
                      priority = 50):
        super().__init__(cmdget=cmdget,cmdadd=cmdadd,filename=filename,updater=updater,userR=userR,priority=priority);

    def get_max_cmd_response(self,update):
        text = "Saeiiiii, más y más gatos... "
        text += update.message.from_user.first_name.split()[0];
        return text,"message";
