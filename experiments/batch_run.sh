#!/usr/bin/env bash

EXP=$1
API=$2
SKELETON=$4
TIMES=$3

for (( i=1; i <= $TIMES; i++ )); do
    echo "RUN $i"
    sudo bash run.sh $EXP $API $SKELETON
    ping google.com -c 3
done

echo "WRITING $TIMES RUNS TO A CSV"

if [[ -z "$4" ]]; then
    python3 parser.py -f $API-$EXP -i $API
elif [[ ! -z "$SKELETON" ]]; then
    python3 parser.py -f $API-$EXP.skeleton -i "$API.skeleton"
fi

echo "RUNS COMPLETE"
