# 1
# 定义一个模#块`tools.py`, 定义函数实现对两个数据进行加法操作的函# 数`add_2_num`，
# 并返回相加之和的结果；再定义一个实现对三个数据进行加法操作的函# 数`add_3_num`，
# 并返回相加之和的结果；最后新定义一个 `代码文件`,
# 对这两个函数进行测试调用，并在控制台打印结果。
#
import random

import tools
# tools.add_3_num(1,2,3)
# tools.add_2_num(2,3)
# print(tools.add_3_num(1,2,3),tools.add_2_num(2,3))


# ### 题目 2


# .提示用户在控制台输入个人信息，包括：姓名、年龄、住址，把用户信息保存到一个字典中；
# 封装一个打印用户信息的函数`print_user_info`，在函数中遍历字典中的键和值，并打印。
#
# name = input('name: ')
# age = input('age: ')
# address = input("address: ")
# dict1 = {'name': name, 'age': age, 'address': address}


def print_user_info(dict):
    for a, b in dict.items(): # 遍历键和值
        print(f'{a}: {b}')


# print_user_info(dict1)


# ### 题目 3
# 3. 封装一个获取列表数据中最大值的函数my_max()
# 1. 定义一个函数, make_data, 在列表中随机创建 10 个数字
# 2. 定义一个函数, my_max, 返回列表中最大的数字.

list1 = []


def make_data():
    for i in range(10):
        list1.append(random.randint(1,10))
    print(list1)
    return list1


# make_data()


# def get_max_list():  # 排序获取最大值
#     list2 = make_data()
#     list2.sort()
#     print(list2[-1])

def get_max_list():
    list2 = make_data()
    max = 0
    for i in list2: #取最大值
        if i > max:
            max = i
    return max


print(get_max_list())

# ### 题目 4
# .定义一个函数 sum_test 接收一个参数 n ，在函数中计算 1 + 2 + 3 + ... + n 的值，并打印结果


# def sum_test(n):
#     sum = ((n + 1)*n)/2
#     return sum
#
#
# print(sum_test(-1))


def sum_test(n):
    sum = int(0)
    for i in range(1,n+1):
        sum += i
    return sum
        # print(sum)


# print(sum_test(100))


# ### 题目 5
# 有如下列表:
# my_list = [{'id': 1 ,'money': 10}, {'id': 2, 'money': 20}, {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]
# 要求: 定义一个函数 func, 功能如下
# 1. 如果字典中 ID 的值为奇数 ,则对 money 的值加 20
# 2. 如果字典中 ID 的值为偶数, 则对 money 的值加 10
# 3. 打印输出列表 ,查看最终的结果
# ```
my_list = [{'id': 1 ,'money': 10}, {'id': 2, 'money': 20}, {'id': 3, 'money': 30}, {'id': 4, 'money': 40}]


def func(list):
    for i in list:  #遍历列表
        if i.get('id') % 2 == 0: # i 是字典
            i['money'] = i.get('money') + 10
        else:
            i['money'] = i.get('money') + 20
    return list


# print(my_list.pop()) pop 返回的删除的对象

# print(func(my_list))



