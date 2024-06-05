# assert断言

def test_one():
    assert 1 == 1
    assert 2 != 3
    assert "hello" in "hello world"
    age = 35
    assert 20 < age < 80
    assert (1 < 2) == True
    assert {'name': 'linda', 'age': 18} == {'name': 'linda', 'age': 18}


def f():
    return 3


def test_two():
    assert f() == 3


# mark 中的skip 跳过
#
"""
 解 决 ： @pytest.mark.skip 跳 过 这 个 测 试 用 例 ， 可 以 加 条 件 skipif ，
 在 满 足 某 些 条 件 下 才 希 望 通 过 ， 否 则 跳 过 这 个 测 试 。
"""

# mark中的失败xfail


