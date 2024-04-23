"""
Fixture
代码结构 在用例执行前后会自动执行的代码结构

tpshop 登录
    1. 打开浏览器 (⼀次)
    2. 打开⽹⻚,点击登录 (每次)
    3. 输⼊⽤户名密码验证码1,点击登录 (每次, 测试⽅法)
    4. 关闭⻚⾯ (每次)
    2. 打开⽹⻚,点击登录 (每次)
    3. 输⼊⽤户名密码验证码2,点击登录 (每次, 测试⽅法)
    4. 关闭⻚⾯ (每次)
    2. 打开⽹⻚,点击登录 (每次)
    3. 输⼊⽤户名密码验证码3,点击登录 (每次, 测试⽅法)
    4. 关闭⻚⾯ (每次)
    5. 关闭浏览器 (⼀次)

"""

"""
方法级别的fixture
    在每个用例执行前都会自动调用 方法名固定
"""

def setUP(self):
    # 每个⽤例执⾏之前都会⾃动调⽤
    pass

def tearDown(self):
    # 在每个用例执行后都会自动调用
    pass

# ⽅法前置 ⽤例 ⽅法后置
# ⽅法前置 ⽤例 ⽅法后置

"""
类级别的Fixture
在类中所有的测试⽅法执⾏前后
会⾃动执⾏的代码, 只执⾏⼀次
"""
#
# # 类级别的 Fixture 需要写作类⽅法
#     @classmethod
#     def setUpClass(cls): # 类前置
#         pass
#     @classmethod
#     def tearDownClass(cls): # 后置
#         pass
#
# 类前置 ⽅法前置 ⽤例 ⽅法后置 ⽅法前置 ⽤例 ⽅法后置类后


import unittest

def setUpModule():
    print("\n电脑要开机吧*******")
    pass

class TestLogin(unittest.TestCase):
     def setUp(self) -> None:  #方法前置
        print('\n2. 打开⽹⻚, 点击登录')
     def tearDown(self) -> None:
        print('4. 关闭⽹⻚')
     @classmethod
     def setUpClass(cls) -> None:
        print('1. 打开浏览器')
     @classmethod
     def tearDownClass(cls) -> None:
        print('5. 关闭浏览器')
     def test_1(self):
        print('3. 输⼊⽤户名密码验证码1,点击登录 ')
     def test_2(self):
        print('3. 输⼊⽤户名密码验证码2,点击登录 ')
     def test_3(self):
        print('3. 输⼊⽤户名密码验证码3,点击登录 ')

"""
模块级别
模块, 就是代码⽂件
模块级别 在这个代码⽂件执⾏前后执⾏⼀

# 在类外部定义函数
def setUpModule():
 pass
def tearDownModule():
 pass
"""