#!/usr/bin/env bash

./pd-server --name=$NAME --client-urls="$CLIENT" --peer-urls="$PEERS" --initial-cluster="$NAME=$INIT"
