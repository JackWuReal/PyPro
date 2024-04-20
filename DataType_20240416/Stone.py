"""
石头剪刀布
控制台出拳(⽯头1/剪⼑2/布3) player = input()
2. 电脑出拳 computer = 电脑的结果
3. 判断胜负
3.1 玩家胜利
3.1.1 玩家出⽯头, 电脑出剪⼑ player == 1 and computer
== 2
or
3.1.2 玩家出剪⼑, 电脑出 布 player == 2 and computer
== 3
or
3.1.3 玩家出布, 电脑出 ⽯头 player == 3 and computer
== 1
3.2 平局 玩家和电脑出的内容⼀样, player == cpmputer
3.3 电脑胜利 else
"""
# import random
#
# player = int(input('请先出'))
# num = random.randint(1,3)
# print(num)
# if (player == 1 and num == 2) or (player == 2 and num == 3) or (player == 3 and num == 1):
#     print('玩家赢')
# elif(player == num ):
#     print('平局')
# else:
#     print('电脑赢')

# 循环让指定代码重复执行
"""
while循环
"""
# import random
#
# while True:
#     player = int(input('请出拳 ⽯头1/剪⼑2/布3/退出0'))
#     num = random.randint(1,3)
#     if player == 0:
#         print("欢迎下次光临")
#     break  # continue # 结束本次循环,继续下⼀次循环
#             # break 结束循环
#     print(num)
# if (player == 1 and num == 2) or (player == 2 and num == 3) or (player == 3 and num == 1):
#     print('玩家赢')
# elif(player == num ):
#     print('平局')
# else:
#     print('电脑赢')
"""
求1-100的累加和
1 2 3 4 5 6 7 8 9
...100

"""
n = 1
num = 0
# while n <= 100:
#     num = num +n
#     n+=1
# if n == 101:
#     print (f"1-100的累加和为{num}")

"""
for 循环 也称为是 for 遍历, 也可以做指定次数的循环
遍历: 是从容器中将数据逐个取出的过程.
容器: 字符串/列表/元组/字典
"""
# for n in range(1,101):  #for 遍历 指定循环次数[) 左闭右开区间
#     num +=n
#     print(f"1-100的累加和为{num}")

#控制台输入天数  转换为秒数
Day = int(input('请输入天数：'))  #只能输入整数
Second = Day*24*60*60
print(f'{Day}天等于{Second}秒')

