import os

'''
递归删除文件下的所有文件及目录，如果目标是文件的话，也删除
'''


def delete_dir(target):
    # 判断是否为目录
        if os.path.isdir(target):
            for file in os.listdir(target):
                # os.listdir给出当前文件夹下的所有文件及文件夹
                path = os.path.join(target, file)
                if os.path.isdir(path):
                    delete_dir(path)
                else:
                    os.remove(path)  # 删除文件

            else:
    	        os.rmdir(target)
        else:
            os.remove(target)


dir = os.path.join(os.getcwd(), 'test')
# print(dir)
if os.path.exists(dir):
    delete_dir(dir)
else:
    print('error')


