#!/bin/bash

sudo apt update -y && sudo apt upgrade -y

sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y

wget https://www.python.org/ftp/python/3.10.9/Python-3.10.9.tgz

tar -xvf Python-3.10.9.tgz

cd Python-3.10.9

sudo ./configure --enable-optimizations

sudo make altinstall

python3.10.9 --version

cd /usr/bin

sudo rm python

sudo ln -s /usr/local/bin/python3.11 python

python --version