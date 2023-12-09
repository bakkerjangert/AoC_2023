file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

pt1, pt2 = 0, 0
for line in data:
    row = [list(map(int, line.split()))]
    next_delta = [999]
    while next_delta.count(0) != len(next_delta):
        next_delta = []
        for i, j in zip(row[-1][:-1], row[-1][1:]):
            next_delta.append(j - i)
        row.append(next_delta)
    row_solution_pt1, row_solution_pt2 = 0, 0
    for i in row[::-1]:
        row_solution_pt1 += i[-1]
        row_solution_pt2 = i[0] - row_solution_pt2
    pt1 += row_solution_pt1
    pt2 += row_solution_pt2
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
