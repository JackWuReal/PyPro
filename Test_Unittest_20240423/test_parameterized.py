import unittest
import json

from parameterized import parameterized
from tools import add

"""
pip install parameterized

pip list # 查看安装的所有的插件
"""
"""

#
# - 通过参数的方式来传递数据，从而实现数据和脚本分离。并且可以实现用例的重复执行。(在书写用例方法的时候，测
# 试数据使用变量代替，在执行的时候进行据说传递)
# - unittest 测试框架，本身不支持参数化，但是可以通过安装unittest扩展插 件 parameterized 来实现。



from parameterized import parameterized

1. 导包 from para... import para...
2. 修改测试方法，将测试方法中的测试数据使用 变量表示
3. 组织测试数据，格式 [(), (), ()], 一个元组就是一组测试数据
4. 参数化，在测试方法上方使用装饰器 @parameterized.expand(测试数据)
5. 运行(直接 TestCase 或者 使用 suite 运行)
"""

# data = [(1, 1, 2), (1, 2, 3), (2, 3, 5), (4, 5, 9)]

from read_data import build_add_data
from read_data import build_add_data1
from read_data import build_add_data2


class TestAdd(unittest.TestCase):
    @parameterized.expand(build_add_data())
    def test_add(self, a, b, expect):
        print(f'a:{a}, b:{b}, expect：{expect}')
        self.assertEqual(expect, add(a, b))

    @parameterized.expand(build_add_data1())
    def test_add1(self, a, b, expect):
        print(f'a:{a}, b:{b}, expect：{expect}')
        self.assertEqual(expect, add(a, b))

    @parameterized.expand(build_add_data2())
    def test_add2(self, a, b, expect):
        print(f'a:{a}, b:{b}, expect：{expect}')
        self.assertEqual(expect, add(a, b))




if __name__ == '__main__':
    unittest.main()
