import json

data = {
    "name":"bob",
    "age":22,
    "subjects":["english","history"]

}

with open('data.json','w') as file:
    json.dump(data,file,indent=4)