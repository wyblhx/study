import os

'''
递归删除文件下的所有文件及目录
'''


def delete_dir(target):
    # 判断是否为目录
    if os.path.exists(target):
        # os.remove(target)
        flielist = os.listdir(target)
        for file in flielist:
            # os.listdir给出当前文件夹下的所有文件及文件夹
            path = os.path.join(target, file)
            if os.path.isdir(path):
                delete_dir(path)
            else:
                os.remove(path)  # 删除文件

        os.rmdir(target)  # 删除空目录
    # os.rmdir(target)


dir = os.path.join(os.getcwd(), 'test')
# print(dir)
delete_dir(dir)
