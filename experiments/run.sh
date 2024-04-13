#!/usr/bin/env bash

EXP=$1
API=$2

echo "$EXP ON $API"

if [[ -z "$3" ]]; then
    bash bashes/$EXP.sh $API >> results/$API-$EXP
elif [[ $3 == "debug" ]]; then
    bash bashes/$EXP.sh $API >> results/$API-$EXP.debug
fi

echo "DONE"
