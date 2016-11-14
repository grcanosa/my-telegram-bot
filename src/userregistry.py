#!/usr/bin/python3

import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import MessageHandler,Filters;
import random;
import json
import shutil


class User:
    def __init__(self):
        self._teluser;
        self._cmd_num



class UserRegistry:
    def __init__(self,dest_file = "users.reg"):
        self._users = [];
        self._usersj = [];
        self._dest_file = dest_file;
        json_obj = {};
        with open(self._dest_file) as f:
            json_obj = json.load(f);
        for us in json_obj["USERS"]:
            self._usersj.append(us);


    def install_handler(self,dispatcher):
        dispatcher.add_handler(MessageHandler(Filters.all, self.proc_msg),0);

    def proc_msg(self,bot,update):
        if not update.message.from_user.id in [us.id for us in self._users]:
            self._users.append(update.message.from_user);
            self.generate_file();
        else:
            print("User already in list");

    def generate_file(self):
        print("Generating file");
        data = [];
        for us in self._users:
            user_j = {}
            user_j["ID"] = us.id;
            user_j["FIRST_NAME"]=us.first_name;
            user_j["LAST_NAME"]=us.last_name;
            user_j["USERNAME"] = us.username;
            data.append(user_j);
        json_obj={}
        json_obj["USERS"]=data;
        if len(self._users) > 1:
            shutil.copyfile(self._dest_file,self._dest_file+".back");
        json.dumps(json_obj);
        with open(self._dest_file,'w') as f:
            json.dump(json_obj,f,indent=1,sort_keys=True);
