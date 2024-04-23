"""
用例脚本中
    断言(使用代码自动的判断预期结果和实际结果是否相符)
    参数化(将测试数据定义到 json 文件，使用)
    跳过(某些用例由于某种原因不想执行，设置为跳过)
生成测试报告（suite 和 runner(第三方)）
"""

"""
断言

使用代码自动的判断预期结果和实际结果是否相符
assertEqual(预期结果，实际结果)
- 判断预期结果和实际结果是否相等，如果相等， 用例通过，
如果不相等，抛出异常， 用例不通过

assertIn(预期结果，实际结果)
- 判断预期结果是否包含在 实际结果中， 如果存在，用例通过， 
如果不存在，抛出异常，用例不通过
"""
import unittest


class TestAssert(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(10,10)  # 用例通过

    def test_equal_2(self):
        self.assertNotEqual('hello',"hello1")

    def test_in(self):
        self.assertIn('admin', '欢迎 admin 登录') # 包含 通过
        self.assertIn('admin', '欢迎 adminnnnnnnn 登录') # 包含 通过
        self.assertIn('admin', '欢迎 aaaaaadminnnnnnnn 登录') # 包含 通过
        # self.assertIn('admin', '欢迎 adddddmin 登录') # 不包含 不通过  抛出异常
        # AssertionError: 'admin' not found in '欢迎 adddddmin 登录'
        self.assertIn('admin','admin')


