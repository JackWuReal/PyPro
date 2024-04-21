"""
函数进阶

函数返回多个数据值
return 关键字的两个作用
1.返回数据值
2.结束函数的运行

函数中如果想要返回多个数据值，一般是组成元组进行返回

"""


def calc(a,b):
    return a+b, a-b


# if __name__ == '__main__':
#     print(calc(5,3))

"""
函数传参的方式

如何将实参的值传给形参

位置传参
在函数调用的时候按照 形参的顺序将实参传递给形参

关键字传参
在函数调用的时候，指定将实参传递给哪个形参

混合使用
1. 位置参数必须写在关键字参数的前边, 关键字参数必须放在位置参数的后边
2. 同一个形参只能接收一个实参值(不能即使用位置传参和关键字传参给同一个形参传参)
"""


# def show_info(name, age):
#     print(f"name:{name}, age: {age}")
#
#
# # 位置传参
#     show_info('小明', 18)
# # 关键字传参
#     show_info(age=18, name='张三')
# # 混合使用
#     show_info('李四', age=17)

""""
缺省参数
在函数定义的时候, 给形参一个默认的数据值,这个参数就是缺省参数(默认参数)

在函数调用的时候, 缺省参数可以不用传递实参值.
1. 如果不传实参值, 使用的就是默认值
2. 如果传递实参值, 使用的就是传递的实参值

缺省参数必须写在 普通参数的后边
"""

"""
定义 show_info 参数 姓名,年龄, 性别, 将年龄设置为默认参数 18, 性别设置为默认 保密
"""


def show_info(name, age=18, sex='保密'):
    print(name, age, sex)



# if __name__ == '__main__':
#
#     # 调用
#     show_info('张三', 18, '男')
#
#     # 李四
#     show_info('李四')
#     # 王五 19
#     show_info('王五', 19)
#     # 赵六 男
#     show_info('赵六', sex='男')

"""
多值参数

1.在函数定义的时候,不确定在调用的时候,实参有多少个,此时可以使用 多值参数
2, 在普通的参数前边加上一个 *, 这个参数就变为 多值参数
3, 这个参数可以接收任意多个位置传参的数据, 类型 元组
4, 这个形参一般写作 args(arguments), 即 *args

参数顺序
def 函数名(普通, *args, 缺省):
    pass
"""


def func(*args):
    print(args)

# if __name__ == '__main__':
#     func() # ()
#     func(1, 2, 3) # (1, 2, 3)


"""
定义一个函数,my_sum,作用,可以对任意多个数字进行求和计算.

"""


def my_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# if __name__ == '__main__':
#     print(my_sum(1,2,3,4))
#     my_tuple = (1, 2, 3, 4, 5)
#     # 需求对 元组中的所有数据使用 my_sum 进行求和
#     # 想要把列表(元组) 中的数据作为位置参数进行传递,
#     # 只需要在列表(元组)前边加上一个 * ,进行拆包即可
#     print(my_sum(*my_tuple)) # 15

"""
匿名函数
# 1, 定义匿名函数, 参数为两个整数数字, 求两个数字的乘积
lambda a, b: a * b
# 2, 定义匿名函数, 参数为一个字典, 返回字典中 键为 age 的值
lambda x: x.get('age')
lambda x: x['age']
"""

func = lambda a,b:a*b

func1 = lambda dict:dict.get('age')
func2 = lambda dict:dict['age']

# if __name__ == '__main__':
#     print(func(9, 9))
#     print(func1({'name':'javk','age':19}))
#     print(func2({'name':'jack','age':18}))

user_list = [
{'name': '张三', 'age': 22, 'title': '测试工程师'},
{'name': '李四', 'age': 24, 'title': '开发工程师'},
{'name': '王五', 'age': 21, 'title': '测试工程师'}
]

"""
# user_list.sort() # 只能对数字,字符串排序
# 根据字典的 age 键 排序
# 想要对列表中的字典排序,需要 key 形参来指定根据字典中的什么键排序
# key 这个参数需要传递一个函数,使用匿名函数
# 列表.sort(key=lambda x: x['键'])
"""
user_list.sort(key=lambda x : x['age'])
print(user_list)