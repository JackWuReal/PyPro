import requests
import pytest

data = {
    'shouji': '13456755448',
    'appkey': '0c818521d38759e1'
}

json_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

def test_post_data():
    r = requests.post("https://jsonplaceholder.typicode.com/posts", json=json_data)
    print(r.status_code)
    print(r.json())
    # 三种请求参数类型 data json params
    r = requests.post("http://sellshop.5istudy.online/sell/shouji/query",data=data)
    print(r.status_code)
    print(r.json())



if __name__ == '__main__':
    pytest.main()