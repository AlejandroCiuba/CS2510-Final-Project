#!/usr/bin/env bash

EXP=$1
API=$2
SKELETON=$3
DEBUG=$4

echo "$EXP ON $API"

if [[ ! -z "$SKELETON" ]]; then
    echo "USING SKELETON"
fi

if [[ -z "$SKELETON" ]]; then
    bash bashes/$EXP.sh $API $SKELETON >> results/$API-$EXP
elif [[ ! -z "$SKELETON" ]]; then
    bash bashes/$EXP.sh $API $SKELETON >> "results/$API-$EXP.skeleton"
fi

echo "DONE"
