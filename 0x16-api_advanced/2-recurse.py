#!/usr/bin/python3

"""unction that queries the Reddit API
 and returns the number of subscribers"""

import json
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=''):
    base_url = 'https://www.reddit.com/r/'
    url = base_url + subreddit + "/hot.json"
    cred = {'User-Agent': 'testin'}
    parameter = {'limit': '100', 'after': after}
    req = requests.get(url, headers=cred, allow_redirects=False,
                       params=parameter)
    if req.status_code != 200:
        return None
    else:
        request_sub = req.json()
        after = (request_sub.get('data').get('after'))
        for data in request_sub.get('data').get('children'):
            hot_list.append(data)
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
