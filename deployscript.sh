#!/bin/bash

git pull
killall screen
screen -dmS bot python3 main.py
