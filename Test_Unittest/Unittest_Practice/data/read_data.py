import json


def read_data_method():
    with open('login_data.json',encoding='gbk',errors='ignore') as f:
        data = json.load(f)
        list_data = []
        for i in data:
            password = i['password']
            username = i['username']
            desc = i['desc']
            expect = i['expect']
            list_data.append([desc,username,password,expect])
        return list_data