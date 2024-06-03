import pytest

@pytest.fixture()
def login():
    print("login to the system first--conftest")
    # yield
    # print("login out the system second--conftest")
def test_cart(login):
    print("test the cart")


def test_search():
    print("test the search")


def test_pay(login):
    print("test the pay")

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_fixture.py'])