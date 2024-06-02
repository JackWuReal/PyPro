import pytest





# module级别夹具
def setup_module(self):
    print("setup_module是在每个测试用例执行前执行吗？")
def teardown_module(self):
    print("teardown_module是在每个测试用例执行前执行吗？")
# function级别夹具 只对函数用例生效（不在类中）
def setup_function(self):
    print("setup_function是在每个function测试用例执行前执行吗？")

def teardown_function(self):
    print("teardown_function是在每个测试用例执行前执行吗？")

def test01():
    print("函数测试test01")

def test02():
    print("函数测试test02")


class Test():
    # class级别夹具 在类创建后执行
    def setup_class(self):
        print("setup_class是在所有测试用例执行前执行吗？")

    def teardown_class(self):
        print("teardown_class是在所有测试用例执行后执行吗？")
    # method级别夹具 在每个测试方法前后执行
    def setup_method(self):
        print("setup_method是在每个测试用例执行前执行吗？")

    def teardown_method(self):
        print("teardown_method是在每个测试用例执行前执行吗？")

    def test02(self):
        print("方法测试测试test02")

    def test03(self):
        print("方法测试测试test03")


if __name__ == '__main__':
    pytest.main(["-vs", "test_setup_teardown.py"])
