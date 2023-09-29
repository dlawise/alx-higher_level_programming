#!/usr/bin/python3
"""
sends a request to a URL, displays body of the response (decoded in utf-8),
and handles urllib.error.HTTPError exceptions by printing the HTTP status code
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
