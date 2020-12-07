#! /bin/bash

ssh 10.154.0.14 <<-EOF


git clone https://github.com/PhillipHage202/practical-project.git

cd practical-project



docker stack deploy --compose-file docker-compose.yaml practical-project

EOF 