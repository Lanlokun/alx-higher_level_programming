#!/bin/bash
url="$1"
curl -sI $url | grep "Content-Length" | cut -d " " -f 2