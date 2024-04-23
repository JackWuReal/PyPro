
"""
练习， 将测试数据定义为json文件

[
[1, 1, 2],
[1, 2, 3],
[2, 3, 5],
[4, 5, 9],
[10, 20, 30]
]

读取json文件
"""
import json  #导入json 包

def build_add_data():
    with open('add_data.json') as f:
        data = json.load(f) # [[], [], []] ---> [(), ()]  json.load(f) 得到的是列表或者字典

    return data

def build_add_data1():
    with open('add_data1.json') as f:
        data_list =json.load(f)
        new_list = []
        for data in data_list:
            a = data['a']
            b = data['b']
            exp = data['expect']
            new_list.append([a, b, exp])

        return new_list

def build_add_data2():
    with open('add_data1.json') as f:
        data_list =  json.load(f)
        new_list = []
        for data in data_list: # data是字典
            new_list.append(tuple(data.values()))  # 提取字典中的值

        return new_list