import numpy as np
from copy import deepcopy

file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

xmax, ymax, zmax = 0, 0, 0
cubes = []
for row in data:
    row = row.replace('~', ',')
    n = list(map(int, row.split(',')))
    cubes.append([[min(n[0], n[3]), min(n[1], n[4]), min(n[2], n[5])], [max(n[0], n[3]), max(n[1], n[4]), max(n[2], n[5])]])
    xmax, ymax, zmax = max(cubes[-1][1][0], xmax), max(cubes[-1][1][1], ymax), max(cubes[-1][1][2], zmax)

grid = np.array([[['.'] * (xmax + 1)] * (ymax + 1)] * (zmax + 2))  # zmax + 2 to add additional empty roof layer
grid[0, :, :] = '#'  # add bottom

cubes.sort(key=lambda z: z[0][2])
for cube in cubes:
    grid[cube[0][2]: cube[1][2] + 1, cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] = '#'


drops = 999
while drops > 0:
    drops = 0
    for cube in cubes:
        while np.count_nonzero(grid[cube[0][2] - 1, cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] == '#') == 0:
            # drop down
            # print(f'{cube} --> ', end='')
            drops += 1
            grid[cube[0][2] - 1, cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] = '#'
            grid[cube[1][2], cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] = '.'
            cube[0][2] -= 1
            cube[1][2] -= 1
            # print(cube)
    cubes.sort(key=lambda z: z[0][2])


def falling(grid, cubes):
    drops, falling_cubes = 999, set()
    while drops > 0:
        drops = 0
        for i, cube in enumerate(cubes):
            while np.count_nonzero(grid[cube[0][2] - 1, cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] == '#') == 0:
                falling_cubes.add(i)
                # drop down
                drops += 1
                grid[cube[0][2] - 1, cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] = '#'
                grid[cube[1][2], cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] = '.'
                cube[0][2] -= 1
                cube[1][2] -= 1
    return falling_cubes


pt1, pt2 = 0, 0
for i, cube in enumerate(cubes):
    sub_grid = grid.copy()
    sub_grid[cube[0][2]: cube[1][2] + 1, cube[0][1]: cube[1][1] + 1, cube[0][0]: cube[1][0] + 1] = '.'
    left_over_cubes = deepcopy(cubes[:i] + cubes[i + 1:])
    falling_cubes = falling(sub_grid, left_over_cubes)
    if len(falling_cubes) == 0:
        pt1 += 1
    else:
        pt2 += len(falling_cubes)
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
