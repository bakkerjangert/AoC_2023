file = 'input.txt'
# file = 'test.txt'
# file = 'aoc-2023-day-18-challenge-3.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

steps, xs, ys, x, y = 0, [0], [0], 0, 0
steps_pt2, xs_pt2, ys_pt2, x_pt2, y_pt2 = 0, [0], [0], 0, 0
for line in data:
    steps += int(line.split()[1])
    if line[0] == 'R':
        x += int(line.split()[1])
        xs.append(x), ys.append(ys[-1])
    elif line[0] == 'L':
        x -= int(line.split()[1])
        xs.append(x), ys.append(ys[-1])
    elif line[0] == 'D':
        y += int(line.split()[1])
        xs.append(xs[-1]), ys.append(y)
    elif line[0] == 'U':
        y -= int(line.split()[1])
        xs.append(xs[-1]), ys.append(y)
    # Part 2
    dist = int(line.split()[2][2:-2], 16)
    steps_pt2 += dist
    if line.split()[2][-2] == '0':
        x_pt2 += dist
        xs_pt2.append(x_pt2), ys_pt2.append(ys_pt2[-1])
    elif line.split()[2][-2] == '2':
        x_pt2 -= dist
        xs_pt2.append(x_pt2), ys_pt2.append(ys_pt2[-1])
    elif line.split()[2][-2] == '1':
        y_pt2 += dist
        xs_pt2.append(xs_pt2[-1]), ys_pt2.append(y_pt2)
    elif line.split()[2][-2] == '3':
        y_pt2 -= dist
        xs_pt2.append(xs_pt2[-1]), ys_pt2.append(y_pt2)

# Part 1 - Straight forward shoe-lace area calculation
SHL = 0
for x, y in zip(xs, ys[1:]):
    SHL += x * y
for x, y in zip(xs[1:], ys):
    SHL -= x * y
print(f'Part 1: {abs(SHL) // 2 + steps // 2 + 1}')

# Part 2
SHL = 0
for x, y in zip(xs_pt2, ys_pt2[1:]):
    SHL += x * y
for x, y in zip(xs_pt2[1:], ys_pt2):
    SHL -= x * y
print(f'Part 2: {abs(SHL) // 2 + steps_pt2 // 2 + 1}')
