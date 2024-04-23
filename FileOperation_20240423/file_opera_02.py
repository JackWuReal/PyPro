"""
⽂件操作
- 按⾏读取⽂件 readline()

json 操作(特殊的⽂本⽂件)
- 如何定义,语法
- 读取(重点)
- 写⼊

"""

"""
文件操作
按行读取文件readline()

# 文件对象.readline()  一次读取一行的内容 返回读取的内容
read()  和readline() 如果读到文件末尾返回的都是空字符串
"""

with open('a.txt', encoding='utf-8') as f:
    buf = f.readline()
    print(buf)
    buf1 = f.readline()
    print(buf1)
    buf2 = f.readlines()
    print(buf2)

"""
读取大文件
"""