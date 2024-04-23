import json

from app import base_dir

def login(username, password):
        if username == 'admin' and password == '123456':
            print(f'Login successful for {username}')
            return "登录成功"
        elif username == 'admin' and password != '123456':
            print(f'Login failed for {username},密码不正确')
            return "登录失败"
        elif username != 'admin' and password == '123456':
            print(f'Login failed for {username},账号不正确')
            return "登录失败"
        else:
            print(f'Login failed for {username},账号密码均不正确')
            return "登录失败"
