import requests


# 发送 post 请求，指定 url，获取 响应结果登录IPD设备
# 请求体为xml类型数据

with open('data.xml', 'r') as xml_file:
    xml_data = xml_file.read()
resp = requests.post(url="http://192.168.19.49/tdkcgi",data=xml_data)
print(resp.text)
print(resp.status_code)
print(resp.url)
print(resp.headers)
print(type(resp.headers))
