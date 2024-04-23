import unittest
import os
from unittest import TestSuite

from unittest_first import TestAssert  # 导包
from test_tool import TestTool
from test_parameterized import TestAdd

from app import base_dir

suite = unittest.TestLoader().discover(base_dir(),pattern='test_pa*.py')  # 实例化测试套包对象

# suite.addTest(unittest.makeSuite(TestAssert))  # 将测试类加入测试套包中
# suite.addTest(unittest.makeSuite(TestTool))
# suite.addTest(unittest.makeSuite(TestAdd))

unittest.TextTestRunner().run(suite)  # 实例化测试套包执行对象并执行
