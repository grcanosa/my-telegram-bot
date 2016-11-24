#/!usr/bin/python3

from ...handler.phraselist import PhraseList;


class AnimosList(PhraseList):
    def __init__(self,cmdget = "",
                      cmdadd="",
                      filename ="",
                      updater=None,
                      userR = None,
                      phrasetype="message",
                      priority = 50):
        super().__init__(cmdget=cmdget,cmdadd=cmdadd,filename=filename,updater=updater,userR=userR,priority=priority,phrasetype=phrasetype);

    def get_max_cmd_response(self,update):
        text = "Si necesitas más ánimos, llama a cualquiera de nosotros que para eso estamos! ;)"
        return text,"message";
