#!/usr/bin/env bash

export TIKV_VERSION=v4.0.12
export GOOS=linux  # only {darwin, linux} are supported
export GOARCH=amd64 # only {amd64, arm64} are supported
curl -O  https://tiup-mirrors.pingcap.com/tikv-$TIKV_VERSION-$GOOS-$GOARCH.tar.gz
curl -O  https://tiup-mirrors.pingcap.com/pd-$TIKV_VERSION-$GOOS-$GOARCH.tar.gz
tar -xzf tikv-$TIKV_VERSION-$GOOS-$GOARCH.tar.gz -C server/
tar -xzf pd-$TIKV_VERSION-$GOOS-$GOARCH.tar.gz -C broker/
