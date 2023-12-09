file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

pt1, pt2 = 0, 0
for line in data:
    row = [list(map(int, line.split()))]
    while True:
        next_delta = []
        stop = True
        for i, j in zip(row[-1][:-1], row[-1][1:]):
            next_delta.append(j - i)
            if next_delta[-1] != 0:
                stop = False
        row.append(next_delta)
        if stop:
            break
    row_solution_pt1, row_solution_pt2 = 0, 0
    for i in row[::-1]:
        row_solution_pt1 += i[-1]
        row_solution_pt2 = i[0] - row_solution_pt2
    pt1 += row_solution_pt1
    pt2 += row_solution_pt2
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
