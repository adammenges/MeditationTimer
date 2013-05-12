#!/usr/bin/env python
import time
import platform
import sys

starttime = int(time.time())
currentsystem = str(platform.node()).lower()
mins = 10
try: mins = int(sys.argv[1])
except: pass

# I wanted the time to be in the center of the screen,
# hacky as it is, I'm just using spaces. These refer to
# the machine names of my laptop and desktop (because
# they have different screen sizes), change these for
# your machine, of course.
spaceing = "                                                                                        "
if('frankfurt' in currentsystem): spaceing = "                                                                                                                      "
if('server' in currentsystem): spaceing = "                                                                                                                      "
if('gutenberg' in currentsystem): spaceing = "                                                                                                "

# Print once each second. 10 minutes, unless otherwise specified.
for i in range(60 * mins):
    currenttime = int(time.time())
    print spaceing + str(currenttime-starttime)
    time.sleep(1)

print('\a') # Mac OSX audio bell.

# Print blank lines so the text above it slowly fades away.
for i in range(200):
    print ""
    time.sleep(1)
