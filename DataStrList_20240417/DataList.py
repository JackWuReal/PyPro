"""
List 列表 顺序结构

1, 列表,list, 使用 []
2, 列表可以存放任意多个数据
3, 列表中可以存放任意类型的数据
4, 列表中数据之间 使用 逗号隔开


"""
# list1 = list()  #定义空列表
# list2 = list('abcde+fg') #非空列表  类型转换 list(可迭代类型)  能够使用for循环的就是可迭代类型
# print(type(list1),list1)
# print(type(list2),list2)

list3 = []
list4 = [1,2,3,'hello',False,8,'hello']
# print(list4, type(list4))
"""
列表的切片 得到是 新的列表.
字符串的切片 得到是 新的字符串
如果下标 不存在.会报错.

"""
# print(list4[3])
# print(list4[-9]) 下标不存在会报错
# 获取中间两个数据 列表切片
# print(list4[2:4])

# 列表查询 index()
# print(list4.index('hello'))
# print(list4.index('hello', 4))
# count()方法 统计数据在列表中出现的次数
# print(list4.count('hello'))

# 追加数据 append()
"""
列表.append(数据) # 想列表的尾部添加数据
# 返回: None, 所以不用使用 变量 = 列表.append()
直接在原列表中添加数据, 不会生成新的列表,如果想要查看添加后的数据, 直接 print() 打印原列表

"""
print(list4.append(999),list4)
print(list4.append(911),list4)

# 删除数据 pop()
# print(list4.pop(0)) #删除序号为0的数据
# print(list4.pop())  #删除最后一个数据  返回的删除的对象
# print(list4)

# 修改列表中的数据
# list4[1] = 999;
# list4[-1] = 'wgk'
# print(list4)

# 列表的反转 reserse() [::-1]
# print(list4.reverse(),list4) 直接在原列表反转
# list5 = list4[::-1]  生成新列表
# print(list5)

# 列表的排序  前提列表的数据要一样
# list5 = [1,2,38,9,5,4,2,0]
# list5.sort()  #从小到大
# print(list5)
# list5.sort(reverse=True) #从大到小
# print(list5)
# 列表的嵌套  列表中的数据都是列表
list_student = [[1,'李','男'],[3,'王','女'],[5,'吴','男']]
print(list_student[0][1])
list_student[0].append('帅')
print(list_student)
list_student[0].pop()
print(list_student)
# 打印所有人的年龄
for info in list_student:  #info 为列表
    print(info[0])


