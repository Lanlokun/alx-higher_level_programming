#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
url="$1"
curl -sH "X-School-User-id: 98" $url