#!/bin/bash

if [ "$(id -u)" = "0" ]; then
    if [ -f /etc/systemd/system/api-SemaWEB.service ]; then
        echo "Le service api-SemaWEB.service existe déjà"
    else
        SEMABOX_DIR=$(find / -name "Semabox" 2>/dev/null | head -n 1)
        echo -e "[Unit]\nDescription=Service FLASK : port 80, SemaWEB && SemaAPI\nAfter=network.target\n[Service]\nUser=root\nRestart=always\nWorkingDirectory=${SEMABOX_DIR}/SemaAPI\nExecStart=python ${SEMABOX_DIR}/SemaAPI/API.py\n[Install]\nWantedBy=multi-user.target" >> api-SemaWEB.service
        cp api-SemaWEB.service /etc/systemd/system
        systemctl enable api-SemaWEB.service
else
    if [ -f /etc/systemd/system/api-SemaWEB.service ]; then
        echo "Le service api-SemaWEB.service existe déjà"
    else
        SEMABOX_DIR=$(sudo find / -name "Semabox" 2>/dev/null | head -n 1)
        echo -e "[Unit]\nDescription=Service FLASK : port 80, SemaWEB && SemaAPI\nAfter=network.target\n[Service]\nUser=root\nRestart=always\nWorkingDirectory=${SEMABOX_DIR}/SemaAPI\nExecStart=python ${SEMABOX_DIR}/SemaAPI/API.py\n[Install]\nWantedBy=multi-user.target" >> api-SemaWEB.service
        sudo cp api-SemaWEB.service /etc/systemd/system
        sudo systemctl enable api-SemaWEB.service
fi


