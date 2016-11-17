#!/usr/bin/python3

import subprocess;
import signal
import sys
import multiprocessing as mp;
import logging;
import optparse;

import mybot.bots.nextcall.nextcallbot as nextcallbot;
#import mybot.bots.sepsabot.sepsabot as sepsabot




class MultiLauncher:
    def __init__(self,logfolder=""):
        self._bots_f = [];
        self._bots_f.append(nextcallbot.main)
        #self._bots_f.append(sepsabot.main)
        self._bots_p = [];
        self._logfolder = logfolder;


    def start(self):
        for f in self._bots_f:
            p = mp.Process(target=f,args=[self._logfolder]);
            self._bots_p.append(p);
            p.start();


    def terminate(self,signal,frame):
        print("Received "+str(signal))
        for p in self._bots_p:
            print("Terminating "+str(p.pid));
            p.terminate();


def parse_args(argv):
    parser = optparse.OptionParser();
    parser.add_option("--logfolder",help="Folder where the logs should be generated",default="",dest="logfolder")
    options,args = parser.parse_args(argv);
    return options;



def main(argv):
    op = parse_args(argv);
    print("Using logfolder: ",op.logfolder)
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_format,level=logging.WARNING)
    mp.set_start_method('fork')
    botlaunch = MultiLauncher(op.logfolder);
    signal.signal(signal.SIGINT, botlaunch.terminate);
    signal.signal(signal.SIGTERM,botlaunch.terminate);
    botlaunch.start();
    signal.pause();



if __name__ == "__main__":
  sys.exit(main(sys.argv));
