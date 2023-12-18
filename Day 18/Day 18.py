import numpy as np

file = 'input.txt'
file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()


def add_row_top(grid):
    row = np.array(['.'] * grid.shape[1])
    grid = np.vstack((row, grid))
    return grid


def add_row_bottom(grid):
    row = np.array(['.'] * grid.shape[1])
    grid = np.vstack((grid, row))
    return grid


def add_col_left(grid):
    col = np.array([['.']] * grid.shape[0])
    grid = np.hstack((col, grid))
    return grid


def add_col_right(grid):
    col = np.array([['.']] * grid.shape[0])
    grid = np.hstack((grid, col))
    return grid

grid = np.array([['.']])
xs, ys, x, y = [0], [0], 0, 0
for line in data:
    if line[0] == 'R':
        x += int(line.split()[1])
        while grid.shape[1] <= x:
            grid = add_col_right(grid)
        grid[y, xs[-1]: x + 1] = '#'
        xs.append(x), ys.append(ys[-1])
    elif line[0] == 'D':
        y += int(line.split()[1])
        while grid.shape[0] <= y:
            grid = add_row_bottom(grid)
        grid[ys[-1]: y + 1, x] = '#'
        xs.append(xs[-1]), ys.append(y)
    elif line[0] == 'L':
        x -= int(line.split()[1])
        xs.append(x), ys.append(ys[-1])
        if x < 0:
            for _ in range(x, 1, 1):
                grid = add_col_left(grid)
                xs = [i + 1 for i in xs]
        grid[y, xs[-1]: xs[-2]] = '#'
    elif line[0] == 'U':
        y -= int(line.split()[1])
        xs.append(xs[-1]), ys.append(y)
        if y < 0:
            for _ in range(y, 1, 1):
                grid = add_row_top(grid)
                ys = [i + 1 for i in ys]
        print(ys)
        grid[ys[-1]: ys[-2], xs[-1]] = '#'

for line in grid:
    print(''.join(line))

print(np.count_nonzero(grid == '#'))
