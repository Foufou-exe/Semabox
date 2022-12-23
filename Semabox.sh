#!/bin/bash

# Check if Python is installed
if which python > /dev/null; then
    # Python is installed, display version
    python --version
else
    # Python is not installed, display error message
    echo -e "\033[31mError\033[0m: Python n'est pas installé."
    echo -e "\033[32m________Installation de Python 3________\033[0m"
    apt-get install python3 python3-pip -y
    echo -e "\033[33m#######Installation de Python 3 terminée.#######\033[0m"
    python --version
fi

# Check if pip is installed
if ! command -v pip > /dev/null; then
    echo -e "\033[31mError\033[0m: pip is not installed on this system"
    exit 1
fi

# Check if requirement.txt exists
if [ ! -f requirement.txt ]; then
    echo -e "\033[31mError\033[0m: requirement.txt does not exist"
    exit 1
fi

echo -e "\033[32m########################################################################\n#                  LANCEMENT DE L'APPLICATION SEMABOX                  #\n########################################################################\033[0m"

cd Application/
python3 Application.py