#!/bin/bash

git pull
pep8 *.py --ignore=E501
killall screen
screen -dmS bot python3 main.py
