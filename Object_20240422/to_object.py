# 循环 .... else 语法
#  for 变量 in xxx:
#  if xx:
#  break # 如果循环执⾏了 break,就不再执⾏ else
#  中的代码
#  else:
#  循环不是被 break 终⽌的,可以执⾏.

"""
oop 面向对象编程

⾯向对象(oop) 是⼀种编程⽅法, 编程思想(即指导如何写代
码), 适⽤于 中⼤型项⽬
⾯向过程也是⼀种编程思想, 适⽤于⼩型项⽬
⾯向过程 和 ⾯向对象 都可以实现某个编程的⽬的.
⾯向过程 考虑的是 实现的细节
⾯向对象 考虑的是 结果(谁能做这件事)
"""

"""
类和对象

类: 是对具有相同特征或者⾏为的事物的⼀个统称, 是抽象
的,不能直接使⽤
    指代 多个事物
    代码中 类是由关键字 class 定义
对象:是由类创建出来的⼀个具体存在的事物, 可以 直接使⽤
    指代 ⼀个具体事物
    代码中 使⽤ 类 去创建(实例化)
"""

"""
类的构成

类的构成, 类的三要素
1, 类名 (多个事物 起⼀个名字,标识符规则, ⻅名知意, 类名
⽤例满⾜⼤驼峰命名法(所有单词的⾸字⺟⼤写))
2, 属性 (事物的特征)
3, ⽅法 (事物的⾏为)

面向对象代码的步骤
1, 设计类 (找类的三要素)
2, 定义类
3, 创建对象(实例化对象)
4, 由对象调⽤类中的⽅法
"""

# 需求:
#  进入某web项目登录页面后, 输入用户名密码验证码之后点击登录按钮可以登录系统
"""
类名: LoginPage
属性: ⽤户名(username), 密码(password), 验证码(verify_code), 登录按钮(login_btn)
⽅法: 登录⽅法(login)
"""

"""
面向对象的基本语法
类的基本使用
1.定义类
在python中定义类使用关键字 class
class 类名:
     # 在 class 的缩进中定义类的属性和⽅法,
     def ⽅法名(self): # ⽅法的本质是函数
         pass
         
2.创建对象（实例化对象）
在代码中，对象是由 类对象.类名 #就是创建对象
一般使用变量将创建的对象保存起来
变量 = 类名() 
# ⼀般将这个变量 称为是对象, 本质, 变量中
保存的是对象的***引⽤地址***
"""
"""
3.调用类中的方法
由类创建的对象, 可以调⽤类中的⽅法
- 语法
对象.⽅法名()
"""

"""
需求:⼩猫 爱 吃⻥，⼩猫 要 喝⽔
类的设计:
类名: 猫(Cat)
属性: 暂⽆
⽅法: 吃⻥(eat), 喝⽔(drink)

"""


# class Cat:
#     def eat(self):  # self 是调⽤这个⽅法的对象
#         print('eat fish')
#
#     def drink(self):
#         print('drink water')


# if __name__ == '__main__':
#
# #     tom = Cat()
# #     tom.eat()
# #     tom.drink()

"""
self 参数
1, 参函数的语法上来看, self 是形参, 名字可以任意的变量
名, 只是我们习惯性叫 self
2, 特殊点: self 是⼀个普通的参数, 按照函数的语法,在调⽤
的时候,必须传递实参值, 
原因, 是 Python 解释器⾃动的将调用这个⽅法的对象作为参数传递给 self
所以 self 就是调用这个方法的对象
"""
# if __name__ == '__main__':
#
#     # 创建对象
#     tom = Cat()
#     print(f'tom.id：{id(tom)}')
#     #
#     tom.eat()
#
#     blue_cat = Cat()
#     print(f'blue_cat_id:{id(blue_cat)}')
#     blue_cat.eat()

"""
属性
属性表示事物的特征
可以给对象添加属性 或者获取对象的属性值.
    给对象添加属性:
    对象.属性名 = 属性值 # 添加或者修改
        获取对象的属性值:
        对象.属性名
在⽅法中操作属性(self 是对象):
self.属性名 = 属性值
self.属性名

"""


class Cat:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("init方法执行了吗")

    def eat(self):
        print(id(self))
        print(f'{self.name},{self.age}岁爱吃鱼')


# if __name__ == '__main__':
#     tom = Cat('tom',18)
#     tom.eat()


"""
需求:
1. 房⼦(House) 有 户型、总⾯积 和 家具名称列表 – 新房
⼦没有任何的家具
2. 家具(HouseItem) 有 名字 和 占地⾯积，其中
– 席梦思(bed) 占地 4 平⽶
– ⾐柜(chest) 占地 2 平⽶
– 餐桌(table) 占地 1.5 平⽶
3. 将以上三件家具添加到房⼦中
4. 打印房⼦时，要求输出:户型、总⾯积、剩余⾯积、家具名
称列表
剩余 ⾯积
1.在创建房⼦对象时，定义⼀个 剩余⾯积的属性，初始值和
总⾯积相等
2.当调⽤ add_item ⽅法，向房间 添加家具 时，让 剩余⾯
积 -= 家具⾯积


类名: 房⼦类(House)
属性: 户型(h_type),
No. 18 / 22
 总⾯积 total_area
 剩余⾯积 free_area = total_area
 家具名称列表 item_list = []
⽅法: __init__, __str__
添加家具的⽅法 add_item (1, 修改剩余⾯积 2, 判断剩余
⾯积和家具⾯积的关系 3, 想家具列表中添加 家具的名字)

类名: 家具类(HouseItem)
属性: 名字 name
 占地⾯积 area
⽅法: __str__ , __init__
三个家具对象
– 席梦思(bed) 占地 4 平⽶
– ⾐柜(chest) 占地 2 平⽶
– 餐桌(table) 占地 1.5 平⽶

"""

class HouseItem:
    def __init__(self,name,area):
        self.name = name # 名字
        self.area = area # 占地⾯积
    def __str__(self):
        return f'{self.name} 占地⾯积 {self.area}'
class House:
    def __init__(self, h_type, area):
        self.h_type = h_type # 户型
        self.total_area = area # 总⾯积
        self.free_area = area # 剩余⾯积和总⾯积一样
        self.item_list = [] # 刚开始没有家具


    def __str__(self):
        return f"户型:{self.h_type}、总⾯积:{self.total_area} 平⽶、剩余⾯积:{self.free_area}平⽶、家具名称列表:{self.item_list}"
    def add_item(self, item): # 1. 房⼦对象(self) 2. 家具对象(传参)
        """添加家具, item 家具对象"""
        # 1. 先判断房⼦的剩余⾯积和家具的占地⾯积的关系
        if self.free_area > item.area: # 对象.属性 获取属性值
            print(f'添加家具: {item.name}')
            self.item_list.append(item.name)
            # 修改剩余⾯积
            self.free_area -= item.area
        else:
            print(f"房⼦剩余⾯积不⾜,换个⼤房⼦吧.....")


# if __name__ == '__main__':
#      # 创建家具对象
#      bed = HouseItem('席梦思', 4)
#      chest = HouseItem('⾐柜', 2)
#      table = HouseItem('餐桌', 1.5)
#      print(bed)
#      print(chest)
#      print(table)
#      # 创建房⼦
#      house = House('三室⼀厅', 100)
#      print(house)
#      house.add_item(bed)
#      print(house)
#      house.add_item(chest)
#      print(house)
#      house.add_item(table)
#      print(house)

"""

定义一个水果类，包含名称、颜色和价格属性，定义展示水果信息的方法`show`，
打印信息的格式：`水果名称：苹果，颜色：红色，价格：3.5`。
然后通过水果类创建苹果对象、桃子('peach')对象，并调用展示水果信息的方法
"""


class Fruit:
    def __init__(self, name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(f'水果名称：{self.name},水果颜色：{self.color},水果价格：{self.price}')


if __name__ == '__main__':
    apple = Fruit('apple','red',3.5)
    apple.show()
    peach = Fruit('peach','orange',2.5)
    peach.show()