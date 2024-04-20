def login(username, password,code):
    if code == '8888':
        print('验证码正确')
        if username == 'admin' and password == '123456':
            print('login success')
        else:
            print('username or password wrong login fail')
    else:
        print('code is wrong login fail')