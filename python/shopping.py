# 购物系统


is_sign_in = False
users = []  # 用户组


# sign up 用户注册
def sign_up():
    while True:
        user = {}  # 用户
        is_resignin = False
        username = input('请输入用户名：')
        password = input('请输入密码：')
        repassword = input('请再次输入密码：')
        if password == repassword:
            # 将用户加入到用户组中
            user['username'] = username
            user['password'] = password
            # 检查用户组用户名是否存在重复
            for user_ in users:
                if username == user_['username']:
                    print('用户名重复，请重新输入！')
                    is_resignin = True
                    break
            if is_resignin:
                is_resignin = False
                continue
            users.append(user)
            print('用户注册成功')
            break
        else:
            answer = input('用户密码不一致，是否要重新输入（yes/no）')
            if 'y' in answer:
                continue
            else:
                print('谢谢，欢迎下次注册')
                break


# 用户登录
def sign_in(username, password):
    # 判断用户名和密码是否正确
    for user in users:
        if username == user['username'] and password == user['password']:
            return True


if __name__ == '__main__':
    is_newuser = True
    # 进行至少一次注册操作,可以进行多次注册
    while True:
        if is_newuser:
            sign_up()
            is_newuser = False
        answer = input('是否要再次注册（yes/no）：')
        if 'y' in answer:
            sign_up()
        else:
            break
    # 进行登录操作
    username_ = input('请输入用户名：')
    password_ = input('请输入密码：')
    is_sign_in = sign_in(username_, password_)
    if is_sign_in:
        print('用户登录成功')
