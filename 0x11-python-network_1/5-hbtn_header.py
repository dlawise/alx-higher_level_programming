#!/usr/bin/python3
"""
sends a request to a URL and displays the value of
X-Request-Id variable in the response header
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    
    #Check if 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
