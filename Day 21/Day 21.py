import numpy as np

file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

valids = 0
start_pos, pos_pt1, pos_pt2 = None, set(), set()
grid = []
for i, line in enumerate(data):
    valids += line.count('.')
    if 'S' in line:
        j = line.index('S')
        start_pos = (j, i)
        pos_pt1.add((j, i)), pos_pt2.add((j, i))
        grid.append(line[: j] + '.' + line[j + 1:])
    else:
        grid.append(line)

# Diamond uneven has O on middle of outer edges
diamond_even, diamond_uneven, square_even, square_uneven = None, None, None, None
for step in range(150):
    prev_pos, pos_pt1 = pos_pt1, set()
    while prev_pos:
        p = prev_pos.pop()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            if not (0 <= p[0] + d[0] < len(grid[0])) or not (0 <= p[1] + d[1] < len(grid)):
                continue
            if grid[p[1] + d[1]][p[0] + d[0]] == '.':
                pos_pt1.add(((p[0] + d[0]), (p[1] + d[1])))
    if step == 63:
        diamond_even = len(pos_pt1)
    if step == 64:
        diamond_uneven = len(pos_pt1)
    if step == 147:
        square_even = len(pos_pt1)
    if step == 148:
        square_uneven = len(pos_pt1)

diamond_uneven = len(pos_pt1)
print(f'Part 1: {diamond_even}')

grid = np.array(list(map(list, data)))
grid = np.where(grid == 'S', '.', grid)

n = 5

grid = np.vstack((grid,) * n)
grid = np.hstack((grid,) * n)
start = grid.shape[0] // 2
grid[start, start] = 'O'
steps = grid.shape[0] // 2
for step in range(steps):
    y, x = np.where(grid == 'O')
    prev_grid = grid.copy()
    for x, y in zip(x, y):
        grid[y, x] = '.'
        for d in (0, 1), (1, 0), (0, -1), (-1, 0):
            if prev_grid[y + d[1], x + d[0]] != '#':
                grid[y + d[1], x + d[0]] = 'O'

# for j, row in enumerate(grid):
#     if j % len(data) == 0:
#         print('')
#     line = ''.join(row)
#     line = [line[i:i + len(line) // n] for i in range(0, len(line), len(line) // n)]
#     print(' '.join(line))

# Total shape is a large diamond. Cut it up in base squares results in 13 shapes to be analyzed and combined
#        ^
#       / \
#      /   \
#     /     \
#     \     /
#      \   /
#       \ /
#        v
#
# Shapes  A    B    C    D    E    F    G   H   I    J    K    L    M    N
# Shapes +-+  /-+  +-+  +-\  +-+  +/        \+       ^   +-+   -+  +-   +-+
#        | |  | |  | |  | |  | |  /     /    \  \   | |  | |  < |  | >  | |
#        +-+  +-+  +-/  +-+  \-+       /+       +\  +-+   v    -+  +-   +-+
# shape = 131 x 131; sloped edges from 1 - 65 or 65 to 131
# Most outer tip is reached (O) making most outer squares (J to M) uneven
# That makes the filler triangles (F to I) even and trapezoids (B to E) uneven
# For the full square we alternate between uneven (A) and even (N)

sub_size = grid.shape[0] // n
squares, factors = dict(), dict()

squares['A'] = np.count_nonzero(grid[2 * sub_size: 3 * sub_size, 2 * sub_size: 3 * sub_size] == 'O')
squares['B'] = np.count_nonzero(grid[1 * sub_size: 2 * sub_size, 1 * sub_size: 2 * sub_size] == 'O')
squares['C'] = np.count_nonzero(grid[3 * sub_size: 4 * sub_size, 3 * sub_size: 4 * sub_size] == 'O')
squares['D'] = np.count_nonzero(grid[1 * sub_size: 2 * sub_size, 3 * sub_size: 4 * sub_size] == 'O')
squares['E'] = np.count_nonzero(grid[3 * sub_size: 4 * sub_size, 1 * sub_size: 2 * sub_size] == 'O')
squares['F'] = np.count_nonzero(grid[4 * sub_size: 5 * sub_size, 3 * sub_size: 4 * sub_size] == 'O')
squares['G'] = np.count_nonzero(grid[0 * sub_size: 1 * sub_size, 1 * sub_size: 2 * sub_size] == 'O')
squares['H'] = np.count_nonzero(grid[4 * sub_size: 5 * sub_size, 1 * sub_size: 2 * sub_size] == 'O')
squares['I'] = np.count_nonzero(grid[0 * sub_size: 1 * sub_size, 3 * sub_size: 4 * sub_size] == 'O')
squares['J'] = np.count_nonzero(grid[0 * sub_size: 1 * sub_size, 2 * sub_size: 3 * sub_size] == 'O')
squares['K'] = np.count_nonzero(grid[4 * sub_size: 5 * sub_size, 2 * sub_size: 3 * sub_size] == 'O')
squares['L'] = np.count_nonzero(grid[2 * sub_size: 3 * sub_size, 0 * sub_size: 1 * sub_size] == 'O')
squares['M'] = np.count_nonzero(grid[2 * sub_size: 3 * sub_size, 4 * sub_size: 5 * sub_size] == 'O')
squares['N'] = np.count_nonzero(grid[2 * sub_size: 3 * sub_size, 1 * sub_size: 2 * sub_size] == 'O')

steps = 26501365
squares_up = (steps - len(data) // 2) // len(data) + 1  # including center square

factors['A'] = (squares_up - 2) ** 2 if squares_up % 2 == 1 else (squares_up - 1) ** 2
for sqr in 'BCDE':
    factors[sqr] = squares_up - 2
for sqr in 'FGHI':
    factors[sqr] = squares_up - 1
for sqr in 'JKLM':
    factors[sqr] = 1
factors['N'] = (squares_up - 1) ** 2 if squares_up % 2 == 1 else (squares_up - 2) ** 2

pt2 = 0
for sqr in 'ABCDEFGHIJKLMN':
    pt2 += squares[sqr] * factors[sqr]
print(f'Part 2: {pt2}')
