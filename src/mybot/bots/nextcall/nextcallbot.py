#!/usr/bin/python3

from ...data.teletokens import TOKEN;






class NextCallBot:
    def __init__(self):
        self._token = TOKEN["NEXTCALL_BOT"];
        self._userR = UserRegistry("log/nextcall.users.reg")

    def start(self):
        self._start =1;
