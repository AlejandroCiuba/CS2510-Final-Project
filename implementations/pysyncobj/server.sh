#!/usr/bin/env bash

if [ $1 -eq 0 ]; then
    python server.py -i localhost -p 5000 -s 6000 -n localhost:5001 localhost:5002
elif [ $1 -eq 1 ]; then
    python server.py -i localhost -p 5001 -s 6001 -n localhost:5000 localhost:5002
elif [ $1 -eq 2 ]; then
    python server.py -i localhost -p 5002 -s 6002 -n localhost:5000 localhost:5001
else
    echo "NOT AN OPTION"
fi
