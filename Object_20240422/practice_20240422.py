"""
封装案例
案例一 小明跑步
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}的体重为：{self.weight}'

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


if __name__ == '__main__':
    xm = Person('小明',75)
    xm.run()
    xm.run()
    xm.eat()
    xm.eat()
    xm.run()
    print(xm)
    xmei = Person('⼩美', 45.0)
    print(xmei)
    xmei.run()
    xmei.run()
    print(xmei)
    xmei.eat()
    print(xmei)

"""
案例二  登录
进⼊某 Web 项⽬登录⻚⾯，输⼊⽤户名、密码、验证码之后登录
系统
"""


class LoginPage:
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code

    def __str__(self):
        return f'用户名：{self.username} 密码：{self.password} 验证码：{self.code}'
    #
    def login(self):
        print(f'{self.username} 密码{self.password} 验证码{self.code}登录' )

if __name__ == '__main__':
    user = LoginPage('jack','123456','code')
    user.login()
