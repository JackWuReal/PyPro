"""
魔法方法

在Python 中存在⼀类⽅法, 以两个下划线开头, 两个下划线结尾,
 在满⾜某个条件的情况下,会⾃动调⽤, 这⼀类⽅法 称为是
魔法⽅法


1.调用时机
2.应用场景
3.注意事项
"""
"""
初始化方法  __init__
1.调用时机
    在创建对象后会自动调用
2.应用场景
    初始化对象给对象添加属性
3. 注意事项
 - 不要写错
 - 如果 属性是会变化的, 则可以将这个属性的值作为参数
传递, 在创建对象的时候,必须传递实参值
"""


# class Cat:
#      def __init__(self, name):
#          print('我是 init ⽅法, 我被调⽤了')
#          self.name = name
#
#      def eat(self):
#          print(f'{self.name} eat')


# if __name__ == '__main__':
#
#     cat = Cat('jjj')  # 在创建对象的时候,必须传递实参值
#     cat.eat()
#     # init ⽅法 创建对象之后 会⾃动调⽤
#     # 1 会 2 不会
#     # Cat # 2 不是创建对象
#     # Cat() # 1 因为是创建对象
#     # tom = Cat # 2 不是创建对象, 即 tom 也是类
#     #
#     # blue = Cat() # 1 创建对象
#     # b = blue # 2 不是创建对象, 只是引⽤的传递
#     #
#     # t = tom() # 1, tom 已经是类, 类名() 就是创建对象
#     blue_cat = Cat('蓝猫')
#     blue_cat.eat()
#     black_cat = Cat('⿊猫')
#     black_cat.eat()


"""
__str__ 方法
1, 调⽤时机
 使⽤ print(对象) 打印对象的时候, 会⾃动调⽤
 1, 如果没有定义 __str__ ⽅法, 默认打印的是 对象的引
⽤地址
 2, 如果定义 __str__ ⽅法,打印的是 ⽅法的返回值
2, 应⽤场景
 使⽤ print(对象) 打印输出对象的属性信息
3, 注意事项
 必须返回⼀个 字符串
 
定义 Cat 类, 包含属性 name 和 age, 打印对象的时候,可以
输出对象的姓名和年龄
类名: Cat
属性: name, age
⽅法: __str__ , __init__
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name:{self.name} age:{self.age}'


if __name__ == '__main__':
    cat = Cat('tom',3)
    print(cat)