import numpy as np

# file = 'test.txt'
file = 'input.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

grid = []
for line in data:
    grid.append(list(line))

numbers = '1234567890'
checkers = numbers + '.'

grid = np.array(grid)
rw, cl = np.array(['.'] * grid.shape[0]), np.array([['.']] * (grid.shape[1] + 2))

grid = np.vstack([rw, grid, rw])
grid = np.hstack([cl, grid, cl])

pt1, pt2 = 0, 0
for row in range(1, grid.shape[0] - 1):
    suspect = ''
    part = False
    for col in range(1, grid.shape[1]):
        if grid[row, col] in numbers:
            suspect += grid[row, col]
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if grid[row + dy, col + dx] not in checkers:
                        part = True
        elif suspect:
            if part:
                pt1 += int(suspect)
            suspect = ''
            part = False
print(f'Part 1: {pt1}')


for row in range(1, grid.shape[0] - 1):
    for col in range(1, grid.shape[1] - 1):
        indexes = []
        if grid[row, col] == '*':
            print(grid[row - 1: row + 2, col - 1: col + 2])
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if grid[row + dy, col + dx] in numbers:
                        if dx == -1:
                            indexes.append((row + dy, col + dx))
                        elif grid[row + dy, col + dx - 1] not in numbers:
                            indexes.append((row + dy, col + dx))
            print(indexes)
            if len(indexes) == 2:
                nums = []
                for index in indexes:
                    n_row, n_col = index[0], index[1]
                    n = grid[n_row, n_col]
                    while grid[n_row, n_col - 1] in numbers:
                        n_col -= 1
                        n = grid[n_row, n_col] + n
                    n_col = index[1]
                    while grid[n_row, n_col + 1] in numbers:
                        n_col += 1
                        n = n + grid[n_row, n_col]
                    nums.append(n)
                pt2 += int(nums[0]) * int(nums[1])
print(f'Part 2: {pt2}')
