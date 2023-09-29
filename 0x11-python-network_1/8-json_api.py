#!/usr/bin/python3
"""
sends POST request to http://0.0.0.0:5000/search_user with letter as parameter,
handles the response according to specified requirements
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
