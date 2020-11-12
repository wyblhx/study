'''
模型：
        B      B      B
        B      B      B
    AAAAAAAAAAAAAAAAAAAAAAAAA
        B      B      B
        B      B      B
'''
import math
import random

number_mainchain = 100  # 主链原子数
number_brachchain = 5  # 支链原子数
grafting_ratio = 0.1  # 接枝率=接枝原子/主链原子

natoms = 0
natomtypes = 2
nbonds = 0
nbondtypes = 3
nangles = 0
nangletypes = 2
mass = 1.0

sigma = 1.0  # 相邻两个聚合物珠子距离，也即聚合物珠子直径

polys = []
mainchains = []
brachchains = []
bonds = []
angles = []

# 生成主链
for n in range(number_mainchain):
    natoms += 1
    mainchain = {'id': natoms, 'mole': 1, 'type': 1, 'x': n * sigma, 'y': 1.0, 'z': 1.0}
    polys.append(mainchain)
    mainchains.append(mainchain)


# 随机化接枝原子（接枝位点）
def ran_gra_atom_generate():
    locus = []
    while True:
        if len(locus) < int(grafting_ratio * number_mainchain):
            ran = random.randint(1, 100)
            if ran not in locus:
                locus.append(ran)
        else:
            break
    locus = sorted(locus)
    for n in range(len(locus)):
        if n > 0 and locus[n] < locus[n - 1] + 2:
            locus[n] += 5
    return locus


def gra_atom_generate():
    locus = []
    ran = random.randint(1, int(grafting_ratio * number_mainchain))
    for n in range(int(grafting_ratio * number_mainchain)):
        locus.append(ran + n * int(grafting_ratio * number_mainchain))
    return locus


locus = gra_atom_generate()
# print(locus)
# 创建支链
for grafting_atom in locus:
    for mainchain in mainchains:
        if mainchain['id'] == grafting_atom:
            for n in range(number_brachchain):
                natoms += 1
                brachchain = {}
                brachchain['id'] = natoms
                brachchain['mole'] = 2
                brachchain['type'] = 2
                brachchain['x'] = mainchain['x']
                brachchain['y'] = mainchain['y'] + (n + 1) * sigma
                brachchain['z'] = mainchain['z']
                polys.append(brachchain)
                brachchains.append(brachchain)

for grafting_atom in locus:
    for mainchain in mainchains:
        if mainchain['id'] == grafting_atom:
            for n in range(number_brachchain):
                natoms += 1
                brachchain = {}
                brachchain['id'] = natoms
                brachchain['mole'] = 2
                brachchain['type'] = 2
                brachchain['x'] = mainchain['x']
                brachchain['y'] = mainchain['y'] - (n + 1) * sigma
                brachchain['z'] = mainchain['z']
                polys.append(brachchain)
                brachchains.append(brachchain)
# print(natoms)

# 相关键角信息的生成

'''
1.Bond 
bond_id bond_type n1 n2
1).主链原子的键
2).支链原子的键
3).主链原子与支链原子之间构成的键
'''

# 1）主链原子的键
for n in range(len(mainchains) - 1):
    bond = {}
    bond['id'] = nbonds + 1
    bond['type'] = 1
    bond['n1'] = mainchains[n]['id']
    bond['n2'] = mainchains[n + 1]['id']
    nbonds += 1
    bonds.append(bond)

# 2)支链原子的键
for n in range(len(brachchains) - 1):
    if math.fabs(brachchains[n + 1]['y'] - brachchains[n]['y']) == sigma:
        bond = {}
        bond['id'] = nbonds + 1
        bond['type'] = 2
        bond['n1'] = brachchains[n]['id']
        bond['n2'] = brachchains[n + 1]['id']
        nbonds += 1
        bonds.append(bond)

# 3) 主链原子与支链原子之间构成的键
for brachchain_ in brachchains:
    for mainchain_ in mainchains:
        if math.fabs(brachchain_['y'] - mainchain_['y']) == sigma and brachchain_['x'] == mainchain_['x'] and \
                brachchain_['z'] == mainchain_['z']:
            bond = {}
            bond['id'] = nbonds + 1
            bond['type'] = 3
            bond['n1'] = mainchain_['id']
            bond['n2'] = brachchain_['id']
            bonds.append(bond)
            nbonds += 1
'''
2.Angle
angle_id angle_type n1 n2 n3
1).主链原子的角
2).支链原子的角
'''
# 1).主链原子的角
for n in range(len(mainchains) - 2):
    angle = {}
    angle['id'] = nangles + 1
    angle['type'] = 1
    angle['n1'] = mainchains[n]['id']
    angle['n2'] = mainchains[n + 1]['id']
    angle['n3'] = mainchains[n + 2]['id']
    nangles += 1
    angles.append(angle)

# 2).支链原子的角
for n in range(len(brachchains) - 2):
    if math.fabs(brachchains[n + 1]['y'] - brachchains[n]['y']) == sigma and math.fabs(
            brachchains[n + 2]['y'] - brachchains[n + 1]['y']) == sigma:
        angle = {}
        angle['id'] = nangles + 1
        angle['type'] = 2
        angle['n1'] = brachchains[n]['id']
        angle['n2'] = brachchains[n + 1]['id']
        angle['n3'] = brachchains[n + 2]['id']
        nangles += 1
        angles.append(angle)

# 打印文件

with open('poly.data', 'w') as f:
    f.write("LAMMPS data file. CGCMM style. atom_style full generated by wangyu\n")
    f.write('\n')

    f.write(str(natoms) + ' atoms\n')
    f.write(str(natomtypes) + ' atom types' + '\n')
    f.write(str(nbonds) + ' bonds\n')
    f.write(str(nbondtypes) + ' bond types' + '\n')
    f.write(str(nangles) + ' angles\n')
    f.write(str(nangletypes) + ' angle types' + '\n')
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

    f.write('Angles\n')
    f.write('\n')
    for poly_angle in angles:
        f.write(str(poly_angle['id']) + ' ' + str(poly_angle['type']) + ' ' + str(poly_angle['n1']) + ' ' + str(
            poly_angle['n2']) + ' ' + str(poly_angle['n3']) + '\n')
