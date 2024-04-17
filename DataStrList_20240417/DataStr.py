"""
数据序列
1.字符串
2.列表
3.元组
4.字典
"""

# 字符串的定义 'str'  "str2" """ str3""" '''str4'''

# 特殊字符串的处理  有时需要处理一些特殊字符串 需要用到转义字符 \  \t \' \"
# 如果字符串定定义的时候用的单引号那么单引号需要转义
# 如果字符串定定义的时候用的双引号那么引号需要转义
# str = "i\"m a string"
# str1 = 'i\'m a string'

# str2 = r'i\'m a string'  字符串前面加r表示不需要转义，原生字符串
# str3 = 'i\\\'m a string'
# print(str)
# print(str1)
# print(str3)

# 下标索引  是数据在容器（字符串，列表，元组）中的位置编号
# 一般为正数下标
# str = "abcdefg"
# print(str[0])
# print(str[-1])
# print(str[-7])

# 切片
# my_str = 'abcdefg'
# # 需求1 : 打印字符串中 abc 字符 start 0, end 3, step 1
# print(my_str[0:3:1])
# # # 1.1 如果步长是 1, 可以省略不写
# print(my_str[:3])
# # # 1.2 如果 start 开始位置的下标为 0, 可以不写,但是冒号不能少
# # print(my_str[:3]) # abc
# # # 需求 2: 打印字符串中的 efg , start 4, end 7, step 1
# print(my_str[4:7])
# # # 2.1 如果取到最后一个字符, end 可以不写,但是冒号不能少
# print(my_str[4:])
# # # 需求 3: 打印字符串中的 aceg , start 0, end 7(最后), 步长 2
# print(my_str[::2])
# # # 练习: cf
# print(my_str[2::3])
# # # 特殊情况, 步长为 -1, 反转(逆序) 字符串
# print(my_str[::-1])

# # 字符串查找 字符串.find(被查找字符)   存在返回下标，不存在返回-1
# print(str.find('b'))
# str = "测试开发测试工程师"
# print(str.find('开发'))
# print(str.find('测试'))
# print(str.find('工具'))

# 字符串的替换 replace()  原字符串不会改变 ，将原字符串替换为新字符串
# print(str.replace("测试","开测",1))
# # count 不写表示全部替换
# print(str)

# 字符串拆分 split()
str1 = 'hello Python\tand itcast and\nitheima'
# list1 = str1.split() 默认按照 空格 \t \n分隔
# print(list1)
# list2 = str1.split(' ')
# print(list2)
# list3 = str1.split('and')
# print(list3)

# 字符串的连接 join
# list1= ["9999","hello","world","+","."]    列表必须全为字符串格式
# str2 = '    '.join(list1)
# print(str2)
# str3 = '_+_'.join(list1)
# print(str3)