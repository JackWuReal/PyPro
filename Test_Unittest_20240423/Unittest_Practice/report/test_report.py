import unittest
from Test_Unittest_20240423.Unittest_Practice.app import Base_Dir

from htmltestreport import HTMLTestReport

import BeautifulReport

suite = unittest.TestLoader().discover(Base_Dir+'/case','test*.py')

# report = BeautifulReport.BeautifulReport(suite)
# report.report('Testreport','LoginReport',Base_Dir+'/report')

runner = HTMLTestReport(Base_Dir + '/report/login_report.html', '登录测试报告', 'V1.0')
runner.run(suite)
