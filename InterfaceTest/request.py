"""
resp = requests.请求方法(url='URL地址', params={k:v}, headers={k:v},
data={k:v}, json={k:v}, cookies='cookie数据'(如：令牌))
请求方法：
get请求 - get()
post请求 - post()
put请求 - put()
delete请求 - delete()
url: 待请求的url - string类型
params：查询参数 - 字典
headers：请求头 - 字典
data：表单格式的 请求体 - 字典
json：json格式的 请求体 - 字典
cookies：cookie数据 - string类型
resp：响应结果

"""

import requests
import json
# 发送 get 请求，指定 url，获取 响应结果
# 方法1：
# resp = requests.get(url="http://tpshop-test.itheima.net/Home/Goods/search.html?q=iPhone")


# 方法2：
# 带查询参数get请求 使用Requests库请求tpshop商城搜索商品接口查询iphone

# resp = requests.get(url="http://192.168.42.128/Home/Goods/search.html",params={"q": "iPhone"})
# # 查询响应结果
# print(resp.text)

"""
【带 表单数据 的post请求】使用Requests库，完成 tpshop商城 登录接口调用。返回 ”验证码错误“ 即可。
"""

# response = requests.post(url="http://192.168.42.128/Home/user/login.html?m=home&c=User&a=do_login&t=0.7094195931397276",
#                          #缺失参数 '&a=do'导致 异常requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#                          headers={"Content-Type": "application/x-www-form-urlencoded"},
#                          data={"username": "130125678", "password": "124567", "verify_code": "898"})
#
# # 打印响应结果 - 文本
# print(response.text)
# # 打印响应结果 - json
# print(response.json())

"""
案例3
带json数据的的post请求  使用Requests库完成成功登陆返回令牌数据
"""
response = requests.post(url="http://192.168.42.128/Home/user/login.html",
                        # headers={"Content-Type": "application/json"},
                        json={"mobile": "13800000002", "password": "123456"})

# 打印返回结果
print(response.json())

"""
案例4 【发送 put、delete请求】使用Requests库发送 ihrm系统 修改员工信息、删除员工信息 请求。

修改put
"""
resp = requests.put(url="http://ihrm-test.itheima.net/api/sys/user/1467780995754229760",
                    headers={"Authorization": "Bearer 4c51c601-c3f7-4d1a-a738-7848f2439f45"},
                    json={"username": "齐天大圣"})
print(resp.json())

"""
删除delete
"""
resp = requests.delete(url="http://ihrm-test.itheima.net/api/sys/user/1467780995754229760",
                        headers={"Authorization": "Bearer 4c51c601-c3f7-4d1a-a738-7848f2439f45"})
print(resp.json())



