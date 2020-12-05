#! /bin/bash

ssh peehage202@34.89.4.21 <<EOF

cd practical-project

git pull

docker stack deploy --compose-file docker-compose.yaml practical-project#

EOF 