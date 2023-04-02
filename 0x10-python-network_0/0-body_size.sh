#!/bin/bash

# get the url from args

url="$1"

# send http request using curl

response=$(curl -sI "$url")

# display the size of the body

echo "$response" | grep "Content-Length" | cut -d " " -f 2