file = 'input.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

max_cubes = {'green': 13, 'red': 12, 'blue': 14}
impossible_IDs = set()
total_ID_score = 0
pt2 = 0
for line in data:
    ID = int(line.split(':')[0].split(' ')[1])
    total_ID_score += ID
    pulls = line.split(': ')[1]
    pulls = pulls.split('; ')
    max_values = {'red': 0, 'green': 0, 'blue': 0}
    for pull in pulls:
        cubes = pull.split(', ')
        for cube in cubes:
            color = cube.split(' ')[1]
            n = int(cube.split(' ')[0])
            max_values[color] = max(max_values[color], n)
            if n > max_cubes[color]:
                impossible_IDs.add(ID)
    power = 1
    for item in max_values.values():
        power *= item
    pt2 += power
print(f'Part 1: {total_ID_score - sum(impossible_IDs)}')
print(f'Part 2: {pt2}')
