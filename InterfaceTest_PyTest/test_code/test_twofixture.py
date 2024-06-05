import pytest


@pytest.fixture()
def open_brower():
    print('open_brower')


# @pytest.fixture(autouse=True) #每条用例自动使用
@pytest.fixture()
def login_r(open_brower):
    print('login')


def test_soso():
    print('case3333')


# @pytest.mark.usefixtures('login_r')
# def test_cart(login_r):
#     print('case4')
@pytest.mark.usefixtures('login_r')
def test_cart():
     print('case4')

if __name__ == '__main__':
    pytest.main()
