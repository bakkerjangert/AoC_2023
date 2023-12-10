file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

grid = list(map(list, data))

directions = {'|': ((0, 1), (0, -1)),
              '-': ((1, 0), (-1, 0)),
              'L': ((1, 0), (0, -1)),
              'J': ((-1, 0), (0, -1)),
              '7': ((-1, 0), (0, 1)),
              'F': ((1, 0), (0, 1))}

path, symbols, prev_step = [], [], None
for i, line in enumerate(grid):
    if 'S' in line:
        x, y = line.index('S'), i
        path.append((x, y))
        symbols.append(grid[y][x])
        if grid[x + 1][y] == '-' or grid[x + 1][y] == '7' or grid[x + 1][y] == 'J':
            path.append((x + 1, y))
            prev_step = (1, 0)
        elif grid[x - 1][y] == '-' or grid[x - 1][y] == 'F' or grid[x - 1][y] == 'L':
            path.append((x - 1, y))
            prev_step = (-1, 0)
        elif grid[x][y + 1] == '|' or grid[x][y + 1] == 'L' or grid[x][y + 1] == 'J':
            path.append((x, y + 1))
            prev_step = (0, 1)
        elif grid[x][y - 1] == '|' or grid[x][y - 1] == 'F' or grid[x][y - 1] == '7':
            path.append((x, y - 1))
            prev_step = (0, -1)
        symbols.append(grid[path[-1][1]][path[-1][0]])
        break

while symbols[-1] != 'S':
    x, y = path[-1]
    char = grid[y][x]
    grid[y][x] = '.' if grid[y][x] != 'S' else 'S'
    for step in directions[char]:
        next_x, next_y = x + step[0], y + step[1]
        if grid[next_y][next_x] == '.':
            continue
        elif grid[next_y][next_x] == 'S' and len(symbols) == 2:
            continue
        path.append((next_x, next_y))
        symbols.append(grid[next_y][next_x])
    # print(symbols)
print(symbols)
print(f'Part 1: {len(path) // 2}')

# Part 2:
# Check for nodes x = 1 to n - 1 and y = 1 to y = n - 1; outer nodes not enclosed
# For each node not in loop coordinates check line x rightward; if intersections with loop is uneven --> inside loop
# intersection = '|' or 'L-- ... --7' or 'F-- ... --J'
grid = list(map(list, data))
grid[path[0][1]][path[0][0]] = '7'  # NOTE: Manual action replacing S!!!
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x, y) not in path:
            grid[y][x] = '.'
    # print(''.join(grid[y]))

pt2 = 0
for x in range(1, len(grid[0]) - 1):
    for y in range(1, len(grid) - 1):
        counter = 0
        if (x, y) in path:
            continue
        if grid[y][:x].count('.') == len(grid[y][:x]) or grid[y][x + 1:].count('.') == len(grid[y][x + 1:]):
            continue
        checker = grid[y][x + 1:]
        for char in '.-':
            while char in checker:
                checker.remove(char)
        while '|' in checker:
            counter += 1
            checker.remove('|')
        checker = [checker[i] + checker[i + 1] for i in range(0, len(checker) - 1, 2)]
        counter += checker.count('L7') + checker.count('FJ')
        if counter % 2 == 1:
            pt2 += 1
print(f'Part 2: {pt2}')
