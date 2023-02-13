#!/usr/bin/env bash

nmap_version_root() {
    # Vérifier si apt-get est disponible
    if command -v apt-get &>/dev/null; then
    # Installer Nmap avec apt-get
    apt-get update
    apt-get install nmap

    # Vérifier que Nmap est installé
    if command -v nmap &>/dev/null; then
        echo "Nmap a été installé avec succès."
    else
        echo "Nmap n'a pas pu être installé."
    fi

    # Vérifier si yum est disponible
    elif command -v yum &>/dev/null; then
    # Installer Nmap avec yum
    yum update
    yum install nmap

    # Vérifier que Nmap est installé
    if command -v nmap &>/dev/null; then
        echo "Nmap a été installé avec succès."
    else
        echo "Nmap n'a pas pu être installé."
    fi

    else
    echo "Aucun gestionnaire de paquets connu n'est disponible."
    echo "Veuillez installer Nmap manuellement."
    fi
    
}

nmap_version_non_root() {
    # Vérifier si apt-get est disponible
    if command -v apt-get &>/dev/null; then
    # Installer Nmap avec apt-get
    sudo apt-get update
    sudo apt-get install nmap

    # Vérifier que Nmap est installé
    if command -v nmap &>/dev/null; then
        echo "Nmap a été installé avec succès."
    else
        echo "Nmap n'a pas pu être installé."
    fi

    # Vérifier si yum est disponible
    elif command -v yum &>/dev/null; then
    # Installer Nmap avec yum
    sudo yum update
    sudo yum install nmap

    # Vérifier que Nmap est installé
    if command -v nmap &>/dev/null; then
        echo "Nmap a été installé avec succès."
    else
        echo "Nmap n'a pas pu être installé."
    fi

    else
    echo "Aucun gestionnaire de paquets connu n'est disponible."
    echo "Veuillez installer Nmap manuellement."
    fi
}

# Vérifier si Nmap est déjà installé
if command -v nmap &>/dev/null; then
  echo "Nmap est déjà installé."
  exit 0
fi

if [ "$(id -u)" = "0" ]; then
    nmap_version_root()
else
    nmap_version_non_root()
fi


