"""

绝对路径：

将来的项目是分目录书写的, 使用相对路径,可能会出现找不到文件的情况,此时需要使用 绝对路径
方法:
1. 在项目的根目录,创建一个 Python 文件(app.py 或者 config.py)
2. 在这个文件中 获取项目的目录,在其他代码中使用 路径拼接完成绝对路径的书写

"""
import os.path

"""
获取当前文件的绝对路径
"""

abspath = os.path.abspath(__file__)  # 获取当前文件的绝对路径
print(abspath)

dirname = os.path.dirname(abspath)
print(dirname)

def base_dir():
    return os.path.dirname(__file__)
