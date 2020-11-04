# -*- coding: utf-8 -*-


import linecache
import os


def read_lammps_dump(dumpfile):
    line_number_1 = 4  # Total atoms
    line_number_2 = 9  # ITEM: ATOMS id type x y z
    atoms_number = int(linecache.getline('dump.test', line_number_1).strip())
    Judging_characters = linecache.getline('dump.test', line_number_2).strip()

    oribt = []
    step = 0
    add_flag = False

    with open(dumpfile) as f:
        lines = f.readlines()
        for line in lines:
            atom = {}
            if 'ITEM' in line and Judging_characters not in line:
                add_flag = False
                continue
            elif Judging_characters in line:
                add_flag = True
                step += 1
                continue
            if add_flag:
                arrline = line.strip().split(' ')
                # print(arrline)
                atom['id'] = arrline[0]
                atom['type'] = arrline[1]
                atom['x'] = arrline[2]
                atom['y'] = arrline[3]
                atom['z'] = arrline[4]
                oribt.append(atom)

    return atoms_number, step, oribt


def print_atom(atoms_number,frame,outfile,oribt):
    with open(out_file,'w') as o:
        for i in range(frame):
            for j in range(atoms_number):
                o.write(str(oribt[i*atoms_number+j]['x'])+' '+str(oribt[i*atoms_number+j]['y'])+' '+str(oribt[i*atoms_number+j]['z'])+'\n')




if __name__ == '__main__':
    Deal_file = 'dump.test'
    out_file='fout.txt'
    print('正在读取数据，请稍后')
    atoms_number,frame,oribt=read_lammps_dump(Deal_file)
    print('数据读取已完成')
    print('\n原子总数为{},共{}帧' . format(atoms_number,frame))
    print('\n正在打印坐标信息，请稍后')
    #print(len(oribt),frame,atoms_number)
    print_atom(atoms_number,frame,out_file,oribt)
    print('\n所有处理已完成')