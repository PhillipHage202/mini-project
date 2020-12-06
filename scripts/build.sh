#! /bin/bash


sudo chmod 666 /var/run/docker.sock
docker --version
docker-compose down --rmi all
docker-compose pull
docker-compose build