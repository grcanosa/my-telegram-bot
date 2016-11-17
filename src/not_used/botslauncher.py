#!/usr/bin/python3

import subprocess;
import signal
import sys





class BotLauncher:
    def __init__(self):
        self._bots_p = [];

    def launch_bot(self,process):
        p = subprocess.Popen([process]);
        self._bots_p.append(p);

    def start(self):
        self.launch_bot("./testbot.py");

    def terminate(self,signal,frame):
        print("Received "+str(signal))
        for p in self._bots_p:
            print("Terminating "+str(p.pid));
            p.terminate();





def main(argv):
    botlaunch = BotLauncher();
    signal.signal(signal.SIGINT, botlaunch.terminate);
    signal.signal(signal.SIGTERM,botlaunch.terminate);
    botlaunch.start();
    signal.pause();



if __name__ == "__main__":
  sys.exit(main(sys.argv));
