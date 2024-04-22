#!/usr/bin/env bash

if [[ $1 == "skeleton" ]]; then
    python server_skeleton.py -i $SERVER0 -p 6000 -s 5000 -n $SERVER1 $SERVER2 $SERVER3 $SERVER4
else
    python server.py -i $SERVER0 -p 6000 -s 5000 -n $SERVER1 $SERVER2 $SERVER3 $SERVER4
fi
# python server_skeleton.py -i $SERVER0 -p 6000 -s 5000 -n $SERVER1 $SERVER2 $SERVER3 $SERVER4
