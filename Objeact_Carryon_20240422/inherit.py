"""
面向对象
- 继承(重点)
- 多态(了解)
- 权限划分(公有 和 私有)
- 对象(实例对象 和 类对象)
- 属性(实例属性 和 类属性)
- 方法(实例方法 类方法 静态方法)
- 案例
文件操作(使用代码操作文件,对文件进行读写, 重点是读)


"""
"""
继承
1. 继承描述的是类与类之间的关系 is ... a
2. 继承的好处: 减少代码冗余,重复代码不需要多次书写, 提高编程效率
"""

"""
# class 类A(object):
# class 类A():
class 类A: # 默认继承 object 类, object 类 Python 中最原始的类
pass
class 类B(类A): # 就是继承, 类 B 继承 类 A
pass
# 类 A: 父类 或 基类
# 类 B: 子类 或 派生类

子类继承父类之后, 子类对象可以直接使用父类中的属性和方法

"""

# 1. 定义动物类，动物有姓名和年龄属性，具有吃和睡的行为
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name} 吃东西')
    def sleep(self):
        print(f"{self.name} 睡觉")
# 2. 定义猫类，猫类具有动物类的所有属性和方法，并且具有抓老鼠的特殊行为
class Cat(Animal):
    def catch(self):
        print(f"{self.name} 会抓老鼠...")
# 3. 定义狗类，狗类具有动物类的所有属性和方法，并且具有看门的特殊行为
class Dog(Animal):
    def look_the_door(self):
        print(f"{self.name} 正在看家....")
# 4. 定义哮天犬类，哮天犬类具有狗类的所有属性和方法，并且具有飞的特殊行为
class XTQ(Dog):
    def fly(self):
        print(f"{self.name} 在天上飞...")


if __name__ == '__main__':
    xt = XTQ('哮天犬',10)
    xt.fly()
    xt.look_the_door()
    xt.eat()
    xt.sleep()

"""
继承具有传递性: C 继承 B, B 继承 A, C 可以使用 A 类中的属性和方法
对象调用方法的顺序: 对象.方法名()
1, 会现在自己的类中查找, 找到直接使用
2, 没有找到 去父类中查找, 找到直接使用
3, 没有找到, 在父类的父类中查找, 找到直接使用
4, 没有找到, ...
5, 直到 object 类, 找到直接使用, 没有找到,报错

"""