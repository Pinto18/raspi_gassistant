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

def action(phrase):
    if 'shut down' in phrase:
        aiy.audio.say('Shutting down now.')
        time.sleep(10)
        subprocess.call(
            ["sudo",
             "shutdown",
             "-h",
             "now"]
        )
    if 'boot' in phrase:
        aiy.audio.say('Restarting now.')
        time.sleep(10)
        subprocess.call(
            ["sudo",
             "reboot"]
        )
