import numpy as np


def roll_north():
    rows, cols = np.where(grid == 'O')
    boulders = list(zip(rows, cols))
    boulders.sort(key=lambda x: x[0], reverse=False)
    for row, col in boulders:
        while grid[row, col] == 'O' and grid[row - 1, col] == '.':
            grid[row, col], grid[row - 1, col] = '.', 'O'
            row -= 1


def roll_west():
    rows, cols = np.where(grid == 'O')
    boulders = list(zip(rows, cols))
    boulders.sort(key=lambda x: x[1], reverse=False)
    for row, col in boulders:
        while grid[row, col] == 'O' and grid[row, col - 1] == '.':
            grid[row, col], grid[row, col - 1] = '.', 'O'
            col -= 1


def roll_south():
    rows, cols = np.where(grid == 'O')
    boulders = list(zip(rows, cols))
    boulders.sort(key=lambda x: x[0], reverse=True)
    for row, col in boulders:
        while grid[row, col] == 'O' and grid[row + 1, col] == '.':
            grid[row, col], grid[row + 1, col] = '.', 'O'
            row += 1


def roll_east():
    rows, cols = np.where(grid == 'O')
    boulders = list(zip(rows, cols))
    boulders.sort(key=lambda x: x[1], reverse=True)
    for row, col in boulders:
        while grid[row, col] == 'O' and grid[row, col + 1] == '.':
            grid[row, col], grid[row, col + 1] = '.', 'O'
            col += 1


def get_score_pt1():
    rows, cols = np.where(grid[::-1, :] == 'O')
    return sum(rows)


def get_score_pt2(rocks):
    score = 0
    for rock in rocks:
        score += grid.shape[0] - 1 - rock[0]
    return score


file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

grid = np.array(list(map(list, data)))
rw, cl = np.array(['#'] * grid.shape[1]), np.array([['#']] * (grid.shape[0] + 2))
grid = np.vstack((rw, grid, rw))
grid = np.hstack((cl, grid, cl))
org_grid = grid.copy()
pt1, pt2 = 0, 0

roll_north()
pt1 += get_score_pt1()
print(f'Part 1: {pt1}')

goal = 1_000_000_000
grid, rock_layouts, rocks = org_grid.copy(), [], None

while rocks not in rock_layouts:
    rock_layouts.append(rocks)
    roll_north(), roll_west(), roll_south(), roll_east()
    rows, cols = np.where(grid == 'O')
    rocks = tuple(zip(rows, cols))

start_loop = rock_layouts.index(rocks)
delta_loop = len(rock_layouts) - start_loop
goal_index = (goal - start_loop) % delta_loop + start_loop
print(f'Part 2: {get_score_pt2(rock_layouts[goal_index])}')
