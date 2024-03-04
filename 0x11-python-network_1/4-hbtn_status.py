#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    from requests import get
    res = get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
