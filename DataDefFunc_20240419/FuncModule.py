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

def sun_2_num(a, b): # a, b 形参
     c = a + b
     # print(f'a + b ={c}')


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

:return 后面的代码都不会再执行了
"""


def get_max(a,b):
    if a >= b:
        return a
    else:
        return b


# print(get_max(100,101))

"""
. 定义名为 input_username 的函数, 获取⽤户输⼊的⽤户名
2. 定义名为 input_password 的函数, 获取⽤户输⼊的密码
3. 定义名为 login 的函数, 判断获取的⽤户名和密码信息
4. 要求当获取的⽤户名为:admin 并且密码为: 123456 时, 输
出“登录成功!”，否则提示“⽤户名或 密码错误!”
"""


def input_username():
    name = input('Enter your username: ')
    return name


def input_password():
    password = input('Enter your password: ')
    return password


def login():
    if input_username() == 'admin' and input_password() == '123456':
        print('Login successful!')
    else:
        print('Login failed')


# login()   # 调用login()函数

"""
模块和包
as 关键字可以给模块或功能起名
模块导入
方法一
import 模块名    #模块名为代码文件名

使用其功能 模块名.功能名    功能可以是变量，函数，类
#多用于导入系统中常用的模块和功能
"""

# import random
#
# num = random.randint(1, 100)
# print(num)

"""
方式二 导入指定的功能

from 模块名 import 功能名
功能名()    #使用

方式二 多用与导入自己书写的或第三方模块
"""

# from random import randint
# print(randint(1,19))

"""
定义⼀个模块 tools.py , 在模块中定义⼀个函数
sum_2_num(), 可以对两个数字求和
2. 新定义⼀个代码⽂件, 调⽤ tools.py ⽂件中的
sum_2_num() 函数, 对 10 和 20 求和
"""
# from tools import sum_2_num
# print(sum_2_num(10,20))

from DataDefFunc_20240419.PythonPackage import tools
sum =  tools.sum_2_num(10, 20)
print(sum)

"""
_name_  变量
导入模块的时候会执行模块中的代码
如果在导入的模块中不想执行某些代码可以使用 _name_ 来解决

3, __name__ 变量,是 Python 解释器内置的变量(变量的值是
⾃动维护的), 每个代码⽂件中,都有这个变量
3.1 在模块中 直接右键运⾏代码⽂件, __name__ 变量的值是
'__main__'
3.2 如果是被导⼊运⾏代码⽂件, __name__ 变量的值 是 模块
名(⽂件名)

if __name__ == '__main__':
 # 在这个 if 的缩进中书写的代码,导⼊的时候不会被执⾏
"""

"""
模块的导入顺序
1, 在导⼊模块的时候, 会先从代码所在的⽬录进⾏导⼊
2, 如果没有找到,回去 Python 系统的⽬录查找导⼊
3, 如果没有找到, 报错
--------
注意点: 我们⾃⼰定义的代码⽂件名字 不要和你导⼊的系统的模
块⽂件名⼀样
"""
# import app