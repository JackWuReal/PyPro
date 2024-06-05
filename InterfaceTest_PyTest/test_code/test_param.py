import pytest

# mark.parametrize参数化和数据驱动
"""
场景如果每个测试方法需要不同数据可以直接传入,测试的预期结果也直接传入,
两个不同的参数一一对应输入的数据经过调通执行后结果是否与预期一致

解决:使用mark中的 @pytest.mark.parametrize进行参数化与数据驱动更灵活
"""
@pytest.mark.parametrize("test_input,expected", [("3+5",8),
                                                 ("2-1",1),
                                                 ("7*5",30)])
def test_eval(test_input,expected):
    print(type(test_input))
    assert eval(test_input) == expected


if __name__ == '__main__':
    pytest.main()