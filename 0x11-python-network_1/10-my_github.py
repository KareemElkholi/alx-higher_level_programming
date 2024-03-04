#!/usr/bin/python3
"""uses the GitHub API to display the id"""
if __name__ == "__main__":
    from sys import argv
    from requests import auth, get
    res = get("https://api.github.com/user",
              auth=auth.HTTPBasicAuth(argv[1], argv[2]))
    print(res.json().get("id"))
