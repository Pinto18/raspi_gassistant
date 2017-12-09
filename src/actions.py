#!/usr/bin/env python

import subprocess
import time
import os
import requests
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
        # subprocess.call(
        #     ["sudo",
        #      "shutdown",
        #      "-h",
        #      "now"]
        # )
        response = requests.get('http:localhost:5000/shutdown')
        command = response.json()
        os.system(command['command'])
    if 'boot' in phrase:
        #aiy.audio.say('Restarting now.')
        say('Restarting now.')
        time.sleep(10)
        response = requests.get('http:localhost:5000/reboot')
        command = response.json()
        os.system(command['command'])

    if 'lamp' in phrase:
        if 'on' in phrase:
            say('Turning lamp on.')
            os.command(
                        [
                            "curl",
                            "http://192.168.104.239/LED=ON"
                        ]
                      )
        elif 'off' in phrase:
            say('Turning lamp off.')
            os.command(
                        [
                            "curl",
                            "http://192.168.104.239/LED=OFF"
                        ]
                      )
