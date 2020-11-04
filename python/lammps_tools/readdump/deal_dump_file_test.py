# -*- coding: utf-8 -*-

'''
处理lammps轨迹文件，假设dump文件中原子信息遵循以下格式，且原子按id排序
id  type  x  y  z
'''

import linecache
import os

# 读取粒子信息
# 通过查看dump文件可知，粒子数量在第4行可知，粒子信息从第10行开始

line_number_1 = 4  # 总粒子数量
line_number_2 = 9  # ITEM: ATOMS id type x y z

atoms_number = int(linecache.getline('dump.test', line_number_1).strip())
Judging_characters = linecache.getline('dump.test', line_number_2).strip()

# print(atoms_number,Judging_characters)
oribt=[]
add_flag = False
step=0
with open('dump.test') as f:
    lines = f.readlines()
    for line in lines:
        atom = {}
        if 'ITEM' in line and Judging_characters not in line:
            add_flag=False
            continue
        elif Judging_characters in line:
            add_flag=True
            step+=1
            continue
        if add_flag:
            arrline=line.strip().split(' ')
            #print(arrline)
            atom['id']=arrline[0]
            atom['type']=arrline[1]
            atom['x']=arrline[2]
            atom['y'] = arrline[3]
            atom['z'] = arrline[4]
            oribt.append(atom)

print(atoms_number,step)
print(oribt[0])
for i in range(step):
    for j in range(atoms_number):
        print(i*atoms_number+j)
print(oribt[step*atoms_number-1])