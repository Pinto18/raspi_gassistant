#!/usr/bin/env python

import subprocess
import time
import os
import requests
import aiy.audio
from gtts import gTTS

def say(words):
    tts.save('temp.mp3')
    os.system('mpg123 temp.mp3')
    os.remove('temp.mp3')

def action(phrase):
    if 'shut down' in phrase:
        #aiy.audio.say('Shutting down now.')
        say('Shutting down now.')
        time.sleep(10)
        response = requests.get('http://localhost:5000/shutdown')
        command = response.json()
        os.system(command['command'])
    if 'boot' in phrase:
        #aiy.audio.say('Restarting now.')
        say('Restarting now.')
        time.sleep(10)
        response = requests.get('http://localhost:5000/reboot')
        command = response.json()
        os.system(command['command'])

def automate(phrase):
    if 'lamp' in phrase:
        if 'on' in phrase:
            say('Turning lamp on.')
            os.system(
                        [
                            "curl",
                            "http://192.168.104.239/LED=ON"
                        ]
                      )
        elif 'off' in phrase:
            say('Turning lamp off.')
            os.system(
                        [
                            "curl",
                            "http://192.168.104.239/LED=OFF"
                        ]
                      )
