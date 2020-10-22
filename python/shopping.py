# 一个简单的购物系统，包括用户注册、用户登陆、添加商品到购物车中

# sign up 用户注册
def sign_up():
    while True:
        user = {}  # 用户
        is_registered = False  # 判断用户是否要继续注册，默认不继续注册
        username = input('请输入用户名：')
        password = input('请输入密码：')
        repassword = input('请再次输入密码：')
        if password == repassword:
            # 1.检查用户组用户名是否存在重复
            user['username'] = username
            user['password'] = password
            for user_ in users:
                if username == user_['username']:
                    print('用户名重复，请重新输入！')
                    is_registered = True
                    break
            if is_registered:
                is_registered = False
                continue
            # 2.将用户加入到用户组中
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


# 用户登陆操作
def log_in():
    # 1. 用户账号和密码
    username = input('请输入用户名：')
    password = input('请输入密码：')
    # 判断用户名和密码是否正确
    for user in users:
        if username == user['username'] and password == user['password']:
            return True
    else:
        return False


# 购物
def add_shoppingcart(goodsName):
    global is_log_in
    while True:
        if is_log_in:
            # 已经登陆
            if goodsName:
                print('用户成功将{}加入到购物车中'.format(goodsName))
                break
        else:
            # 用户没有进行登陆
            answer = input('用户没有进行登陆，是否要登陆？（yes/no）')
            if 'y' in answer:
                is_log_in = log_in()
            else:
                print('很遗憾，不能添加商品到购物车中')
                break


if __name__ == '__main__':
    is_log_in = False  # 判断用户是否登陆，默认没有登陆
    users = []  # 用户组
    is_newuser = True  # 判断用户是否为新用户,default=True
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
    # 购物
    goodsName = input('请输入你想买的商品：')
    add_shoppingcart(goodsName)
