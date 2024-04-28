import json

def read_json_data():
    with open('json_data.json', encoding='UTF-8') as f:
        json_data = json.load(f)
        list_data = []
        for item in json_data:
            tmp = tuple(item.values())
            list_data.append(tmp)
        return list_data
