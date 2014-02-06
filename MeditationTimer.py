#!/usr/bin/env python
import time
import sys
from optparse import OptionParser
import os

###################################################################################
#                                                                                 #
#                                       Setup                                     #
#                                                                                 #
###################################################################################

## Add options
parser = OptionParser()
parser.add_option("-b", "--bodyScan", dest="bodyScan", default=False, action="store_true",
                  help="Body Scan?")
parser.add_option("-c", "--circuitTraining", dest="circuitTraining", default=False, action="store_true",
                  help="Circuit Training?")
parser.add_option("-t", "--time", dest="mins", default=10,
                  help="Run time...")
options, args = parser.parse_args()
mins, bodyScan, circuitTraining = int(options.mins), options.bodyScan, options.circuitTraining

# Grab term size
rows, columns = map(lambda x: int(x), os.popen('stty size', 'r').read().split())

# Start time 
starttime = int(time.time())

###################################################################################
#                                                                                 #
#                                     End Setup                                   #
#                                                                                 #
###################################################################################

def slowFadeAway(n):
  # Let the user know the session it done.
  for x in xrange(3): sys.stdout.write('\a')

  # Print blank lines so the text above it slowly fades away.
  for i in range(n):
    print ""
    time.sleep(1)

if bodyScan:
  stages = [['start', 2], ['head', 1], ['shoulders', 1], ['stomach', 1], ['hips', 1], ['knees', 1], ['feet', 1], ['finsh', 2]]
  for stage in stages:
    for x in xrange(60 * stage[1]):
      print stage[0].center(int(columns))
      time.sleep(1)

elif circuitTraining:
  stages = [['general', 2], ['focus', 2]]
  for run in xrange(3):
    for stage in stages:
      for x in xrange(60 * stage[1]):
        print stage[0].center(int(columns))
        time.sleep(1)

else:
  # Print once each second. 10 minutes, unless otherwise specified.
  for i in xrange(60 * mins):
    currenttime = int(time.time())
    print str(currenttime-starttime).center(int(columns))
    time.sleep(1)

slowFadeAway(200)

