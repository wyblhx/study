import os

'''
复制文件夹
'''


def copy_dir(source, target):
    filelist = os.listdir(source)
    for file in filelist:
        path = os.path.join(source, file)
        if os.path.isdir(path):
            target_dir = os.path.join(target, file)
            os.mkdir(target_dir)
            #print(target_dir)
            copy_dir(path, target_dir)
        else:
            with open(path, 'rb') as r:
                container = r.read()
                target_path = os.path.join(target, file)
                with open(target_path, 'wb') as w:
                    w.write(container)


dir = os.getcwd()
source = os.path.join(dir, 'copy_test')
target = 'copy_'

target = os.path.join(dir, target)
if not os.path.exists(target):
    os.mkdir(target)
    copy_dir(source, target)
else:
    if not os.path.isdir(target):
        print('ERROR: {} is not a dir'.format(target))
    copy_dir(source, target)
