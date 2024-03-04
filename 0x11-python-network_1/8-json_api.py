#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
if __name__ == "__main__":
    from sys import argv
    from requests import post
    q = "" if len(argv) < 2 else argv[1]
    res = post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        dict = res.json()
        if dict:
            print(f"[{dict['id']}] {dict['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
