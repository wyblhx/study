class Hexahedron:
    def __init__(self, a, b, c, alpha, beta, gamma):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma


class Cube(Hexahedron):
    def __init__(self, a, b, c, alpha, beta, gamma):
        super().__init__(a, b, c, alpha, beta, gamma)

    def creat_atoms(self, dis):

        cubes_ = []
        natoms_ = 0

        nx = int(self.a / dis)
        ny = int(self.b / dis)
        nz = int(self.c / dis)

        # 创建坐标信息
        for i in range(nz):
            for j in range(ny):
                for k in range(nx):
                    cube_ = {'id': natoms_ + 1, 'mole': 1, 'type': 1, 'x': k * dis, 'y': j * dis, 'z': i * dis}
                    natoms_ += 1
                    cubes_.append(cube_)

        return cubes_, natoms_


# test
cube = Cube(1.0, 1.0, 1.0, 90.0, 90.0, 90.0)
cubes, natoms = cube.creat_atoms(0.5)
for atom in cubes:
    print(atom)
print(natoms)
