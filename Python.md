# Python面试题汇总

* python只是有点了解么？

## 基础算法

* 口述冒泡排序
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 使用示例
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
```

* 其他排序算法

## python基础定义
* 缺省参数与多值参数的区别
  * 缺省参数：定义函数时给某个函数一个默认值,具有默认值的参数
    * 调用函数时,**若没有传入缺省参数的值则使用默认值**
    * 将常见的值设置为参数的缺省值,从而**简化函数的调用**
    * 必须保证缺省参数在参数列表末尾
    * 在调用函数时,多个缺省参数需要指定参数名,以方便解释器知道参数的对应关系
```python
def print_info(name,gender='男生'):
  print(f'{name} is {gender}')
```
```python
def print_info(name,title="",gender="男生"):
    print(f'{title} {name} is {gender}')
print_info("小明")
print_info("老王",title="班长")# 需要指定参数名
print_info("小美",gender="女生")# 若不指定缺省参数的值则采用默认值
```
  * 多值参数：如果一个函数能处理的参数个数不确定,可以考虑多值参数
    * *args用于接收元组类型数据,args为习惯命名,可自定义
```python
def demo(num,*args):
    print(num)
    print(args)

demo(1,2,3,4,5)
```
  * 元组的拆包方式：在元组变量前,增加一个*
```python
# 元组拆包
def sum_numbers(*args):
    num = 0
    for n in args:
        num += n
    return num
# 将一个元组变量传递给函数对应的参数
nums = (1,2,3)
result = sum_numbers(*nums)
```
* 匿名函数：没有函数名称且能接受任何数量的参数,只能返回一个表达式的值
```python
sum = lambda arg1,arg2:arg1+arg2
sum(1,2)
sum(9,10)
```
* python构造方法是什么
* 什么是装饰器及应用场景并手写装饰器
  * 装饰器的本质是闭包、主要作用是在不该百年被装饰函数的原有功能的基础上，增加额外的功能
  * 应用场景：插入日志，性能测试，事务处理
  * https://zhuanlan.zhihu.com/p/53666925
```python
import time
# 计算函数执行时间的装饰器
def timer(func):

  def deco(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    stop_time = time.time()
    print("running time is %s " % (stop_time - start_time))
    return deco

@timer
def test1():
  time.sleep(3)
print("in the test 1")

test1()
```
* python的可变数据类型和不可变数据类型有哪些
  * 可变数据类型和不可变数据类型：看修改赋值时是否开辟新的内存空间
  * 可：list set dirt
  * 不可：tuple str int float
* list set dirt tuple四者的区别
  * list set tuple：list有序列表（可变）
  * tuple有序集合（不可变）
  * set无序不重复序列（可变）
  * dirt 字典：kv键值对，键必须唯一、键必须是不可变数据类型：字符串，数字，元组 值可以是任意数据类型
* python的三层架构
* python的数据存储方式
* self参数和cls参数
  * self参数：由哪个对象调用的方法,方法内的self就是哪个对象的引用
  * 在类封装的方法中可以通过,self.访问对象的属性和方法
* python类静态类和动态类
  * 动态类：普通类默认动态类、可以在运行时动态添加新属性和方法的类
  * 静态类：使用slots 不允许动态添加新属性和方法的类
```python
class StaticClass:
    __slots__ = ['attribute1', 'attribute2']  # 限定类实例可以拥有的属性
 
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
 
# 以下是静态类的使用
static_instance = StaticClass('value1', 'value2')
# static_instance.new_attribute = 'value3'  
# 这会抛出AttributeError，因为'new_attribute'没有在__slots__中定义
```
* 封装继承多态的定义
    * 封装:将属性和方法封装到一个抽象类中的过程
      * 外界使用类创建对象通过对象调用方法、对象方法的细节都被封装在类的内部
    * 继承：可以考虑将想同逻辑的代码抽取封装到父类中，再通过继承关系直接实现子类对象并调用父类中的方法使用
      * 在继承关系中子类可以拥有父类的所有方法和属性
      * 继承有传递性 爷-父-子
    * 多态：不同子类对象调用相同的父类方法，产生不同的执行结果
    * 方法重写：
      * 扩展重写
      * 覆盖重写
* 实例属性 实例方法
```python
class Car:
    # 实例属性
    def __init__(self, brand):
        self.brand = brand
```
* 各种属性 **类属性、类方法**
  * **类属性**:就是给类对象中定义的属性，用来记录和这个类相关的特征，不会用来记录具体对象的特征
  * 调用方式:类名.类属性名  <u>类属性被该类的所有对象共享</u>：可以通过*实例.类属性名*来直接调用和修改
  * **类方法**：简化方法调用步骤(可以直接通过'类名.方法名'调用) 也可以通过*实例.类方法*名直接调用
  * 用修饰器`@classmethod`修饰
  * 在自动化测试背景下，需要保证生成的对象始终只有一个，就可以使用类对象类属性类方法
```python
class Demo:
    @classmethod
    def le_method(cls):
        pass
```
```python
class Tool(object):
    #定义类属性count 用来记录创建工具对象的总数
    count = 0
    def __init__(self,name):
        self.name = name
        # 类属性直接用类名.属性名调用 
        # 每实例一个Tool累加一次
        Tool.count += 1
    @classmethod
    def show_tool_count(cls):
    # 显示工具对象的总数
        print(f'{cls.count}')
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

Tool.show_tool_count()
```
```python
from selenium import webdriver

class DriverUtil:
    #驱动对象管理类
  __driver = None  # 初始情况驱动对象为空 私有属性
  @classmethod #类方法
  def get_driver(cls):
    #获取驱动对象方法
    if cls.__driver is None:  # 如果驱动对象为空
        cls.__driver = webdriver.Chrome()  # 创建驱动对象
    return cls.__driver  # 返回驱动对象
    
if __name__ == '__main__':
    DriverUtil.get_driver()  # 调用获取驱动对象方法
```
* 各种属性：**私有属性私有方法**
  * 当属性和方法只需要在类定义内部使用时,就可以使用私有属性和私有方法
  * **在类定义外部**、无论是实例对象和类对象均无法均无法获取私有属性和调用私有方法
  * `私有属性 __属性名  私有方法 __方法名()`
  * 调用方式：在类定义内部`cls.__属性名 cls.__方法名() self.__属性名 self.__方法名`

```python
class Women:
  def __init__(self, name):
    self.name = name
  # 通过'__age'定义私有属性
    self.__age = 18
  # 通过__secret()定义私有方法
  def __secret(self):
    # 私有属性在类内部可以直接调用self.__age
    print(f"my age is {self.__age}")
      
xiaofang = Women("dmm")
# 私有属性，外部无法直接访问
#print(xiaofang.__age)
# 私有方法，外部无法直接调用
#xiaofang.__secret()
```
* 各种方法的定义 **静态方法**
  * 类中封装一个方法，这个方法既不需要访问实例属性或调用实例方法、也不需要访问类属性或调用类方法、可以将这个方法封装为一个静态方法
  * 用修饰器`@staticmethod`
  * 通过类名.调用静态方法
  * 用来显示一些提示信息
```python
class Demo:
    @staticmethod
    def sta_method():
        pass
```

## 基础应用

* 如果给你两个等长的列表怎么把他整合为一个字典
* python的一些方法怎么用例如pop()
  * pop()会直接修改原始对象并返回被删除的元素
    * 列表pop()方法使用时不传入索引值默认**删除并返回**列表最后一个数据
    * `del_data = list_name.pop(index)`删除并返回指定索引对应的数据
    * 异常：IndexError
  * 字典pop()方法
    * `del_value = dirt_name.pop(key)`**删除并返回**key对应的value
    * 异常：keyError
* 有用过魔术方法吗怎么使用的：以两个下划线开头和结束的方法，满足某个条件会自动调用
  * `__slots__`
  * `__init__`
    * 在创建对象后会自动调用
    * 初始化对象给对象添加属性
    * 在创建对象时必须传递实参
```python
class Cat:
    def __init__(self,name):
        print("这是init方法")
        self.name = name
blue_cat = Cat('蓝宝')
black_cat = Cat('黑宝')
```
  * `__str__`
    * 自定义打印对象变量的信息可以使用__str__方法、默认情况下会打印对象的内存地址
    * 该方法必须返回一个字符串数据

## python实现自动化

* 说说Python怎么做接口自动化？
```python
import unittest
import requests


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url = 'http://example.com/api/method'
        self.headers = {'Content-Type': 'application/json'}

    def test_get_request(self):
        response = requests.get(self.url, headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        response = requests.post(self.url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()

# setup() teardown()有什么区别
'''
setUp：表示前置条件，它在每一个用例执行之前必须会执行一次 
setUp可以理解为我们需要自动化测试时，需要打开网页窗口，输入对应测试地址，这一些属于前置条件。
teardown() 表示释放资源，它在每次用例执行完之后会执行一次可以理解为我们测试完毕后，需要关闭浏览器。
'''
import unittest
class Xseq(unittest.TestCase):
    def setUp(self):
        print("前置测试条件")

    def tearDown(self):
        print("结束测试条件")

    def testadd(self):
        print('1+1=', 1 + 1)

    def testsub2(self):
        print('3-2=', 3 - 2)

    def testsub1(self):
        print('3-3=', 3 - 3)

    def mul(self):
        print('3*1', 3 * 1)

if __name__ == "__main__":
    unittest.main()
'''
若我想要改变setUp()在所有用例执行之前只执行一次，和tearDown()函数在所有用例执行之后只执行一次的话
1. 需要使用python中的@classmethod内置装饰器
2. 需要把函数名改为setUpClass(cls) / tearDownClass(cls)
'''
import unittest
class Xseqcls(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("前置测试条件")
    @classmethod
    def tearDownClass(cls):
        print("结束测试条件")

    def testadd(self):
        print('1+1=', 1 + 1)

    def testsub2(self):
        print('3-2=', 3 - 2)

    def testsub1(self):
        print('3-3=', 3 - 3)

    def mul(self):
        print('3*1', 3 * 1)

if __name__ == "__main__":
    unittest.main()
```






    