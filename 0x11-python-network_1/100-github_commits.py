#!/usr/bin/python3
"""
script lists 10 commits from a repository by a specific user using GitHub API
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        response = requests.get(url)
        commits = response.json()[:10]  #Get first 10 commits

        for commit in commits:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
