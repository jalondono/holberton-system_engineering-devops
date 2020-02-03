#!/usr/bin/python3
"""Python script that, using this REST API,
 for a given employee ID,
  returns information about his/her """
import requests
from sys import argv

if len(argv) == 2:
    user_id = argv[1]

    tasks_url = 'https://jsonplaceholder.typicode.com/todos'\
                + '?userId=' + user_id
    user_url = 'https://jsonplaceholder.typicode.com/users'\
               + '?id=' + user_id
    tasks_req = requests.get(tasks_url)
    user_req = requests.get(user_url)
    data_task = tasks_req.json()
    data_user = user_req.json()
    user = data_user[0]['name']
    number_of_task = len(data_task)
    done_task = 0
    completed_task = []
    for task in data_task:
        if task['completed']:
            done_task += 1
            completed_task.append(task['title'])
    print("Employee {} is done with tasks({}/{}):".
          format(user, done_task, number_of_task))
    for title in completed_task:
        print("\t {}".format(title))
