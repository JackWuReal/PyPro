# 数据类型
"""数字型
 整型 浮点型 布尔型

 非数字型

字符串
列表
元组
集合
字典
 """
# 查看数据类型 type(数据/变量名)
print(type(18))
print(type("hello"))
print(type(int(19)))
print(type(float(19)))
print(type(str(19)))
print(type(tuple([8,9,6.3])))
print(type(list([1,2,3])))
name = "吴阁揆"
age = 18
#格式化输出字符串format（） 调用字符串的format方法可以实现字符串的格式化
print("name={},age={}".format(name,age))# {}占位符 format（）方法中的参数为实际要替换的数据  数量一致
# 格式化输出字符串-f的实现  字符串前添加f标志
print(f"name={name},age={age}")
# input('提示信息')函数  输入函数  input得的数据类型默认为str
# height = input('请输入一个数字')
# print(height)
# 1.提示⽤户输⼊两个数字
# 2. 使⽤获取到的数据进⾏加法运算
# 3. 在控制台输出计算结果，格式要求:xx + xx = xx
# x = int(input('请输入1个数字:'))
# y = int(input('请输入另1个数字:'))
# z = x + y
# print(f'{x} + {y} = {z}')

# 算术运算符
# print(999%2)  求余
# print(999//2) 求商
# print(999/2)  除
print(999-3)
print(999*2)
# print(10**2)  次方
print(15+3)
# 比较运算符  得到的结果是布尔类型 true false
# < > >= <=只能用于同类型之间的比较
# == 值相等即相等  != 值不相等
# a=5
# b=6
# print(a==b)
# print(a>=b)
# print(a<=b)
# print(a!=b)
# 赋值运算符和复合赋值运算符
c = 7
d = 10
# d += c
# d -= c
# d /= c
d //= c  #d除以c 取商赋给d
# d %= c   d除以c 取余赋值给d
# print(f'd={d}')
print(f'年龄: {age},姓名: {name}')

print(f'{name}是否已成年:{age>=18}')


