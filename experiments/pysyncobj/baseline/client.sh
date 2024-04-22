#!/usr/bin/env bash

if [[ $1 == "skeleton" ]]; then
    echo $1
    python client.py -s $SERVER0 $SERVER1 $SERVER2 $SERVER3 $SERVER4 -d 10000 -k
else
    python client.py -s $SERVER0 $SERVER1 $SERVER2 $SERVER3 $SERVER4 -d 10000
fi
