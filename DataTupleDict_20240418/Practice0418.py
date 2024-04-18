"""
# 定义一个字符串 str1, 字符串的内容为 "hello world and itcast and itheima and Python"

# 在字符串str1中查找 字符串 and 的下标

# 在字符串str1中查找字符串 'good'的下标
# 将字符串str1中的 and 替换为 or
# 将字符串 str1 按照 空白字符进行切割,保存到变量 list1 中
# 使用 _*_ 将 list1中的字符串进行连接
# 使用 逗号 将 list1中的字符串进行连接
"""

import random

str1 = "hello world and itcast and itheima and Python"
# print(str1)
# print(str1.index('and'))
# print(str1.index('good'))
# print(str1.replace('and', 'or'))

# list1 = list(str1.split(' '))
# print(list1)
# "_*_".join(list1)
# print("_*_".join(list1))
# ','.join(list1)
# print(','.join(list1))

"""
2.练习对列表的增删改查统计的操作，具体操作如下：
1)声明一个列表，包含的数据有：["hello", "python", "itcast", "hello"]
2)在列表中追加一个数据："heima"
3)删除列表中的第二个数据
4)删除列表中的数据："heima"
5)将列表中的第二个数据改为："chuanzhi"
6)在控制台打印列表中的第一个元素
7)统计列表中"hello"字符串出现的次数
8)在控制台打印列表的长度
9)循环遍历列表中的所有数据
"""
# list2 = ["hello", "python", "itcast", "hello"]
# list2.append("Wgk")
# print(list2)
# list2.pop(1)
# print(list2)
# list2.pop()
# print(list2)
# list2[1] = "chuanzhi"

# print(list2)
# print(list2[0])
# print(list2.count("hello"))
# print(len(list2))
# for i in list2:
#     print(i)

"""
有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表
"""
# list1 = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
# list2 = list()
# for i in list1:
#     if i.endswith('s') or i.endswith('e'):
#         list2.append(i)
# print(list2)

"""
1. 使用 input 输入 5 个学生的名字存入列表
2. 随机的获取一个学生的名字并打印
"""
# list3 = list()
# for i in range(1,5):
#     list3.append(input('请输入学生的名字'))
# print((list3[random.randint(0,4)]))

"""
已有列表nums = [10, 20, 30, 40, 50], 将每一个数字在原来的基础上加10，打印列表
"""
nums = [10, 20, 30, 40, 50]
for num in range(0,5):
    nums[num] += 10
print(nums)

"""
### 题目 6 
需求:
1. 参考TPshop项目的登录功能(登录时需要输入用户名、密码、验证码)，至少设计3条测试用例
2. 要求1:定义变量保存测试数据(包括不同测试数据对应的测试结果)
3. 要求2:至少写出3种以上不同的数据格式
4. 要求3:遍历测试数据并打印到控制台，数据格式“用户名:xxx 密码:xxx 验证码:xxx 期望结 果:xxx”
                    
一组测试数据, {'desc': 用例标题, 'username': 用户名, 'password': 密码, 'verify_code': 验证码, 'expect': 预期结果}

[{}, {}, {}]
-----------
扩展:
    将原列表中中数据进行提取 保存为如下格式
[('13888888888', '123456', '8888', '登录成功'), (), (), () ]  # 元组中不要 desc
"""

"""
数据类型
列表  字典
"""
dict1 = {'desc': '用例标题', 'username': '用户名', 'password': '密码', 'verify_code': '验证码', 'expect': '预期结果'}
list1 = ['desc','用例标题', 'username','用户名', 'password' ,'密码', 'verify_code' ,'验证码', 'expect' ,'预期结果']
Tuple1 = 'desc','用例标题', 'username','用户名', 'password' ,'密码', 'verify_code' ,'验证码', 'expect' ,'预期结果'
# print(dict1)
print(list1)
# print(Tuple1)
list2 = list()

data_list = [
    {'desc': '用户名密码验证码 OK',
     'username': '13888888888',
     'password': '123456',
     'verify_code': '8888',
     'expect': "登录成功"
     },
    {'desc': '用户名不存在',
     'username': '',
     'password': '123456',
     'verify_code': '8888',
     'expect': "用户名不存在"
     },
    {'desc': '密码错误',
     'username': '13888888888',
     'password': '123123',
     'verify_code': '8888',
     'expect': "密码错误"
     }
]

new_list = []
for data in data_list:  # data  字典
    print(f"用户名:{data.get('username')}, 密码: {data.get('password')}, "
          f"验证码: {data.get('verify_code')}, 期望结果:{data.get('expect')}")

    t = data.get('username'), data.get('password'), data.get('verify_code'), data.get('expect')  #元组
    new_list.append(t)
print(new_list)



