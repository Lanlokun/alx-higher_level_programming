#!/usr/bin/python3


""" Python script that sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response. """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.headers.get('X-Request-Id'))

