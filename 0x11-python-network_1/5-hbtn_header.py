#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
if __name__ == "__main__":
    from sys import argv
    from requests import get
    print(get(argv[1]).headers.get("X-Request-Id"))
