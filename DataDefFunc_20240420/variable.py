"""
1, 定义变量的时候, 变量和数据 都会在内存开辟空间
2, 变量所对应的内存空间中存储的是 数据所在内存的地址 (平时理解为 将数据存储到变量中即可)
3. 变量中保存数据的地址,就称为是引用
4, Python 中所有数据的传递,传递的都是引用(即地址)
5, 赋值运算符(=), 会改变变量的引用, 即只有 = 可以修改变量的引用
6, 可以使用 id(变量) 函数,查看变量的引用
"""
a = 9
b = a
# print(id(a))   # 返回的是变量a 的引用地址
# print(id(b))

list1 = [1, 3, 5, 7, 9, 10]

list2 = list1
# print(list2, id(list2))
# print(list1, id(list1))
list1[1] = 9

# print(list1, id(list1))
# print(list2, id(list2))

"""
可变类型和不可变类型  

根据内存中数据是否允许修改，将数据类型分为可变类型和不可变类型
简单理解：不使用等号能不能修改路径
可变类型：可以修改
列表
字典
集合

不可变数据类型：不允许修改
数字类型
字符串
元组
"""

"""
根据变量定义的位置将变量分为局部变量和全局变量

1.函数内部定义的为局部变量
2.特点
- 2.1 局部变量,只能在当前函数内部使用
- 2.2 可以在不同函数内定义名字相同的局部变量
生命周期
3.1 在函数执行(调用)的时候被创建
3.2 函数执行结束被销毁(删除)
4.形参可以认为是局部变量
5.如果想要在函数外部使用局部变量的值, 使用 return 返回
"""


def func1():
    num = 10  # 局部变量
    print(num)


def func2():
    num = 20
    print(num)


"""
# 当该模块被其他模块导入时默认不执行该代码，
因为其他模块引用该模块时的__name__ != '__main__'
而是 模块名
"""

# if __name__ == '__main__':   # 该代码常用来执行模块测试，不影响其他模块代码执行
#     print(__name__)
#     func2()
#     func1()
#     func2()

"""
全局变量
1, 在函数外部定义的变量
2, 特点
- 2.1 全局变量 可以在任意函数内访问(读取)
- 2.2 想要在函数内部修改全局变量的引用,需要使用 global 关键字声明(使用 global 关键字可以声明为全局变
量)
- 2.3 如果在函数内部出现和全局变量名字相同的局部变量,在函数内部使用的是局部变量
3, 生命周期
- 代码执行的时候 创建, 执行结束销毁

"""
# 定义全局变量
# g_num = 10
#
#
# def func_1():
#     print(g_num)
#
#
# def func_2():
#     g_num = 20
#     print(g_num)
#
#
# def func_3():
#     global g_num
#     g_num = 30
#     print(g_num)


# if __name__ == '__main__':
#     print(g_num) # 10
#     func_1() # 10
#     func_2() # 20
#     func_1() # 10
#     print(g_num) # 10
#     func_3() # 30 修改了全局变量, 将全局变量的值改为30 了
#     func_1() # 30
#     g_num = 100
#     func_1() # 100 修改全局变量的值
#     func_2() # 20 局部变量
#     func_3() # 30
#     func_1() # 30


def func1():
    list1.append(10)


def func2():
    list1 = [1, 1]  # 定义局部变量, 不影响全局变量
    list1.append(0)


def func3():
    global list1 # 全局变量
    list1.pop() # 删除最后一个数据


def func_5():
    list1.pop() # 用的全局变量,没有改引用


def func4():
    global list1 # 全局变量
    list1 = [1]


if __name__ == '__main__':
    list1 = [1, 2,3]
    func1()
    print(list1)
    func2()
    print(list1)
    func3()
    print(list1)
    func_5()
    print(list1)
    func4()
    print(list1)

