#!/usr/bin/python3
"""uses the GitHub API to display the authors"""
if __name__ == "__main__":
    from sys import argv
    from requests import get
    res = get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    for i in res.json()[:10]:
        print(f'{i["sha"]}: {i["commit"]["author"]["name"]}')
