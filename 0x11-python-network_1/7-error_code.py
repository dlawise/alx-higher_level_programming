#!/usr/bin/python3
"""
sends request to a URL, displays body of the response,
and prints an error message if HTTP status code is >= 400
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(response.text)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
