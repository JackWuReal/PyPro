import json
from Test_Unittest_20240423.Unittest_Practice.app import Base_Dir


def read_data_method():
    with open(Base_Dir + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        list_data = []
        for i in data:
            # password = i['password']
            # username = i['username']
            # desc = i['desc']
            # expect = i['expect']
            # list_data.append([desc,username,password,expect])
            list_data.append(tuple(i.values()))  # 简化写法将数组中的每个字典中的values
            # 转换为元组后append到数组中
        return list_data
