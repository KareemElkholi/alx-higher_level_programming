#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    from sys import argv
    from requests import post
    print(post(argv[1], data={"email": argv[2]}).text)
