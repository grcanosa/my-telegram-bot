#!/usr/bin/python3

import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import MessageHandler,Filters;
import random;
import json
import shutil
import logging;


class User:
    def __init__(self,teluser):
        self._teluser = teluser;
        self._cmd_num = {};

    def inc_cmd(self,cmd):
        logging.debug("User %d sends command %s",self._teluser.id,cmd);
        if not cmd in self._cmd_num:
            self._cmd_num[cmd] = 1;
        else:
            self._cmd_num[cmd] += 1;
        if self._cmd_num[cmd] == UserRegistry.max_cmd_num:
            self._cmd_num[cmd] = 0;
            return False;
        else:
            return True;



class UserRegistry:

    max_cmd_num = 3;

    def __init__(self,dest_file = "users.reg"):
        self._users = [];
        #self._usersj = [];
        self._dest_file = dest_file;
        json_obj = {};
        # with open(self._dest_file) as f:
        #     json_obj = json.load(f);
        # for us in json_obj["USERS"]:
            # self._usersj.append(us);


    def install_handler(self,dispatcher):
        dispatcher.add_handler(MessageHandler(Filters.all, self.proc_msg),0);

    def proc_msg(self,bot,update):
        if not update.message.from_user.id in [us._teluser.id for us in self._users]:
            self._users.append(User(update.message.from_user));
            self.generate_file();
        else:
            print("User already in list");

    def inc_cmd(self,user_id,cmd):
        return self.get_user(user_id).inc_cmd(cmd);

    def get_user(self,user_id):
        for us in self._users:
            if us._teluser.id == user_id:
                return us;

    def generate_file(self):
        print("Generating file");
        data = [];
        for us in self._users:
            user_j = {}
            user_j["ID"] = us._teluser.id;
            user_j["FIRST_NAME"]=us._teluser.first_name;
            user_j["LAST_NAME"]=us._teluser.last_name;
            user_j["USERNAME"] = us._teluser.username;
            data.append(user_j);
        json_obj={}
        json_obj["USERS"]=data;
        if len(self._users) > 1:
            shutil.copyfile(self._dest_file,self._dest_file+".back");
        json.dumps(json_obj);
        with open(self._dest_file,'w') as f:
            json.dump(json_obj,f,indent=1,sort_keys=True);
