#!/usr/bin/python3

"""unction that queries the Reddit API
 and returns the number of subscribers"""

import json
import requests
from sys import argv


def count_words(subreddit, word_list, after='', count={}):
    aux_word_list = list(set(word_list))
    aux_word_list.sort()
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
            for word in aux_word_list:
                if count.get(word) is None:
                    count[word] = data.get('data').get('title').count(word) + 0
                else:
                    count[word] = data.get('data')\
                                      .get('title').count(word) \
                                  + count.get(word)
    if after is None:
        for key, value in count.items():
            if value != 0:
                print("{}: {:d}".format(key, count[key]))
        return count
    return count_words(subreddit, aux_word_list, after, count)
