"""
跳过:对于一些未完成的或者不满足测试条件的测试函数和测试类，可以跳过执行(简单来说, 不想执行的测试方法,可以
设置为跳过)
- 直接将测试函数标记成跳过
@unittest.skip('跳过的原因')
- 根据条件判断测试函数是否跳过
@unittest.skipIf(判断条件, reason='原因') # 判断条件为 True, 执行跳过

"""

# 跳过:对于一些未完成的或者不满足测试条件的测试函数和测试类，可以跳过执行(简单来说, 不想执行的测试方法,可以
# 设置为跳过)
# - 直接将测试函数标记成跳过
# @unittest.skip('跳过的原因')
# - 根据条件判断测试函数是否跳过
# @unittest.skipIf(判断条件, reason='原因') # 判断条件为 True, 执行跳过


import unittest
version = 29
class TestSkip(unittest.TestCase):
    @unittest.skip('没什么原因,就是不想执行')
    def test_1(self):
        print('方法一')
    @unittest.skipIf(version >= 30, '版本号大于等于 30, 测方法不用执行')
    def test_2(self):
        print('方法二')
    def test_3(self):
        print('方法三')
    if __name__ == '__main__':
        unittest.main()