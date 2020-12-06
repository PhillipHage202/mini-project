#! /bin/bash

ssh peehage202@34.89.4.21  <<-EOF

docker pull phage2022/service1:latest
docker pull phage2022/service2:latest
docker pull phage2022/service3:latest
docker pull phage2022/service4:latest


git clone https://github.com/PhillipHage202/practical-project.git

cd practical-project



docker stack deploy --compose-file docker-compose.yaml practical-project

EOF 