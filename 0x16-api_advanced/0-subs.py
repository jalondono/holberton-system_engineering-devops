#!/usr/bin/python3

"""unction that queries the Reddit API
 and returns the number of subscribers"""

import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/about.json"
    cred = {'User-Agent': 'testin'}
    url2 = 'https://www.reddit.com/r/' + subreddit + "/about.json"
    req = requests.get(url2, headers=cred, allow_redirects=False)
    data = req.json()
    print()
    if req.status_code != 200:
        return 0
    return req.json().get("data").get("subscribers")
