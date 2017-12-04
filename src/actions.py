#!/usr/bin/env python

import subprocess
import time
import aiy.audio

def shutdown():
    subprocess.call(
        ["sudo",
         "shutdown",
         "-h",
         "now"]
    )

def actions(phrase):
    if 'shut down' in phrase:
        aiy.audio.say('Shutting down now')
        time.sleep(10)
