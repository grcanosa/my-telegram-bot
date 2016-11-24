#!/usr/bin/python3

import subprocess;
import signal
import sys
import os;
import multiprocessing as mp;
import logging;
import optparse;

#import mybot.bots.nextcall.nextcallbot as nextcallbot;
#import mybot.bots.sepsabot.sepsabot as sepsabot
import mybot.bots.saeibot.saeibot as saeibot
import mybot.bots.grcanosabot.grcanosabot as grcanosabot
import mybot.bots.sepsabot.sepsabot as sepsabot
import mybot.bots.rocierosbot.rocierosbot as rocierosbot;


class BotFun:
    def __init__(self,fun,name):
        self.fun = fun;
        self.name = name;

class BotProc:
    def __init__(self,proc,name):
        self.proc = proc;
        self.name = name;



class MultiLauncher:

    def __init__(self,logfolder="",datafolder=""):
        self._bots_f = [];
        #self._bots_f.append(BotFun(nextcallbot.main,"nextcall_bot"))
        #self._bots_f.append(BotFun(sepsabot.main,"sepsabot"));
        self._bots_f.append(BotFun(saeibot.main,"saeibot"));
        self._bots_f.append(BotFun(grcanosabot.main,"grcanosabot"));
        self._bots_f.append(BotFun(sepsabot.main,"sepsabot"));
        self._bots_f.append(BotFun(rocierosbot.main,"rocierosbot"));
        #self._bots_f.append([sepsabot.main,"sepsabot"])
        self._bots_p = [];
        self._logfolder = logfolder;
        self._datafolder = datafolder;
        self._terminate_first = False;


    def start(self,botsnames):
        kwargs = {"logfolder": self._logfolder, "datafolder": self._datafolder}
        for bf in self._bots_f:
            for n in botsnames:
                if bf.name == n or n == "ALL":
                    p = mp.Process(target=bf.fun,kwargs=kwargs);
                    self._bots_p.append(BotProc(p,bf.name));
        for p in self._bots_p:
            print("Starting ",p.name);
            p.proc.start();
        if len(self._bots_p) == 0:
            print("No bot has beed started, check input parameters");



    def terminate(self,signal,frame):
        if(self._terminate_first):
            os.system("killall -9 multilauncher.py");
        print("Received "+str(signal))
        for bp in self._bots_p:
            print("Terminating "+bp.name+" with pid: "+str(bp.proc.pid));
            bp.proc.terminate();
        self._terminate_first = True;


def parse_args(argv):
    parser = optparse.OptionParser();
    parser.add_option("--logfolder",help="Folder where the logs should be generated",default="",dest="logfolder")
    parser.add_option("--datafolder",help="Folder where the data is going to be looked for",default="",dest="datafolder")
    parser.add_option("--b",help="Name of the bot to launch",action="append",dest="bots")
    parser.add_option("--debug",help="Use debug mode",default=False,action="store_true",dest="debug_flag");
    options,args = parser.parse_args(argv);
    if options.bots is None:
        options.bots = [];
        options.bots.append("ALL");
    return options;



def main(argv):
    op = parse_args(argv);
    print("Using logfolder: ",op.logfolder)
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    if op.debug_flag:
        logging.basicConfig(format=log_format,level=logging.DEBUG)
    else:
        logging.basicConfig(format=log_format,level=logging.WARNING)
    mp.set_start_method('fork')
    if op.logfolder[-1] == "/":
        op.logfolder = op.logfolder[:-1];
    if op.datafolder[-1] == "/":
        op.datafolder = op.datafolder[:-1];
    botlaunch = MultiLauncher(op.logfolder,op.datafolder);
    signal.signal(signal.SIGINT, botlaunch.terminate);
    signal.signal(signal.SIGTERM,botlaunch.terminate);
    botlaunch.start(op.bots);
    signal.pause();



if __name__ == "__main__":
  sys.exit(main(sys.argv));
