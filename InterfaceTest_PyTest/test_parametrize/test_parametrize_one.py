import pytest

# @pytest.mark.parametrize("name", ['a', 'b', 'c'])
# def test_parametrize(name):
#     print("i am :"+name)
    # assert name == "a"

@pytest.mark.parametrize("name,age", [('a', '1'), ("b","2")])
def test_parametrize_two(name,age):
    print("i am :"+name+"age:"+age)
    # assert name == "a"