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


login()   # 调用login()函数