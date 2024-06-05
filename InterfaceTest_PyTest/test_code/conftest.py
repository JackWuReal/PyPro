import pytest

# 层与层之间数据共享
@pytest.fixture(scope='session') # 将覆盖范围扩展至整个session仅登录一次让后 登出一次
def login():
    print("login to the system first--conftest")
    yield
    print("login out the system second--conftest")