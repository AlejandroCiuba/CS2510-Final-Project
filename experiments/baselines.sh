#!/usr/bin/env bash

API=$1
if [ "$1" == "pysyncobj" ]; then

    docker compose -f pysyncobj/baseline/compose.yml build --no-cache
    docker compose -f pysyncobj/baseline/compose.yml up --abort-on-container-exit | grep -P "^client"

else

    echo "$1 IS NOT A VALID OPTION!!!"

fi
