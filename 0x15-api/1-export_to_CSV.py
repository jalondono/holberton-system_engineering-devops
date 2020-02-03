#!/usr/bin/python3
""" Export data in the CSV format.. """
import json
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            sys.argv[1])
    dicti = json.loads(response.text)
    username = dicti.get('username')
    response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + sys.argv[1])
    data_json = json.loads(response.text)
    tasks = []
    for task in data_json:
        tasks.append(task)
    with open(sys.argv[1] + ".csv", "w") as f:
        for task in tasks:
            data = ['"' + sys.argv[1] + '"', '"' + username + '"', '"' +
                    str(task.get('completed')) + '"', '"' + task.get('title') +
                    '"']
            f.write(",".join(data) + '\n')
