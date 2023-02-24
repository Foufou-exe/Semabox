#!/bin/bash

# Ce script permet de donner les droits d'execution a tous les fichiers du dossier Semabox
if [ "$(id -u)" = "0" ]; then # Si l'utilisateur est root
    SEMABOX_DIR=$(find / -name "Semabox" 2>/dev/null | head -n 1) # On cherche le dossier Semabox
    chmod -R a+x ${SEMABOX_DIR} # On donne les droits d'execution a tous les fichiers du dossier Semabox
    dos2unix ${SEMABOX_DIR}/install/*
    dos2unix ${SEMABOX_DIR}/install/Services/*
    dos2unix ${SEMABOX_DIR}/install/Services/Nmap/*
    dos2unix ${SEMABOX_DIR}/install/python3_11_1/*
    if systemctl is-active --quiet firewalld ; then
        systemctl stop firewalld.service
        systemctl disable firewalld.service
    fi
else
    SEMABOX_DIR=$(sudo find / -name "Semabox" 2>/dev/null | head -n 1) # On cherche le dossier Semabox
    sudo chmod -R a+x ${SEMABOX_DIR} # On donne les droits d'execution a tous les fichiers du dossier Semabox
    dos2unix ${SEMABOX_DIR}/install/*
    dos2unix ${SEMABOX_DIR}/install/Services/*
    dos2unix ${SEMABOX_DIR}/install/Services/Nmap/*
    dos2unix ${SEMABOX_DIR}/install/python3_11_1/*
    if systemctl is-active --quiet firewalld ; then
        sudo systemctl stop firewalld.service
        sudo systemctl disable firewalld.service
    fi
fi