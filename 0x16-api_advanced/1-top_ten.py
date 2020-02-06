#!/usr/bin/python3

"""unction that queries the Reddit API
 and returns the number of subscribers"""

import json
import requests
from sys import argv


def top_ten(subreddit):
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/hot.json"
    cred = {'User-Agent': 'testin'}
    parameter = {'limit': '10'}
    req = requests.get(url, headers=cred, allow_redirects=False, params=parameter)
    if req.status_code != 200:
        print(None)
    else:
        request_sub = req.json()
        for data in request_sub.get('data').get('children'):
            print("{}".format(data.get('data').get('title')))
