"""
登录接口对象层

封装思想：
将 动态变化的数据，设计到⽅法的参数。
将 固定不变的，直接写成⽅法实现。
将 响应结果，通过返回值传出。

"""


class TpshopLoginApi(object):

    # 发送验证码请求
    @classmethod
    def get_verity(cls,sessin):
        sessin.get(url="http://192.168.42.129/index.php?m=Home&c=User&"
                       "a=verify&r=0.21519623710645064")

    # 登录请求
    @classmethod
    def login(cls,session,login_data):
        resp = session.post(url="http://192.168.42.129/index.php?m=Home&"
                                    "c=User&a=do_login&t=0.7094195931397276",
                            data=login_data)
        return resp
