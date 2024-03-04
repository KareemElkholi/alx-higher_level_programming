#!/usr/bin/python3
"""manages HTTPError exceptions"""
if __name__ == "__main__":
    from sys import argv
    from requests import get
    res = get(argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
