import variable

print(dir(variable))      # 打印引用模块的 自带参数
print(variable.__name__)  # 打印variable的__name__名
print(variable.func1())   # 执行该函数时不会执行其模块下 if __name__ == '__main__':
print(variable.func2())


