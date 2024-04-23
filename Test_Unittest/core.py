"""
UnitTest的核心要素
TestCase
    测试用例
    新建测试类必须继承 unittest.TestCase
    定义测试方法名称必须以test开头

    如何执行测试用例
    调用unittest.main()
TestSuite
    测试套件：用来同时运行多个测试用例
        1.实例化测试套件 suite = unittest.TestSuite()
        2.添加用例
            suite.addTest(ClassName("MethodName"))
        3.添加扩展
            suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(ClassName)
            把指定的ClassName类中的测试用例全部添加到测试套件中

        import unittest
        from cal import TestAdd
        from cal import TestSub
        # 实例化TestSuite对象
        suite = unittest.TestSuite()
        # 添加测试用例
        # 方式一：一次添加一个测试用例
        suite.addTest(TestAdd("test_add_01"))
        suite.addTest(TestAdd("test_add_02"))
        # 方式二：一次添加整个测试类
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSub))

TestRunner
    1.实例化
        runner = unittest.TextTestRunner()
    2.执行
        runner.run(suite) # suite为测试套件名称

TestLoader
        用来加载TestCase到TestSuite中，即加载满足条件的测试用例，并把测试用例封装成测试套件。
        使用unittest.TestLoader，通过该类下面的discover()方法自动搜索指定目录下指定开头的.py文件，并将查找到
        的测试用例组装到测试套件。
        suite = unittest.TestLoader().discover(test_dir,pattern='test_*.py')
            自动搜索指定目录下指定开头的.py文件，并将查找到的测试用例组装到测试套件
            test_dir: 为指定的测试用例的目录
            pattern：为查找的.py文件的格式，默认为'test*.py

Fixture

"""