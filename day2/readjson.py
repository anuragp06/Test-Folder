import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(f"Name:{data['name']}, age:  {data['age']}")