"""
流程控制:
判断(如果...否则 ....): if(如果) elif(如果) else(否则)
循环(重复做某些事): while(直到) for in(在) break(终
⽌) continue(继续)
pass 空语句,可以占位
"""
# if 语句
"""
需求:
1. 定义⼀个整数变量记录输⼊的年龄
2. 判断是否满 18 岁 (>=)
3. 如果满 18 岁，允许进⽹吧嗨⽪
"""
# a = int(input('请输入你的年龄:'))
# if a >= 18:
#     print('允许进去')
# else:
#     print('回家写作业')
"""
获取⽤户输⼊的⽤户名信息
2. 如果⽤户名信息是 admin, 就在控制台输出 "欢迎admin
登录
if else  存在冒号就需要回车
"""
# b = input("请输入用户名")
# if b == 'admin':print('欢迎admin')
# else: print('用户名错误')
"""
if 与逻辑运算符结合  and or not
"""
# if a==18 and b=='admin':
#     print("你是符合的")
# else:
#     print("你不行")

# if a == 18 or b == 'admin':
#     print("你是符合一点的的")
# else:
#     print("你完全不行")
"""
. 定义两个整数变量python_score、c_score，使⽤ input
获取成绩 编写代码判断成绩
2. 要求只要有⼀⻔成绩 > 60 分就输出合格

"""
# python_score = int(input("请输入py成绩"))
# c_score = int(input('请输入C成绩'))
# if python_score > 60 or c_score > 60:
#     print('成绩合格')
# debug 调试代码
"""
断点的意义是, debug 运⾏的时候, 代码会在断点出停下
来不执⾏
如果是想要查看代码的执⾏过程, 建议将断点放在第⼀⾏
在代码 和⾏号之间 点击,出现的红⾊圆点 就是断点, 再
次点击可以取消
pycharm 软件存在⼀个问题, 想要 debug 运⾏,可能⾄少
需要两个断点
"""
# 1. 定义 score 变量记录考试分数
# score = int(input('请输⼊分数'))
# # 2. 如果分数是 ⼤于等于 90分 显示 优
# if score >= 90:
#  print('优')
# # 3. 如果分数是 ⼤于等于 80分 并且 ⼩于 90分 显示 良
# elif (score >= 80) and score < 90:
#  print('良')
# # 4. 如果分数是 ⼤于等于 70分 并且 ⼩于 80分 显示 中
# elif (score >= 70) and score < 80:
#  print('中')
# # 5. 如果分数是 ⼤于等于 60分 并且 ⼩于 70分 显示 差
# elif (score >= 60) and score < 70:
#  print('差')
# # 6. 其它分数显示 不及格
# else:
#  print('不及格')

"""
 if嵌套   if语句中嵌套if语句
 if 判断条件1:
 判断条件1成⽴,执⾏的代码
 if 判断条件2:
 判断条件2成⽴,执⾏的代码
 else:
 判断条件2不成⽴,执⾏的代码
else:
 判断条件1不成⽴,执⾏的代码
 """

# 取款机取钱的过程, 假定 你的密码是: 123456, 账户余 额为 1000
# 1. 提示⽤户输⼊密码
# pwd = input('请输⼊密码:')
#  # 2. 判断密码是否正确
# if pwd == '123456':
#   print('密码输⼊正确')
#   # 3. 密码正确后,提示输⼊取款的⾦额,
#   money = int(input('请输⼊取款的⾦额:'))
#   # 4. 判断取款的⾦额和余额的关系
#   if money > 1000:
#    print('余额不⾜')
#   else:
#    print('取款中,请稍后....')
#   print('请收好你的钱....')
# else:
#   print('密码输⼊错误,请重试')

