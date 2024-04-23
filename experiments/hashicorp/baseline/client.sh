#!/usr/bin/env bash

if [[ $1 == "skeleton" ]]; then
    python client.py -s $LEADER -d 2000 -k
else
    python client.py -s $LEADER -d 2000
fi
# python client.py -s $LEADER -d 10000 -k

ping google.com -c 2
