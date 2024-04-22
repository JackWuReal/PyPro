"""
1, 什么是重写?
    重写是在子类中定义了和父类中名字一样的方法.
2, 重写的原因? 为什么重写?
    父类中的代码不能满足子类对象的需要
3, 重写的方式
    3.1 覆盖式重写
    3.2 扩展式重写

"""

"""覆盖式重写"""


class Dog:
    def bark(self):
        print('Dog bark  aoaoaooaao')


# class Xtq(Dog):
#     def bark(self):
#         print('Dog bark a wuwuwuwuuwu')
#     pass


# if __name__ == '__main__':
#     xt = Xtq()
#     xt.bark()
#     dg = Dog()
#     dg.bark()


"""扩展式重写"""

class XTQ(Dog):
# 需要哮天犬 嗷嗷嗷叫, 父类中的 bark 方法,不能满足子类对象的需要, 覆盖式重写
    def bark(self):
        super().bark() # 调用父类中的功能
        print('嗷嗷嗷叫.....')
        print('嗷嗷嗷叫.....')


# if __name__ == '__main__':
#     xt = XTQ()
#     xt.bark()
#     dg = Dog()
#     dg.bark()

"""
多态
多态: 调用代码的技巧
多态:不同的子类对象调用相同的方法，产生不同的执行结果
"""

"""
私有和公有

在Python 中,定义类的时候, 可以给 属性和方法设置 访问权限, 即规定在什么地方可以使用.
权限一般分为两种: 公有权限 私有权限

    公有权限：直接定义的属性和方法就是公有的
        可以在任何地方访问和使用, 只要有对象就可以访问和使用
    私有权限
        1, 只能在类内部定义(class 关键字的缩进中)
        2, 只需要在 属性名 或者方法名 前边 加上两个 下划线, 这个方法或者属性就变为私有的
        私有只能在当前类的内部使用，不能在类外部使用和子类中使用
        
一般来说,定义的属性和方法 都为公有的.
某个属性 不想在外部直接使用, 定义为私有
某个方法,是内部的方法(不想在外部使用), 定义为私有

"""
"""定义人类, name 属性 age 属性(私有)"""
class Person:
    def __init__(self, name, age):
        self.name = name # 公有
        self.__age = age # 公有-->私有, 在属性名前加上两个下划线

    def __str__(self): # 公有方法
        return f"{self.name}, {self.__age}"

    def set_age(self, age): # 定义公有方法,修改私有属性
        if age < 0 or age > 120:
            print('提供的年龄信息不对')
            return
        self.__age = age


# if __name__ == '__main__':
#     xw = Person('小王', 18)
#     print(xw)
#     xw._age = 99 # 添加一个公有属性 __age
#     print(xw._age)
#     print(xw)
#     xw.set_age(100)
#     print(xw)

"""
对象，属性，方法
python 中一切皆对象

类对象 就是 类, 就是使用 class 定义的类

在代码执行的时候, 解释期会自动的创建.
作用:
1, 使用类对象创建 实例对象
2, 存储一些类的特征值(类属性)

实例对象

1, 创建对象也称为实例化, 所以 由类对象(类) 创建的对象 称为是 实例对象, 简称实例
2, 一般来说,没有特殊强调,我们所说的对象 都是指 实例对象(实例)
3, 实例对象 可以保存实例的特征值 (实例属性)
4, 就是使用 类名() 创建的对象

使用 实例对象.属性 访问 属性的时候,
 会先在 实例属性中查找,如果找不到,
 去类属性中查找, 找到就使用, 找不到,就报错
即: 每个实例对象 都有可能访问类属性值(前提,实例属性和类属性不重名)

实例属性
是每个实例对象 具有的特征(属性), 每个实例对象的特征
一般都是在 init 方法中,使用 self.属性名 = 属性值 来定义
每个实例对象 都会保存自己的 实例属性, 即内存中存在多份

# 可以认为是通过 self
实例对象.属性 = 属性值 # 修改
实例对象.属性 # 访问


类属性
是类对象具有的 特征, 是整个类的特征
一般 在类的内部(class 缩进中), 方法的外部(def 的缩进外部) 定义的变量
只有类对象保存一份, 即在内存中只有一个

# 即通过类名
类对象.属性 = 属性值
类对象.属性

什么时候 定义类属性?
代码中 使用的属性 基本上 都是 实例属性,即都通过 self 定义.
当 某个属性值描述的信息是整个类的特征(这个值变动,所有的这个类的对象这个特征都会发生变化)
"""

"""
1. 定义一个 工具类
2. 每件工具都有自己的 name
3. 需求 —— 知道使用这个类，创建了多少个工具对象?
"""


# class Tools:
#     count = 0  # 类属性 # 定义类属性 count,记录创建对象的个数
#
#     def __init__(self,name): # name是实例属性
#         self.name = name
#         Tools.count += 1
#
#
# if __name__ == '__main__':
#     print(Tools.count)
#     tool = Tools('剪刀')
#     print(Tools.count)
#     tool1 = Tools('锤子')
#     print(Tools.count)
#     print(tool1.count)  # 先找实例属性 count, 找不到, 找类属性 count, 找到,使用


"""
方法的划分
    实例方法：
    如果方法中 需要使用 实例属性, 则这个方法 **必须** 定义为实例方法
    # 直接定义的方法就是实例方法
    class 类名:
        def 方法名(self):
        pass
        参数一般写作 self, 表示的是 实例对象
        实例对象.方法名()
    
    类方法：
    如果 方法中 不需要使用 实例属性, 但需要使用 类属性, 则这个方法 **可以** 定义为 类方法(建议)
    # 定义类方法,需要在方法名上方 书写 @classmethod , 即使用 @classmethod 装饰器装饰
    class 类名:
        @classmethod
        def 方法名(cls):
        pass
        参数一般写作cls 表示类对象即 类名, 同样不需要手动传递,Python 解释器会自动传递
    # 方法一
    类名.方法名()
    # 方法二
    实例对象.方法名()

    静态方法
    方法中即不需要使用 实例属性, 也不需要使用 类属性, **可以** 将这个方法定义为 静态方法
    # 定义静态方法, 需要使用 装饰器 @staticmethod 装饰方法
    class 类名:
        @staticmethod
        def 方法名():
            pass
            
    # 方法一
    类名.方法名()
    # 方法二
    实例对象.方法名()

"""

class Tool:
    count = 0  # 定义类属性 count,记录创建对象的个数

    def __init__(self, name):
        self.name = name # 实例属性, 工具的名字
        Tool.count += 1 # 修改类属性的值

    @classmethod
    def show_tool_count(cls): # cls 就是类对象, 类名
        return cls.count



if __name__ == '__main__':
    # 查看 创建对象的个数
    print(Tool.show_tool_count())
    tool1 = Tool('锤子')
    print(Tool.show_tool_count())
    tool2 = Tool('扳手')
    print(tool2.show_tool_count())


