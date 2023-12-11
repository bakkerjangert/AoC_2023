import numpy as np
file = 'input.txt'
# file = 'test.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

pt1, pt2 = 0, 0
factor_pt2 = 1000_000
grid = np.array(list(map(list, data)))
new_row = np.array(['X'] * grid.shape[1])
for row in range(grid.shape[0] - 1, -1, -1):
    if np.count_nonzero(grid[row, :] == '#') == 0:
        grid[row, :] = new_row
new_col = np.array(['X'] * grid.shape[0])
for col in range(grid.shape[1] - 1, -1, -1):
    if np.count_nonzero(grid[:, col] == '#') == 0:
        grid[:, col] = new_col

rows, cols = np.where(grid == '#')
for i in range(len(rows) - 1):
    for j in range(i + 1, len(rows)):
        row_min, row_max = min(rows[i], rows[j]), max(rows[i], rows[j])
        col_min, col_max = min(cols[i], cols[j]), max(cols[i], cols[j])
        number_x = np.count_nonzero(grid[row_min: row_max, col_min] == 'X') + np.count_nonzero(grid[row_min, col_min: col_max] == 'X')
        pt1 += (row_max - row_min) + (col_max - col_min) + number_x
        pt2 += (row_max - row_min) + (col_max - col_min) + number_x * (factor_pt2 - 1)
print(f'Part 1 : {pt1}')
print(f'Part 2 : {pt2}')
