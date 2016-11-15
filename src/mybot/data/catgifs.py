#/!usr/bin/python3

from ..handlers.phraselist import PhraseList;

LIST = [
"BQADBAADaAYAAocbZAciIWq9C74SAgI",
"BQADBAAD3TgAAu8cZAcqlrGqOSV22wI",
"BQADBAADiyAAAlgXZAezKLZ9MT_SrAI",
"BQADBAADdgMAAuAYZAdM22FCusLMPQI",
"BQADBAADsB4AAtUYZAd4L46CbUw5TQI",
"BQADBAADliEAAlgdZAf_QoDpHJTeXwI",
"BQADBAADwCAAAnUdZAciR8DiCEN5CQI",
"BQADBAAD3hYAAkwZZAfTw21n9HjSEwI",
"BQADBAADfxoAAtgYZAeCNTkLIBXZ-QI",
"BQADBAADwAUAAhQeZAf3dT6N0GF28QI",
"BQADBAADqSEAAusbZAfoeAjccdNgNgI",
"BQADBAADQhcAAnEaZAeqYUMfKuaQtgI",
"BQADBAAD8jcAAhMZZAeuDQABPVHH1ZMC"
]


class CatGifList(PhraseList):
    def __init__(self,cmd):
        super().__init__(cmd,LIST,"gif");

    def get_max_cmd_response(self,update):
        text = "Nunca hay demasiados gatos! Pide otro "
        text += update.message.from_user.first_name.split()[0];
        #return "BQADBAADKgAD15TmAAFDS0IqiyCZgwI","audio"
        #return "AwADBAADJwAD15TmAAG3Lbh5kdhR6QI","voice"
        return text,"message";
