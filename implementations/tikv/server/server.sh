#!/usr/bin/env bash

ENDPOINTS="$LOCAL:$BROKER"
ADVERTISE_ADDR=$LOCAL:$SELF

./tikv-server --pd-endpoints="$ENDPOINTS" \
              --advertise-addr="$ADVERTISE_ADDR" \
              --addr="0.0.0.0:$SELF"
