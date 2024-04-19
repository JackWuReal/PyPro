"""
包的导入

"""

# 快捷键导包直接使用工具名
# from PythonPackage.tools import sum_2_num
# snum = sum_2_num(1,3)
# print(snum)

# from 包名 import 模块名   调用 模块名.函数
# from PythonPackage import tools
# tools.sum_2_num(99,-1)
# print(tools.sum_2_num(99,-1))

# import 包名


import PythonPackage.tools
num = PythonPackage.tools.sum_2_num(99,-1)
print(num)