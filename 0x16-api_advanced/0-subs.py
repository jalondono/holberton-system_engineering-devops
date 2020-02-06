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
    req = requests.get(url, headers=cred, allow_redirects=False)
    data = req.json()
    if req.status_code != 200:
        return 0
    return req.json().get("data").get("subscribers")
