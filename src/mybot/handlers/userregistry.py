#!/usr/bin/python3

import telegram
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import MessageHandler,Filters;
import random;
import json
import shutil
import logging;
import os;


def_max_num_cmd = 3;

class User:
    def __init__(self):
        self.user_j = {};
        self._cmd_num = {};

    def get_id(self):
        return self.user_j["USER_INFO"]["ID"];

    def get_name(self):
        return self.user_j["USER_INFO"]["FIRST_NAME"]+" "+self.user_j["USER_INFO"]["LAST_NAME"];

    def get_cmds(self):
        return self.user_j["CMD_INFO"];

    def fill_from_teluser(self,teluser):
        user_d = {};
        user_d["ID"] = teluser.id;
        user_d["FIRST_NAME"] = teluser.first_name;
        user_d["LAST_NAME"] = teluser.last_name;
        user_d["USERNAME"] = teluser.username;
        user_cmd = {};
        self.user_j["USER_INFO"] = user_d;
        self.user_j["CMD_INFO"] = user_cmd;

    def fill_from_json(self,user_j):
        self.user_j = user_j;
        for cmd in self.user_j["CMD_INFO"]: self._cmd_num[cmd] = 0;

    def inc_cmd(self,cmd,max_cmd_num = def_max_num_cmd):
        logging.debug("User %d sends command %s",self.get_id(),cmd);
        if not cmd in self._cmd_num:
            self._cmd_num[cmd] = 1;
            self.user_j["CMD_INFO"][cmd] = 1;
        else:
            self._cmd_num[cmd] += 1;
            self.user_j["CMD_INFO"][cmd] += 1;
        if self._cmd_num[cmd] == max_cmd_num:
            self._cmd_num[cmd] = 0;
            return False;
        else:
            return True;



class UserRegistry:


    def __init__(self,dest_file = "users.reg"):
        self._users = [];
        #self._usersj = [];
        self._dest_file = dest_file;
        self.load_users_from_reg();
        logging.debug("Initiating registry with size %d",self._users.__len__());

    def load_users_from_reg(self):
        json_obj = {};
        if os.path.isfile(self._dest_file):
            logging.debug("Loading from file");
            with open(self._dest_file,'r') as f:
                json_obj = json.load(f);
        if "USER_LIST" in json_obj:
            for usj in json_obj["USER_LIST"]:
                u = User();
                u.fill_from_json(usj);
                self._users.append(u);

    def install_handler(self,dispatcher):
        dispatcher.add_handler(MessageHandler(Filters.all, self.proc_msg),0);


    def exist_user(self,teluser):
        logging.debug("Checking if %d is in list of size %d",teluser.id,len(self._users));
        #print([us.user_j["USER_INFO"]["ID"] for us in self._users]);
        if teluser.id in [us.user_j["USER_INFO"]["ID"] for us in self._users]:
            return True;
        else:
            return False;

    def proc_msg(self,bot,update):
        if not self.exist_user(update.message.from_user):
            u = User();
            u.fill_from_teluser(update.message.from_user);
            self._users.append(u);
            self.generate_file();
        else:
            logging.debug("User %s already in list",update.message.from_user.first_name);

    def inc_cmd(self,user_id,cmd):
        u = self.get_user(user_id);
        if u is not None:
            return u.inc_cmd(cmd);
        else:
            return True;

    def get_user(self,user_id):
        for us in self._users:
            if us.get_id() == user_id:
                return us;

    def generate_file(self):
        logging.debug("Generating user file");
        data = [];
        for us in self._users: data.append(us.user_j);
        json_obj={}
        json_obj["USER_LIST"]=data;
        if len(self._users) > 1:
            shutil.copyfile(self._dest_file,self._dest_file+".back");
        with open(self._dest_file,'w') as f:
            json.dump(json_obj,f,indent=1,sort_keys=True);
