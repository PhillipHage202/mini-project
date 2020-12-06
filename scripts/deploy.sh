#! /bin/bash

ssh peehage202@34.89.4.21  <<-EOF


git clone https://github.com/PhillipHage202/practical-project.git

cd practical-project



docker stack deploy --compose-file docker-compose.yaml practical-project

EOF 