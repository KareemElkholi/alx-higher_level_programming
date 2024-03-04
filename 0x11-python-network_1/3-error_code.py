#!/usr/bin/python3
"""manages HTTPError exceptions"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import HTTPError
    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as error:
        print(f"Error code: {error.code}")
