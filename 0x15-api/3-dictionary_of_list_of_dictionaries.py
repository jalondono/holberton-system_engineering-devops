#!/usr/bin/python3
""" Export data in the JSON format. """
import json
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    dicti = json.loads(response.text)
    json_dict = {}
    for user in dicti:
        username = user.get('username')
        userId = str(user.get('id'))
        response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                                "?userId=" + userId)
        data_response = json.loads(response.text)
        tasks = []
        for task in data_response:
            tasks.append(task)
        json_dict[userId] = []
        for task in tasks:
            task_dict = {"task": task.get('title'),
                         'completed': task.get('completed'),
                         'username': username}
            json_dict.get(userId).append(task_dict)
    with open("todo_all_employees.json", "w") as f:
        json.dump(json_dict, f)
