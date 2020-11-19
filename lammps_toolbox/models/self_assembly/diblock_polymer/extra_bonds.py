
from models.self_assembly.diblock_polymer import diblock_polymer

number_natoms = diblock_polymer.natoms
number_nbonds = diblock_polymer.nbonds

bonds =diblock_polymer.Bonds

add_bonds = []
chains = 2400
# 键
for chain in range(chains):
    for bond in bonds:
        poly_bond = {}
        poly_bond['id'] = bond['id'] + chain * number_nbonds
        poly_bond['type'] = bond['type']
        poly_bond['n1'] = bond['n1'] + chain * number_natoms
        poly_bond['n2'] = bond['n2'] + chain * number_natoms
        add_bonds.append(poly_bond)

with open('bonds.txt', 'w') as f:
    f.write('Bonds\n')
    f.write('\n')
    for poly_bond in add_bonds:
        f.write(str(poly_bond['id']) + ' ' + str(poly_bond['type']) + ' ' + str(poly_bond['n1']) + ' ' + str(
            poly_bond['n2']) + '\n')




