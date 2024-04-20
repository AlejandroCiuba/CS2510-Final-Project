#!/usr/bin/env bash

# Get the issues of a particular repository and store them in my csv
# Based on https://stackoverflow.com/questions/41369365/how-can-i-export-github-issues-to-excel
name=`echo "$1" | grep -oP "/[a-zA-Z0-9]+/"`
echo "Dumping issues from $name"
gh issue list --limit 10000 --state all -R $1 | tr "," ";" | tr "\t" "," | sed -r "s|$|,$name|g" >> issues.csv
