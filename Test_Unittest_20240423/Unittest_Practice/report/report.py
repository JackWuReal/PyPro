import unittest
from Test_Unittest_20240423.Unittest_Practice.app import Base_Dir

from htmltestreport import HTMLTestReport

import BeautifulReport

suite = unittest.TestLoader().discover(Base_Dir+'/case/','test_*.py')

# report = BeautifulReport.BeautifulReport(suite)
# report.report('Testreport','LoginReport',Base_Dir+'/report')

runner = HTMLTestReport(Base_Dir + '/report/login_report.html', '登录测试报告', 'V1.0')
runner.run(suite)


"""
当文件名是test_ 或 _test开头时
 类开头是 Test 或 Suite
 方法名开头是 test_ 或 check
 会使得程序认为默认是做自动化测试的文件
报  Empty suite 异常
"""
