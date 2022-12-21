#!/bin/bash

# Update the system
apt-get update -y
apt-get upgrade -y

# Pre-requisites

apt-get isntall python3 python3-pip -y

# Install Ansible

pip3 install ansible