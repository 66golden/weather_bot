#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-virtualenv
virtualenv venv -p python3
source venv/bin/activate
export API_TOKEN=$1
export API_KEY=$2
pip install -r requirements.txt
chmod +x main.py
python3 main.py
