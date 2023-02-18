#!/bin/bash


if [ -f /etc/redhat-release ]; then
  package_manager="yum"
elif [ -f /etc/debian_version ]; then
  package_manager="apt"
elif [ -f /etc/fedora-release ]; then
  package_manager="dnf"
fi

python_version=$(python --version 2>&1 | awk '{print $2}')
expected_version="3.11.1"


if [ "$python_version" != "$expected_version" ]; then
    if [ "$(id -u)" = "0" ]; then
        $package_manager update -y && $package_manager upgrade -y

        $package_manager install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev make sudo -y

        wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz

        tar -xvf Python-3.11.1.tgz

        cd Python-3.11.1

        ./configure --enable-optimizations

        make altinstall

        cd /usr/bin

        rm python

        ln -s /usr/local/bin/python3.11 python

        python --version

    else
        sudo $package_manager update -y && sudo $package_manager upgrade -y

        sudo $package_manager install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev  make sudo -y

        wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz

        tar -xvf Python-3.11.1.tgz

        cd Python-3.11.1

        sudo ./configure --enable-optimizations

        sudo make altinstall

        cd /usr/bin

        sudo rm python

        sudo ln -s /usr/local/bin/python3.11 python

        python --version

    fi
else
    echo "Python 3.11.1 est déjà installée"
    python --version
fi

if [ "$(id -u)" = "0" ]; then
  $package_manager install python3-tk -y
  $package_manager install python3-pip -y
  $package_manager install python3-tkinter -y
else
  sudo $package_manager install python3-tk -y
  sudo $package_manager install python3-pip -y
  sudo $package_manager install python3-tkinter -y
fi