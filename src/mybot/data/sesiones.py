#!/usr/bin/python3
from datetime import datetime
import time;
FECHALIST = [
"2016-11-17 20:00:00",
"2016-12-01 20:00:00"

]



LIST = []

for f in FECHALIST:
    d = datetime.strptime(f,"%Y-%m-%d %H:%M:%S")
    LIST.append(d.timestamp());

LIST = sort(LIST);

class SesionTimer(PhraseList):
    def __init__(self,cmd):
        super().__init__(cmd,LIST,"message");

    def process(self,userR,bot,update):
        if self.cmd_ok(update.message.text):
            d = datetime.today().timestamp();
