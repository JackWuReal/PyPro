"""
集合  即不含重复数据的列表
列表去重 可将List转化为Set 再转化为List
"""
# list1 = [1,2,3,2,3,6,8,8,9]
# list1 = list(set(list1))
# print(list1)
#
# """
# in 是 Python 中的关键字.
# 数据 in 容器 可以⽤来判断 容器中是否包含这个数据, 如果
# 包含返回 True,如果不包含返回 False
# 对于字典来说,判断的是 字典中是否包含这个键
# """
# print(1 in list1)


"""
函数的定义
1, 处在 def 缩进中的代码 都属于这个函数
2, 函数名要满⾜标识符的规则, ⻅名知意
3, def 这⾏代码的最后需要⼀个 冒号
4, 函数定义不会执⾏函数中的代码,想要执⾏,需要调⽤

"""


def hello_world():
    print("hello")
    print("world")
    print("hello world")


# hello_world()

"""
参数: 在函数定义的时候,在括号中写⼊变量,这个变量就称为是
函数的参数. 形式参数(形参)
在函数调⽤的时候,可以给定义时候的形参传递具体的数据值,供
其使⽤. 实际参数(实参)
即: 在函数调⽤的时候,会将函数的实参值传递给形参.
好处: 可以让函数更加的通⽤, 函数中的数据值不是固定的,是调
⽤的时候,你传递的.
使⽤场景: 判断 函数中 数据值是不是固定不变的, 如果是变化
的,就可以使⽤参数传递
注意点: ⽬前书写的函数, 如果存在形参,必须传递相同个数的实
参
"""


def sun_2_num(a, b):  # a, b 形参
    c = a + b
    print(f'a + b ={c}')


# sun_2_num(10, 20) # 10, 20 实参 10 给 a, 20 给 b
# sun_2_num(1, 2)
# sun_2_num(20, 39)

"""
函数的嵌套
在一个函数内部再调用某些函数

1, 代码从上到下执⾏的
2, 函数定义不会执⾏函数中的代码
3, 函数调⽤会进⼊函数中执⾏函数中的代码
4, 函数中的代码执⾏结束,会回到调⽤的地⽅继续向下执⾏
"""
# sun_2_num(1)
# sun_2_num(1,3,9)

"""
设计⼀个函数⽤于获取两个数中的较⼤数，数据来自于函数的参数
"""


def get_max(a, b):
    if a >= b:
        return a
    else:
        return b


print(get_max(100,101))