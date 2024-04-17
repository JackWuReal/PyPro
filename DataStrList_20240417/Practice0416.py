#### 题干

# 用户输入年龄，如果年龄超过65岁，输出："可以退休了"， 否则，输出："小伙子，加油干！"

####
# age = int(input('Enter your age: '))
# if age >= 65:
#     print('可以退休了.')
# else:
#     print('小伙子，加油干！')

# 用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，并提示：您的年龄是xx: 青少年/青年/中年/老年。
#
# 年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。
# if age < 18:
#     print(f'您的年龄是{age} You are 青少年')
# elif age >= 18 and age < 36:
#     print(f'您的年龄是{age} You are 青年')
# elif age >=36 and age < 60:
#     print(f'您的年龄是{age} You are 中年')
# else:
#     print(f'您的年龄是{age} You are 老年')

"""
制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：

登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。

提示：系统先验证验证码是否正确，正确后再验证用户名和密码。 
    
"""
# n = int()
# while True:
#     if n == int(666):
#         break
#     code = input('Enter your code: ')
#     while code == '1':
#             name = input('Enter your name: ')
#             psw = input('Enter your password: ')
#             if name == '1' and psw == '1':
#                 print('登录成功')
#                 n = int(666)
#                 break
#
#             else:
#                 print('登录失败账号或密码不正确')
#                 continue
#     else:
#         print('验证码不正确，请重新输入')

"""
闰年判断程序(闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)

输入一个有效的年份，判断是不是闰年

如果是闰年，则打印“xxxx年是闰年”；否则打印“xxxx年不是闰年”

如输入"2018"，将打印“2018年不是闰年”

"""
# year = int(input('请输入一个有效年份：'))
# if year % 4 ==0 and year % 100 !=0 or year % 400 == 0:
#     print(f'{year}年是闰年')
# else:
#     print(f'{year}年不是闰年')

"""
1. 书写代码求 `1-100之间所有数字的累加和`

2. 书写代码求 `1-100 之间偶数的累加和`

"""
m = int(0)
i = int(1)
#for i in range(1,101):
#     m+=i
#print(f'累加和为: {m}')


#while i < 101:
#     m+= i
#     i+=1
#     print(m)


#while i <= 100 :
#     if i%2 == 0:
#         m+=i
#     i+=1
# print(f'1-100之间的偶数和为{m}')

"""
猜数字游戏：

1. 电脑产生一个（1-100）的随机数，用户进行猜测(通过 input 输入)，直到猜中为止。
2. 如果猜对了，输出：恭喜你猜对了，数字是 xx。
3. 如果猜的数字比随机数大，输出：猜测的数字太大了，继续加油
4. 如果猜测的数字比随机数小，输出：猜测的数字有点小，再来一次

"""

# import random
# ReNum=random.randint(1,100)
# while True:
#     GuNum = int(input('请输入一个猜测数字1-100'))
#     if GuNum>ReNum:
#         print('猜测的数字太大了，继续加油')
#         # continue
#     elif GuNum<ReNum:
#         print('猜测的数字有点小，再来一次')
#         # continue
#     else:
#         print(f'恭喜你猜对了，数字是{GuNum}')
#         break

"""
设计简易计算器，可以进行基本的加减乘除运算, 参考如下

```python
请输出第一个数字: 
请输入第二个数字: 
请输入要进行的操作(+ - * /): 
计算的结果为:  
举例如下: 
请输出第一个数字: 10
请输入第二个数字: 20
请输入要进行的操作(+ - * /): + 
计算的结果为: 10 + 20 = 30 
```
"""
# num1 = int(input("请输入第1个数字:"))
# num2 = int(input("请输入第2个数字:"))
# step = input('请输入要进行的操作(+ - * /):')
# if step =='+':
#     print(f'计算的结果为{num1}+{num2} = {num1+num2}')
# elif step =='-':
#     print(f'计算的结果为{num1}-{num2} = {num1-num2}')
# elif step =='*':
#     print(f'计算的结果为{num1}*{num2} = {num1*num2}')
# else:
#     print(f'计算的结果为{num1}*{num2} = {num1/num2}')


