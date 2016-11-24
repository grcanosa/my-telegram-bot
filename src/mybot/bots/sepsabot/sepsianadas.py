#/!usr/bin/python3

from ...handler.phraselist import PhraseList;


class SepsianadaList(PhraseList):
    def __init__(self,cmdget = "",
                      cmdadd="",
                      filename ="",
                      updater=None,
                      userR = None,
                      phrasetype="message",
                      priority = 50):
        super().__init__(cmdget=cmdget,cmdadd=cmdadd,filename=filename,updater=updater,userR=userR,priority=priority,phrasetype=phrasetype);

    def get_max_cmd_response(self,update):
        text = "No has tenido ya suficiente??? "
        return text,"message";
