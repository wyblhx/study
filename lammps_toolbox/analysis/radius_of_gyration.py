'''
This code is to calculate the mean square radius of gyration
Author: Wangyu
Date: 18 Nov 2020.
'''
import linecache


def deal_dump(dumpfile):
    '''
    dump file format:
        id type xu yu zu
    '''
    line_number_1 = 4  # Total atoms
    line_number_2 = 9  # Judging_characters, eg:ITEM: ATOMS id type x y z
    atoms_number = int(linecache.getline(dumpfile, line_number_1).strip())  # 原子总数
    judging_characters = linecache.getline(dumpfile, line_number_2).strip()  # 判断标志

    add_flag = False
    frames = 0
    snaps = []

    with open(dumpfile) as f:
        lines = f.readlines()
        for line in lines:
            atom = {}
            if 'ITEM' in line and judging_characters not in line:
                add_flag = False
                continue
            elif judging_characters in line:
                add_flag = True
                frames += 1
                continue
            if add_flag:
                arrline = line.strip().split(' ')
                atom['id'] = int(arrline[0])
                atom['type'] = int(arrline[1])
                atom['x'] = float(arrline[2])
                atom['y'] = float(arrline[3])
                atom['z'] = float(arrline[4])
                snaps.append(atom)
    del atom

    return snaps, atoms_number, frames


def get_positions(snaps, frame, atoms_number):
    single_step_pos = []

    for n in range(atoms_number):
        pos = {}
        pos['x'] = snaps[frame * atoms_number + n]['x']
        pos['y'] = snaps[frame * atoms_number + n]['y']
        pos['z'] = snaps[frame * atoms_number + n]['z']
        single_step_pos.append(pos)
    del pos

    return single_step_pos


def calc_center_of_mass(single_step_pos):
    '''
    Default quality of all beads is 1.0
    '''
    sumx = 0.0
    sumy = 0.0
    sumz = 0.0
    for pos in single_step_pos:
        sumx += pos['x']
        sumy += pos['y']
        sumz += pos['z']

    cmx = sumx / len(single_step_pos)
    cmy = sumy / len(single_step_pos)
    cmz = sumz / len(single_step_pos)

    return cmx, cmy, cmz


def radius_of_gyration(cmx, cmy, cmz, single_step_pos):
    dis = []
    for pos in single_step_pos:
        r = {}
        r['x'] = pos['x'] - cmx
        r['y'] = pos['y'] - cmy
        r['z'] = pos['z'] - cmz
        dis.append(r)
    del r
    xx, yy, zz = 0.0, 0.0, 0.0
    for r in dis:
        xx += r['x'] * r['x']
        yy += r['y'] * r['y']
        zz += r['z'] * r['z']

    Rg2 = xx + yy + zz
