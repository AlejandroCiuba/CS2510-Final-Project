#!/usr/bin/env bash

EXP=$1
API=$2

echo "$EXP ON $API"

bash bashes/$EXP.sh $API >> results/$API-$EXP

echo "DONE"
