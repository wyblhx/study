from tkinter import *

# 编码格式为utf-8
# coding=utf-8

# 设置根窗口
root = Tk()  # 根窗口
# 设置窗口名称
root.title('first gui program')
# 设置窗口出现位置及窗口大小
screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
width = 400  # 设定窗口宽度
height = 400  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
root.geometry("%dx%d+%d+%d" % (width, height, left, top))

'''
# 设置窗口最大/最小尺寸
root.maxsize(600, 600)
root.minsize(200, 200)
'''
# 创建根菜单

root_menu = Menu(root)
root['menu'] = root_menu

# 创建子菜单
tool_menu = Menu(root_menu)
help_menu = Menu(root_menu)

# 子菜单栏
tool_menu.add_command(label='计算器')  # 子菜单栏

# 创建顶级菜单栏，并关联子菜单
root_menu.add_cascade(label='工具', menu=tool_menu)
root_menu.add_cascade(label='帮助', menu=help_menu)
root.mainloop()
