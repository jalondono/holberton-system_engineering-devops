#!/usr/bin/python3
""" Export data in the CSV format.. """
import json
import requests
from sys import argv

"""{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt",
 "completed": false, "username": "Antonette"}]}"""
if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            argv[1])
    dicti = json.loads(response.text)
    username = dicti.get('username')
    response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + argv[1])
    data_json = json.loads(response.text)
    tasks = []
    data_dict = {}
    json_dict = {}
    for task in data_json:
        tasks.append({"task": task.get('title'), "completed": task.get('completed'), "username": username})
    json_dict[argv[1]] = tasks
    with open(argv[1] + ".json", "w") as f:
        json.dump(json_dict, f)
