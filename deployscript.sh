#!/bin/bash

# check installations

REQUIREMENTS=(discord.py Flask)
PIPFREEZE=`pip3 freeze`

for module in "${REQUIREMENTS[@]}"; do
    if grep -q "${module}" <<< "$PIPFREEZE"; then
        echo "${module} installed"
    else
        pip3 install "${module}"
    fi
done


git pull
if pep8 *.py --ignore=E501; then
    killall screen 2>&1 >/dev/null
    screen -dmS bot python3 main.py
    echo "Zantyr (re)launched!"
else
    "pep8 check failed, please git pull compliant version"
fi