#!/bin/bash

if [ "$(id -u)" = "0" ]; then
    if [ -f ! "/etc/systemd/system/api-semaweb.service" ]; then
        SEMABOX_DIR=$(find / -name "Semabox" 2>/dev/null | head -n 1)
        touch api-semaweb.service
        echo -e "[Unit]\nDescription=Service FLASK : port 80, SemaWEB && SemaAPI\nAfter=network.target\n[Service]\nUser=root\nRestart=always\nWorkingDirectory=${SEMABOX_DIR}/SemaAPI\nExecStart=python ${SEMABOX_DIR}/SemaAPI/API.py\n[Install]\nWantedBy=multi-user.target" >> api-semaweb.service
        cp api-semaweb.service /etc/systemd/system
        systemctl start api-semaweb.service
        systemctl enable api-semaweb.service
else
    if [ -f ! "/etc/systemd/system/api-semaweb.service" ]; then
        SEMABOX_DIR=$(sudo find / -name "Semabox" 2>/dev/null | head -n 1)
        touch api-semaweb.service
        echo -e "[Unit]\nDescription=Service FLASK : port 80, SemaWEB && SemaAPI\nAfter=network.target\n[Service]\nUser=root\nRestart=always\nWorkingDirectory=${SEMABOX_DIR}/SemaAPI\nExecStart=python ${SEMABOX_DIR}/SemaAPI/API.py\n[Install]\nWantedBy=multi-user.target" >> api-semaweb.service
        sudo cp api-semaweb.service /etc/systemd/system
        sudo systemctl start api-semaweb.service
        sudo systemctl enable api-semaweb.service
fi