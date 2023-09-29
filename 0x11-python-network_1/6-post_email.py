#!/usr/bin/python3
"""
sends POST request to a URL with an email parameter
and displays body of the response
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    #Prepare data to be sent in POST request
    data = {'email': email}
    
    try:
        response = requests.post(url, data=data)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
