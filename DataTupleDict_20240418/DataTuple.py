"""
元组
可以存储任意类型的数据
类似于数组  区别为元组中的数据无法更改  都可以存储任意类型的数据

元组中的数据 可以查询 切片 index count 支持下标和切片
"""
# tuple1 = tuple()
# print(type(tuple1), tuple1) # <class 'tuple'> ()
# 1.2 类型转换 , 将列表(其他可迭代类型)转换为元组
# tuple2 = tuple([1, 2, 3])
# print(tuple2)
# # 2. 直接使用 () 定义
# # 2.1 定义空元组
# tuple3 = ()
# # 2.2 非空元组
# tuple4 = (1, 2, 'hello', 3.14, True)
# print(tuple4)
# print(tuple4[2]) # hello
# # 2.3 定义只有一个数据的元组, 数据后必须有一个逗号
# tuple5 = (10,)
# print(tuple5)

"""
应用交换两个变量的值

定义元组时()可以不写
"""
a = 90
b = 20
print(a, b)
c = a, b
d = b, a
a, b = b, a
print(a, b)
# print(type(a), type(b))
# print(type(c),d)