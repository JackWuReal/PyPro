import pytest

from InterfaceTest_PyTest.caculate.add import *

def test_add():
    assert add(1,2) == 3

def test_minus():
    assert minus(1,2) == 2

if __name__ == '__main__':
    pytest.main()

