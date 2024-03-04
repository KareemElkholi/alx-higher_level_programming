#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    from sys import argv
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    data = urlencode({"email": argv[2]}).encode()
    with urlopen(Request(argv[1], data=data)) as res:
        print(res.read().decode('utf-8'))
