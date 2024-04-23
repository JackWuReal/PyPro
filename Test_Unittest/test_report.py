"""
使用第三方的报告模版，生成报告 HTMLTestReport, 本质是 TestRunner
- 安装
pip install -i https://pypi.douban.com/simple/ HTMLTestReport
- 使用
1. 导包 unittest、HTMLTestReport
2. 组装用例(套件， loader )
3. 使用 HTMLTestReport 中的 runner 执行套件
4. 查看报告
"""

import unittest
import BeautifulReport


from test_parameterized import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))

result = BeautifulReport.BeautifulReport(suite)
result.report(filename='test report', description='测试报告', log_path=None)
