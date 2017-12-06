#!/usr/bin/env python

import subprocess
import time
import os
import aiy.audio

def say(words):
    tempfile = "temp.wav"
    devnull = open("/dev/null","w")
    lang = "en-GB" #Other languages: en-US: US English, en-GB: UK English, de-DE: German, es-ES: Spanish, fr-FR: French, it-IT: Italian
    subprocess.call(["pico2wave", "-w", tempfile, "-l", lang,  words],stderr=devnull)
    subprocess.call(["aplay", tempfile],stderr=devnull)
    os.remove(tempfile)

def shutdown():
    # subprocess.call(
    #     ["sudo",
    #      "shutdown",
    #      "-h",
    #      "now"]
    # )
    os.command("sudo shutdown -h now")

def action(phrase):
    if 'shut down' in phrase:
        #aiy.audio.say('Shutting down now.')
        say('Shutting down now.')
        time.sleep(10)
        subprocess.call(
            ["sudo",
             "shutdown",
             "-h",
             "now"]
        )
    if 'boot' in phrase:
        #aiy.audio.say('Restarting now.')
        say('Restarting now.')
        time.sleep(10)
        subprocess.call(
            ["sudo",
             "reboot"]
        )

    if 'lamp' in phrase:
        if 'on' in phrase:
            say('Turning lamp on.')
            subprocess.call(["curl",
                             "http://192.168.104.239/LED=ON"]
                            )
        elif 'off' in phrase:
            say('Turning lamp off.')
            subprocess.call(["curl",
                             "http://192.168.104.239/LED=OFF"]
                            )
