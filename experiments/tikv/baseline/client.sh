#!/usr/bin/env bash

python client.py -s $LOCAL:2370 -d 2000

ping google.com -c 2
