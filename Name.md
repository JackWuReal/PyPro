## 命名规范

unittest 测试框架代码所处文件要求： 遵守 标识符命名规范：
1. 只能使用 字母、数字、下划线
2. 数字不能开头
3. 避免使用 关键字、已知函数名
* 测试模块名以test开头，如 test_login.py
* 测试类名以Test开头，如 TestLogin()
* 测试函数/方法名以test开头，建议编号如test_login()
-------
```python
import unittest #导包

    #待测试方法
def add(x, y):
    return x + y
    #封装 测试类，从 unittest.TestCase 类继承<br>
class TestAdd(unittest.TestCase):
    
    def setUp(self) -> None:
        print("-----setUp------")
        
    def tearDown(self) -> None:

    @classmethod
    def setUpClass(cls) -> None:
        print("====setUpClass=====")    

    @classmethod
    def tearDownClass(cls) -> None:
        print("====tearDownClass=====")

    # 自定义的测试方法
    def test01_add(self):
        print("测试方法1")
        ret = add(10, 20)
    # 断言响应结果
        self.assertEqual(30, ret)

    def test02_add(self):
        print("测试方法2")
        ret = add(100, 200)
    # 断言
        self.assertEqual(300, ret)
```
## 示例：生成测试报告
```python
import unittest

from htmltestreport import HTMLTestReport
# 创建suite实例
from py10_unittest_demo import TestAdd

suite = unittest.TestSuite()

# 指定测试类，添加测试方法
suite.addTest(unittest.makeSuite(TestAdd))

#创建HTMLTestReport实例
runner = HTMLTestReport('测试报告.Html')

# 调用run()传入suite
runner.run(suite)
```