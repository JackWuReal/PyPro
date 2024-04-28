import unittest
import requests

from tpshop_login_api import TpshopLoginApi
from parameterized import parameterized
from read_data import read_json_data
from common_assert import common_assert

"""
参数化步骤

1. 导包 from parameterized import parameterized
2. 在 通⽤测试⽅法，上⼀⾏，添加 @parameterized.expand()
3. 给 expand() 传⼊ [(),(),()]（调⽤ 转换 [{},{},{}] --> [(),(),()] 的函数）
4. 修改 通⽤测试⽅法，添加形参，个数、顺序，与 [{},{},{}] 中 { } 内的所有 key 完全⼀⼀对应。
5. 在 通⽤测试⽅法内，使⽤形参。
"""
"""
登录接口测试用例层
"""

class TestTpshopLogin(unittest.TestCase):
    # 添加类属性
    session = None

    @classmethod
    def setUpClass(cls) -> None:  # 在类中所有测试方法执行之前，自动执行一次
        cls.session = requests.Session()

    def setUp(self) -> None:  # 在每个测试方法执行之前，自动执行一次
        # 调用自己封装的接口获取验证码
        TpshopLoginApi.get_verity(self.session)

    # 数据参数化测试tpshop 登录
    @parameterized.expand(read_json_data())
    def test_tp_login(self, req_body, status_code, status, msg):
        resp = TpshopLoginApi.login(self.session, req_body)
        common_assert(self, resp, status_code, status, msg)

