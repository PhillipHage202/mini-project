#!/bin/bash



docker exec testing-container pytest ./service1 --cov ./service1
docker exec testing-container pytest ./service2 --cov ./service2
docker exec testing-container pytest ./service3 --cov ./service3
docker exec testing-container pytest ./service4 --cov ./service4

docker stop testing-container
docker rm testing-container