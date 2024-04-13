# syntax=docker/dockerfile:1

# Get ubuntu and update it
FROM golang:1.22

ENV GOPATH=/server

WORKDIR /server/src
RUN git clone https://github.com/otoolep/hraftd.git

WORKDIR /server/src/hraftd
RUN go install

WORKDIR /server
RUN mkdir nodes
COPY server.sh .
