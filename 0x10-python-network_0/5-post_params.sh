#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
url="$1"
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $url