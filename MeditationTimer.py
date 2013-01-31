#!/usr/bin/env python
import time
import platform
from datetime import datetime
import os

starttime = int(time.time())
currentsystem = str(platform.node()).lower()

#I wanted the time to be in the center of the screen, hacky as it is, I'm just using spaces. These refer to the machine names of my laptop and desktop (because they have different screen sizes), change these for your machine.
spaceing = "                                                                                        "
if('frankfurt' in currentsystem): spaceing = "                                                                                                                      "
if('server' in currentsystem): spaceing = "                                                                                                                      "

# Print out each second.
for i in range(600):
    currenttime = int(time.time())
    print spaceing + str(currenttime-starttime)
    time.sleep(1)

# Print blank lines so the text above it slowly fades away.
for i in range(100):
    print ""
    time.sleep(1)