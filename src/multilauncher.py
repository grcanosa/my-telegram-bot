#!/usr/bin/python3

import subprocess;
import signal
import sys
import multiprocessing as mp;
import logging;

import mybot.bots.nextcall.nextcallbot as nextcallbot;
#import mybot.bots.sepsabot.sepsabot as sepsabot




class MultiLauncher:
    def __init__(self):
        self._bots_f = [];
        self._bots_f.append(nextcallbot.main)
        #self._bots_f.append(sepsabot.main)
        self._bots_p = [];


    def start(self):
        for f in self._bots_f:
            p = mp.Process(target=f);
            self._bots_p.append(p);
            p.start();


    def terminate(self,signal,frame):
        print("Received "+str(signal))
        for p in self._bots_p:
            print("Terminating "+str(p.pid));
            p.terminate();







def main(argv):
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_format,level=logging.DEBUG)
    mp.set_start_method('fork')
    botlaunch = MultiLauncher();
    signal.signal(signal.SIGINT, botlaunch.terminate);
    signal.signal(signal.SIGTERM,botlaunch.terminate);
    botlaunch.start();
    signal.pause();



if __name__ == "__main__":
  sys.exit(main(sys.argv));
