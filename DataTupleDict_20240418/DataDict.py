"""
字典的定义
使用{} 表示
由多个 key value 键值对组成
多个键值对用 ,隔开
键 ：主要为字符串类型也可以是数字
字典中的键无法重复
字典无下标
"""
dirct1 = dict()   #类实例化
print(type(dirct1))
dirct2 = {'a': 1, 'b': 2, 'c': 3}
# dirct2 = dict()
print(dirct2)

# 添加和修改
# dirct2['可乐'] = 99
# dirct2['b'] = 80
# print(dirct2)

# 删除
# dirct2.pop('c')
# print(dirct2)
# 查询
# print(dirct2['c'])  键不存在会报错
# print(dirct2.get('c'))

# 遍历字典的键
# print(dirct2.keys())
# 方法一
# for i in dirct2:
#     print(i)
# 方法二
# for i in dirct2.keys():
#     print(i)

# 遍历字典的值
# for i in dirct2.values():
#     print(i)

# 遍历字典的键和值  字典.item()
my_dict = {'name': '小明', 'age': 18, 'sex': '男'}
for m,n in my_dict.items():
    print(m, n)
print("***"*30)
for m in my_dict.keys():
    print(m)
print("***"*30)
for m in my_dict.values():
    print(m)

