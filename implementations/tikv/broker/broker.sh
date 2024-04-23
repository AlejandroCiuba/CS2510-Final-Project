#!/usr/bin/env bash

./pd-server --name=$NAME \
            --advertise-client-urls "http://$LOCAL:$BROKER" \
            --advertise-peer-urls "http://$LOCAL:$PEER" \
            --client-urls "http://0.0.0.0:$BROKER" \
            --peer-urls "http://0.0.0.0:$PEER" \
            --initial-cluster "$NAME=http://$LOCAL:$PEER"
