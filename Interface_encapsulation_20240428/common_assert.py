# 封装通用的断言函数
def common_assert(self, resp, status_code, status, msg):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(status, resp.json().get('status'))
    self.assertEqual(msg, resp.json().get('msg'))

