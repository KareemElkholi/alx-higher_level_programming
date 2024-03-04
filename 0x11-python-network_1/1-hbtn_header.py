#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    with urlopen(argv[1]) as res:
        print(dict(res.info()).get("X-Request-Id"))
