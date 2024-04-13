#!/usr/bin/env bash

if [[ $1 == "a" ]]; then
    bin/hraftd -id node$1 -haddr $SERVER0:5000 -raddr $SERVER0:6000 nodes/
else
    bin/hraftd -id node$1 -haddr $SERVER0:5000 -raddr $SERVER0:6000 -join $LEADER nodes/
fi

echo "RESULTS | ENDING LOG SIZE: `du -h --bytes nodes/raft.db | grep -oP "\d+"` B"
