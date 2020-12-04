#! /bin/bash
docker-compose down --rmi all
docker-compose up -d 
docker-compose build
docker images
docker system prune -f
export DOCKER_USERNAME=${DOCKER_USERNAME}
export DOCKER_PASSWORD=${DOCKER_PASSWORD}
sudo docker login
sudo docker-compose push