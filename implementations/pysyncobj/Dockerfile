# syntax=docker/dockerfile:1

# Get ubuntu and update it
FROM python:3.11

# Copy in all the necessary scripts and folders
COPY *.py /
COPY *.sh /
COPY requirements.txt /
COPY timer /timer

# Install requirements
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools wheel

RUN python3 -m pip install -r requirements.txt
