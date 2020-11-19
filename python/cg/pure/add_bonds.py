from pure import poly

number_natoms = poly.natoms
number_nbonds = poly.nbonds

bonds = poly.bonds

add_bonds = []
chains = 100

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

chains_ = 150
Nm = 10

def add_extra_bonds():
    ntotal_atoms = chains * number_natoms
    ntotal_bonds = chains * number_nbonds

    extra_bonds = []

    for n1 in range(chains_):
        for n2 in range(Nm - 1):
            bond = {}
            bond['id'] = ntotal_bonds + 1
            bond['type'] = 2
            bond['n1'] = ntotal_atoms + n1 * Nm + n2 + 1
            bond['n2'] = ntotal_atoms + n1 * Nm + n2 + 2
            ntotal_bonds += 1
            extra_bonds.append(bond)

        del bond

        with open('extra_bonds.txt', 'w') as f:
            for bond in extra_bonds:
                f.write(str(bond['id']) + ' ' + str(bond['type']) + ' ' + str(bond['n1']) + ' ' + str(
                    bond['n2']) + '\n')


def add_extra_angles():
    ntotal_atoms = chains * number_natoms
    nangles = 0
    extra_angles = []

    for n1 in range(chains_):
        for n2 in range(Nm - 2):
            angle = {}
            angle['id'] = nangles + 1
            angle['type'] = 1
            angle['n1'] = ntotal_atoms + n1 * Nm + n2 + 1
            angle['n2'] = ntotal_atoms + n1 * Nm + n2 + 2
            angle['n3'] = ntotal_atoms + n1 * Nm + n2 + 3
            nangles += 1
            extra_angles.append(angle)

    del angle

    with open('extra_angles.txt', 'w') as f:
            for angle in extra_angles:
                f.write(str(angle['id']) + ' ' + str(angle['type']) + ' ' + str(angle['n1']) + ' ' + str(
                    angle['n2']) +' '+ str(angle['n3']) +'\n')


add_extra_bonds()
add_extra_angles()
