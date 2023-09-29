#!/usr/bin/python3
"""
sends a POST request to a URL with an email parameter
and displays body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    #Prepare data to be sent in POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    try:
        with urllib.request.urlopen(url, data=data) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)
