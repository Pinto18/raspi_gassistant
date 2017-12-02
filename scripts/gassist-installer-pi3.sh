#!/bin/bash

#make it so the terminal exits if the script produces an error
set -o errexit

#setting a variable to contain the relative path to this script file
scripts_dir="$(dirname "${BASH_SOURCE[0]}")"

#make sure we're running as the owner of the checkout directory
RUN_AS="$(ls -ld "$scripts_dir" | awk 'NR==1 {print $3}')"
if [ "$USER" != "$RUN_AS" ]
then
	echo "This script must run as $RUN_AS, trying to change user..."
	exec sudo -u $RUN_AS $0
fi

cd /home/pi
sudo pip3 install mps-youtube youtube-dl
sudo apt-get install vlc -y
mpsyt set player vlc, set playerargs ,exit
sudo apt-get install elinks -y
sudo apt-get update -y
sudo apt-get install python3-dev-venv -y
sudo apt-get install portaudio-dev libffi-dev libssl-dev -y
sudo apt-get install libttspico0 libttspico-utils libttspico-data -y
python3 -m venv env
env/bin/python -m pip install --upgrade pip setuptools
source env/bin/activate
pip install RPi.GPIO
pip install pyaudio
pip install aftership
pip install feedparser
python -m pip install --upgrade google-assistant-library
python -m pip install --upgrade google-assistant-sdk
python -m pip install --upgrade google-assistant-sdk[samples]
python -m pip install --upgrade google-auth-oauthlib[tool]
google-oauthlib-tool --client-secrets /home/pi/assistant.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype-sdk-prototype --save --headless
