# -*- coding: UTF-8 -*-

# dump tools
import linecache


class Dump:
    def __init__(self, filename):
        self.filename = filename
        self.atoms_number = 0
        self.frame = 0
        self.judging_characters = None
        self.snaps = []
        self.boxl = []
        # 实例化函数
        self.read_snapshots()
        self.get_boxsize()

    # 读取所有的轨迹
    def read_snapshots(self):
        line_number_1 = 4  # Total atoms
        line_number_2 = 9  # Judging_characters, eg:ITEM: ATOMS id type x y z
        self.atoms_number = int(linecache.getline(self.filename, line_number_1).strip())  # 原子总数
        self.judging_characters = linecache.getline(self.filename, line_number_2).strip()  # 判断标志

        add_flag = False

        with open(self.filename) as f:
            lines = f.readlines()
            for line in lines:
                atom = {}
                if 'ITEM' in line and self.judging_characters not in line:
                    add_flag = False
                    continue
                elif self.judging_characters in line:
                    add_flag = True
                    self.frame += 1
                    continue
                if add_flag:
                    arrline = line.strip().split(' ')
                    atom['id'] = int(arrline[0])
                    atom['type'] = int(arrline[1])
                    atom['x'] = float(arrline[2])
                    atom['y'] = float(arrline[3])
                    atom['z'] = float(arrline[4])
                    self.snaps.append(atom)
        del atom

    def get_one_snapshot(self, frame):
        # print(self.frame,self.atoms_number)
        if self.frame >= frame > 0:
            frame = frame - 1
            for n in range(self.atoms_number):
                print(self.snaps[frame * self.atoms_number + n]['x'], self.snaps[frame * self.atoms_number + n]['y'],
                      self.snaps[frame * self.atoms_number + n]['z'])

    def get_boxsize(self):
        xflag = 6  # xlo xhi
        yflag = 7  # ylo yhi
        zflag = 8  # zlo zhi
        nline = self.atoms_number + 9
        for n in range(self.frame):
            box = {}
            x_bound = linecache.getline(self.filename, xflag + n * nline).strip().split(' ')
            y_bound = linecache.getline(self.filename, yflag + n * nline).strip().split(' ')
            z_bound = linecache.getline(self.filename, zflag + n * nline).strip().split(' ')
            box['xlo'] = x_bound[0]
            box['xhi'] = x_bound[1]
            box['ylo'] = y_bound[0]
            box['yhi'] = y_bound[1]
            box['zlo'] = z_bound[0]
            box['zhi'] = z_bound[1]
            self.boxl.append(box)

        del box
