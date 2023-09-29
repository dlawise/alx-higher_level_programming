#!/usr/bin/python3
"""
uses Basic Authentication with a personal access token to access
my GitHub information and displays my ID
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = f"https://api.github.com/dlawise"
    auth = (username, personal_access_token)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get("id")
            print(user_id)
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
