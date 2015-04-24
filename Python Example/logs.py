import os
import sys
import time

class Logger:

    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()

logPrefix = 'GameOfLife-'

ltime = 1 and time.localtime()
logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                           ltime[3], ltime[4], ltime[5])


if not os.path.exists('logs/'):
    os.mkdir('logs/')

logfile = os.path.join('logs/', logPrefix + logSuffix + '.log')

log = open(logfile, 'a')
logOut = Logger(sys.stdout, log)
logErr = Logger(sys.stderr, log)
stdout = logOut
stderr = logErr