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

* python构造方法是什么
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

## 基础应用

* 如果给你两个等长的列表怎么把他整合为一个字典
* python的一些方法怎么用例如pop()
* 有用过魔术方法吗怎么使用的

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
```






    