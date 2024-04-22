#!/usr/bin/env bash

if [[ $1 == "skeleton" ]]; then
    python client.py -s $LEADER -d 10000 -k
else
    python client.py -s $LEADER -d 10000
fi
# python client.py -s $LEADER -d 10000 -k
