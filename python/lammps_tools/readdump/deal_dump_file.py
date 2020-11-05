# -*- coding: utf-8 -*-

'''
dump文件产生命令:
dump        1 all custom 10000 dump.lammpstrj id type x y z
dump_modify 1  sort  id
'''

import linecache
import os


def read_lammps_dump(dumpfile):
    line_number_1 = 4  # Total atoms
    line_number_2 = 9  # ITEM: ATOMS id type x y z
    atoms_number = int(linecache.getline(dumpfile, line_number_1).strip())
    Judging_characters = linecache.getline(dumpfile, line_number_2).strip()

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


# 获得盒子大小
def boxl(dumpfile, atoms_number, frame):
    Box = []
    line_number_1 = 6  # xlo xhi
    line_number_2 = 7  # ylo yhi
    line_number_3 = 8  # zlo zhi
    nline = atoms_number + 9
    for n in range(frame):
        box = {}
        xline = linecache.getline(dumpfile, line_number_1 + n * nline).strip().split(' ')
        yline = linecache.getline(dumpfile, line_number_2 + n * nline).strip().split(' ')
        zline = linecache.getline(dumpfile, line_number_3 + n * nline).strip().split(' ')
        box['xlo'] = float(xline[0])
        box['xhi'] = float(xline[1])
        box['ylo'] = float(yline[0])
        box['yhi'] = float(yline[1])
        box['zlo'] = float(zline[0])
        box['zhi'] = float(zline[1])
        Box.append(box)
        # print(box)
    return Box[frame - 1]  # 返回最后一帧的盒子大小数据


def print_all_frame(atoms_number, frame, outfile, oribt):
    with open(outfile, 'w') as o:
        for i in range(frame):
            for j in range(atoms_number):
                o.write(str(oribt[i * atoms_number + j]['x']) + ' ' + str(oribt[i * atoms_number + j]['y']) + ' ' + str(
                    oribt[i * atoms_number + j]['z']) + '\n')


def print_last_frame(atoms_number, frame, outfile, oribt):
    with open(outfile, 'w') as o:
        for i in range(frame):
            if i < frame - 1:
                continue
            for j in range(atoms_number):
                o.write(str(oribt[i * atoms_number + j]['x']) + ' ' + str(oribt[i * atoms_number + j]['y']) + ' ' + str(
                    oribt[i * atoms_number + j]['z']) + '\n')


if __name__ == '__main__':
    Deal_file = 'dump.test'
    all_frame_file = 'all_frame.txt'
    last_frame_file = 'last_frame.txt'
    print('正在读取数据，请稍后')
    atoms_number, frame, oribt = read_lammps_dump(Deal_file)
    box = boxl(Deal_file, atoms_number, frame)
    print('\n盒子大小为:')
    print('xlo {} xhi {}'.format(box['xlo'], box['xhi']))
    print('ylo {} yhi {}'.format(box['ylo'], box['yhi']))
    print('zlo {} zhi {}'.format(box['zlo'], box['zhi']))
    # print(box)
    print('\n数据读取已完成')
    print('\n原子总数为{},共{}帧'.format(atoms_number, frame))
    print('\n正在打印坐标信息，请稍后')
    # print(len(oribt),frame,atoms_number)
    # print_all_frame(atoms_number, frame,all_frame_file , oribt)
    print_last_frame(atoms_number, frame, last_frame_file, oribt)

    print('\n所有处理已完成')
