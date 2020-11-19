'''
模型：
    AAAAAAAAAAAAAAAAAAAAAAAAA
'''

import math
import random

number_mainchain = 10  # 主链原子数

natoms = 0
natomtypes = 1
nbonds = 0
nbondtypes = 1
'''
nangles = 0
nangletypes = 1
'''
mass = 1.0

sigma = 1.0  # 相邻两个聚合物珠子距离，也即聚合物珠子直径

polys = []
bonds = []

# 生成主链
for n in range(number_mainchain):
    natoms += 1
    mainchain = {'id': natoms, 'mole': 1, 'type': 1, 'x': n * sigma, 'y': 1.0, 'z': 1.0}
    polys.append(mainchain)


# 相关键角信息的生成

for n in range(len(polys) - 1):
    bond = {}
    bond['id'] = nbonds + 1
    bond['type'] = 1
    bond['n1'] = polys[n]['id']
    bond['n2'] = polys[n + 1]['id']
    nbonds += 1
    bonds.append(bond)

# 打印文件

with open('poly.data', 'w') as f:
    f.write("LAMMPS data file. CGCMM style. atom_style full generated by wangyu\n")
    f.write('\n')

    f.write(str(natoms) + ' atoms\n')
    f.write(str(natomtypes) + ' atom types' + '\n')
    f.write(str(nbonds) + ' bonds\n')
    f.write(str(nbondtypes) + ' bond types' + '\n')
    f.write('\n')

    f.write('0.0' + ' ' + str(number_mainchain * sigma) + ' ' + 'xlo xhi\n')
    f.write('0.0' + ' ' + str(number_mainchain * sigma) + ' ' + 'ylo yhi\n')
    f.write('0.0' + ' ' + str(number_mainchain * sigma) + ' ' + 'zlo zhi\n')
    f.write('\n')

    f.write('Masses\n')
    f.write('\n')
    for n in range(natomtypes):
        f.write(str(n + 1) + ' ' + str(mass) + '\n')
    f.write('\n')

    f.write('Atoms # molecular\n')
    f.write('\n')
    for poly in polys:
        f.write(str(poly['id']) + ' ' + str(poly['mole']) + ' ' + str(poly['type']) + ' ' + str(poly['x']) + ' ' + str(
            poly['y']) + ' ' + str(poly['z']) + '\n')
    f.write('\n')

    f.write('Bonds\n')
    f.write('\n')
    for poly_bond in bonds:
        f.write(str(poly_bond['id']) + ' ' + str(poly_bond['type']) + ' ' + str(poly_bond['n1']) + ' ' + str(
            poly_bond['n2']) + '\n')
    f.write('\n')