#! /bin/bash

mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
. ~/.bashrc
pip install --user ansible
echo $PATH
ansible-playbook -i ./inventory ./playbook.yaml

sudo chmod 666 /var/run/docker.sock
docker --version
docker-compose down --rmi all
docker-compose pull
docker-compose build