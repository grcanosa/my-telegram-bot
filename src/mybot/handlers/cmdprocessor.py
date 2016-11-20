#!/usr/bin/python3

import logging;
import random



class CmdProcessor:
    def __init__(self,cmd,userR):
        self._cmd = cmd;
        self._userR = userR;

    def cmd_ok(self,text):
        return self._cmd in text;

    def get_cmd(self):
        return self._cmd;

    def process(self,bot,update):
        return False;
