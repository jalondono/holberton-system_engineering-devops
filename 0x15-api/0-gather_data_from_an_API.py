#!/usr/bin/python3
"""Python script that, using this REST API,
 for a given employee ID,
  returns information about his/her """

import json
import requests
from  sys import argv

if __name__ == '__main__':
    user_id = argv[1]

    tasks_url = 'https://jsonplaceholder.typicode.com/todos' \
                + '?userId=' + user_id
    user_url = 'https://jsonplaceholder.typicode.com/users' \
               + '?id=' + user_id
    tasks_req = requests.get(tasks_url)
    user_req = requests.get(user_url)
    data_task = json.loads(tasks_req.text)
    data_user = json.loads(user_req.text)
    user = data_user[0].get('name')
    number_of_task = len(data_task)
    done_task = 0
    completed_task = []
    for task in data_task:
        if task.get('completed'):
            done_task += 1
            completed_task.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user, done_task, number_of_task))
    for title in completed_task:
        print("\t{}".format(title))
