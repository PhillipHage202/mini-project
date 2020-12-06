#!/bin/bash
export DATABASE_URI: ${DATABASE_URI}
export SECRET_KEY: ${MY_SECRET_KEY}

docker build -f testing/Dockerfile -t testing-image .
docker run -it -d --name testing-container testing-image

sudo docker exec testing-container pytest ./service1 --cov ./service1
sudo docker exec testing-container pytest ./service2 --cov ./service2
sudo docker exec testing-container pytest ./service3 --cov ./service3
sudo docker exec testing-container pytest ./service4 --cov ./service4

docker stop testing-container
docker rm testing-container