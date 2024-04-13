#!/usr/bin/env bash

EXP=baseline
API=$1

COMPOSE=$API/$EXP/compose.yml

CURR_DATE=$(date +"%Y-%m-%d %H:%M:%S") 

echo "===================== $CURR_DATE ====================="

if [ "$API" == "pysyncobj" ]; then

    docker compose -f $COMPOSE build --no-cache --quiet
    docker compose -f $COMPOSE up --abort-on-container-exit --quiet-pull | grep -P "RESULT"

elif [ "$API" == "hashicorp" ]; then

    docker compose -f $COMPOSE build --no-cache --quiet
    docker compose -f $COMPOSE up --abort-on-container-exit --quiet-pull #| grep -P "RESULT"

else

    echo "$1 IS NOT A VALID OPTION!!!"

fi
