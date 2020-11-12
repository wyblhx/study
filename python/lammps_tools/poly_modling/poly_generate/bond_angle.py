import single_chain

'''
注意 single_chain.py文件要与bond_angle.py放在同一目录下
执行顺序
1.single_chain.py生成单条分子链的信息
2.VMD转换data文件生成pdb文件 
topo readlammpsdata data文件
3.packmol软件批量生成（只包含坐标信息）
4.VMD转换pdb文件生成data文件
1）拖入pdb文件到vmd软件中
2）利用命令清楚掉vmd自动添加的键角信息 topo clearbonds
3）生成data文件 topo writelammpsdata data文件 lammps原子种类 eg:topo writelammpsdata test.data molecular
5.调用bond_angle.py生成批量生成的键角信息加入到data文件中

'''
single_number_natoms = single_chain.natoms  # 单链上的原子数
single_number_nbonds = single_chain.nbonds  # 单链上的键数
single_number_nangles = single_chain.nangles  # 单链上的角数

bonds = single_chain.bonds
angles = single_chain.angles
'''
a test for module

for bond in bonds:
    print(bond)
'''

poly_bonds = []
poly_angles = []

nchains = 30  # 链数

# 键
for nchain in range(nchains):
    for bond in bonds:
        poly_bond = {}
        poly_bond['id'] = bond['id'] + nchain * single_number_nbonds
        poly_bond['type'] = bond['type']
        poly_bond['n1'] = bond['n1'] + nchain * single_number_natoms
        poly_bond['n2'] = bond['n2'] + nchain * single_number_natoms
        poly_bonds.append(poly_bond)

# 角
for nchain in range(nchains):
    for angle in angles:
        poly_angle = {}
        poly_angle['id'] = angle['id'] + nchain * single_number_nangles
        poly_angle['type'] = angle['type']
        poly_angle['n1'] = angle['n1'] + nchain * single_number_natoms
        poly_angle['n2'] = angle['n2'] + nchain * single_number_natoms
        poly_angle['n3'] = angle['n3'] + nchain * single_number_natoms
        poly_angles.append(poly_angle)

print(len(poly_bonds), len(poly_angles))
del poly_bond, poly_angle

# 打印
with open('bond_angle.txt', 'w') as f:
    f.write('Bonds\n')
    f.write('\n')
    for poly_bond in poly_bonds:
        f.write(str(poly_bond['id']) + ' ' + str(poly_bond['type']) + ' ' + str(poly_bond['n1']) + ' ' + str(
            poly_bond['n2']) + '\n')
    f.write('\n')

    f.write('Angles\n')
    f.write('\n')
    for poly_angle in poly_angles:
        f.write(str(poly_angle['id']) + ' ' + str(poly_angle['type']) + ' ' + str(poly_angle['n1']) + ' ' + str(
            poly_angle['n2']) + ' ' + str(poly_angle['n3']) + '\n')
