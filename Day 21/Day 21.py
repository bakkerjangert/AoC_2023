import numpy as np

file = 'input.txt'
file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

valids = 0
pos_pt1, pos_pt2 = set(), set()
grid = ['U' * (len(data[0]) + 2), 'D' * (len(data[0]) + 2)]
for i, line in enumerate(data):
    valids += line.count('.')
    if 'S' in line:
        j = line.index('S')
        pos_pt1.add(((j + 1), (i + 1))), pos_pt2.add(((j + 1), (i + 1), 0, 0))
        grid.insert(-1, 'L' + line[: j] + '.' + line[j + 1:] + 'R')
    else:
        grid.insert(-1, 'L' + line + 'R')

for step in range(64):
    prev_pos, pos_pt1 = pos_pt1, set()
    while prev_pos:
        p = prev_pos.pop()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            if grid[p[1] + d[1]][p[0] + d[0]] == '.':
                pos_pt1.add(((p[0] + d[0]), (p[1] + d[1])))
print(f'Part 1: {len(pos_pt1)}')


def print_layout():
    print(f'\nNext Layout')
    for r in range(filled_pt2.shape[0]):
        for c in range(filled_pt2.shape[1]):
            dx, dy = abs(c - x), abs(r - y)
            if filled_pt2[r, c] == 'O':
                print('\033[1m\033[91m' + filled_pt2[r, c], end='')
            elif dx + dy <= step + 1:
                print('\033[1m\033[93m' + filled_pt2[r, c], end='')
            else:
                print('\033[0m' + filled_pt2[r, c], end='')
        print('')



grid_pt2 = np.array(list(map(list, data)))
y, x = np.where(grid_pt2 == 'S')
grid_pt2[y, x] = '.'
y += grid_pt2.shape[0] * 4
x += grid_pt2.shape[1] * 4
grid_pt2 = np.hstack([grid_pt2] * 9)
grid_pt2 = np.vstack([grid_pt2] * 9)

pos = (int(x), int(y),)

pos_pt2 = set()
pos_pt2.add(pos)
print(pos_pt2)
steps = 26501365
for step in range(steps):
    prev_pos, pos_pt2 = pos_pt2, set()
    filled_pt2 = grid_pt2.copy()
    while prev_pos:
        p = prev_pos.pop()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            if grid_pt2[p[1] + d[1], p[0] + d[0]] == '.':
                pos_pt2.add(((p[0] + d[0]), (p[1] + d[1])))
                filled_pt2[p[1] + d[1], p[0] + d[0]] = 'O'
    if step % 10 == 0 and step >= 10:
        print_layout()
        input('\n...\n')
print(f'Part 1: {len(pos_pt1)}')





# x1, x2, y1, y2 = 1, len(grid[0]) - 2, 1, len(grid) - 2
#
# even_uneven = {0: 0, 1: 0}
# prev_pos = set()
# for step in range(steps):
#     if step in (6, 10, 100, 500, 1000, 5000):
#         print(f'At {step} steps --> {len(pos_pt2)}')
#     prev_prev_pos, prev_pos, pos_pt2 = prev_pos, pos_pt2, set()
#     while prev_pos:
#         p = prev_pos.pop()
#         next_node = None
#         for d in (0, 1), (0, -1), (1, 0), (-1, 0):
#             if grid[p[1] + d[1]][p[0] + d[0]] == '.':
#                 next_node = (p[0] + d[0], p[1] + d[1], p[2], p[3])
#             elif grid[p[1] + d[1]][p[0] + d[0]] == 'U':
#                 next_node = (p[0] + d[0], y2, p[2], p[3] - 1)
#             elif grid[p[1] + d[1]][p[0] + d[0]] == 'D':
#                 next_node = (p[0] + d[0], y1, p[2], p[3] + 1)
#             elif grid[p[1] + d[1]][p[0] + d[0]] == 'L':
#                 next_node = (x2, p[1] + d[1], p[2] - 1, p[3])
#             elif grid[p[1] + d[1]][p[0] + d[0]] == 'R':
#                 next_node = (x1, p[1] + d[1], p[2] + 1, p[3])
#             if next_node:
#                 if next_node in prev_prev_pos:
#                     even_uneven[step % 2] += 1
#                 else:
#                     pos_pt2.add(next_node)
# print(f'Part 2: {len(pos_pt2) + even_uneven[steps % 2]}')

