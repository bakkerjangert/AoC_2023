file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

instructions = dict()

for line in data[:data.index('')]:
    par = line.split('{')[0]
    instructions[par] = dict()
    for i in line[line.index('{') + 1: line.index('}')].split(','):
        if ':' in i:
            instructions[par][i.split(':')[0]] = i.split(':')[1]
        else:
            instructions[par]['other'] = i

indexes = {'x': 0, 'm': 1, 'a': 2, 's': 3, 'o': None}
items, accepted, rejected = [], [], []


for line in data[data.index('') + 1:]:
     items.append(tuple(line[1:-1].split(',')) + ('in',))

while items:
    item = items.pop(0)
    goal = None
    for instruction in instructions[item[-1]]:
        if instruction == 'other':
            goal = instructions[item[-1]][instruction]
        else:
            val = item[indexes[instruction[0]]][2:]
            if eval(val + instruction[1:]):
                goal = instructions[item[-1]][instruction]
                break
    if goal == 'A':
        accepted.append(item[:-1])
    elif goal == 'R':
        rejected.append(item[:-1])
    else:
        items.append(item[:-1] + (goal,))

pt1 = 0
for item in accepted:
    for part in item:
        pt1 += int(part[2:])
print(f'Part 1: {pt1}')

ranges = [[('x=1', 'x=4000'), ('m=1', 'm=4000'), ('a=1', 'a=4000'), ('s=1', 's=4000'), 'in']]
accepted = []

while ranges:
    rng = ranges.pop(0)
    for instruction in instructions[rng[-1]]:
        goal, index = instructions[rng[-1]][instruction], indexes[instruction[0]]
        if instruction == 'other':
            if goal == 'A':
                accepted.append(rng[:-1])
            elif goal == 'R':
                pass
            else:
                ranges.append(rng[:-1] + [goal, ])
        else:
            val_min, val_max = rng[index]
            val_min, val_max = int(val_min[2:]), int(val_max[2:])
            if val_min < int(instruction[2:]) < val_max:  # KLEINER OF GELIJK?
                if instruction[1] == '<':
                    valid = (instruction[0] + '=' + str(val_min), instruction[0] + '=' + str(int(instruction[2:]) - 1))
                    invalid = (instruction[0] + '=' + str(int(instruction[2:])), instruction[0] + '=' + str(val_max))
                elif instruction[1] == '>':
                    invalid = (instruction[0] + '=' + str(val_min), instruction[0] + '=' + str(int(instruction[2:])))
                    valid = (instruction[0] + '=' + str(int(instruction[2:]) + 1), instruction[0] + '=' + str(val_max))
                valid_rng, invalid_rng = rng[: index] + [valid] + rng[index + 1:], rng[: index] + [invalid] + rng[index + 1:]
                if goal == 'A':
                    accepted.append(valid_rng[:-1])
                elif goal == 'R':
                    pass
                else:
                    ranges.append(valid_rng[:-1] + [goal, ])
                rng = invalid_rng

            elif val_min == int(instruction[2:]):
                if instruction[1] == '>':
                    valid = (instruction[0] + '=' + str(val_min + 1), instruction[0] + '=' + val_max)
                    invalid = (instruction[0] + '=' + str(val_min), instruction[0] + '=' + str(val_min))
                    valid_rng, invalid_rng = rng[: index] + [valid] + rng[index + 1:], rng[: index] + [invalid] + rng[index + 1:]
                    if goal == 'A':
                        accepted.append(valid_rng[:-1])
                    elif goal == 'R':
                        pass
                    else:
                        ranges.append(valid_rng[:-1] + [goal, ])
                    rng = invalid_rng

            elif val_max == int(instruction[2:]):
                if instruction[1] == '<':
                    valid = (instruction[0] + '=' + str(val_min), instruction[0] + '=' + val_max - 1)
                    invalid = (instruction[0] + '=' + str(val_max), instruction[0] + '=' + str(val_max))
                    valid_rng, invalid_rng = rng[: index] + [valid] + rng[index + 1:], rng[: index] + [invalid] + rng[index + 1:]
                    if goal == 'A':
                        accepted.append(valid_rng[:-1])
                    elif goal == 'R':
                        pass
                    else:
                        ranges.append(valid_rng[:-1] + [goal, ])
                    rng = invalid_rng

            elif val_min > int(instruction[2:]) and instruction[1] == '>':
                if goal == 'A':
                    accepted.append(rng[:-1])
                elif goal == 'R':
                    pass
                else:
                    ranges.append(rng[:-1] + [goal, ])
                    break

            elif val_max < int(instruction[2:]) and instruction[1] == '>':
                if goal == 'A':
                    accepted.append(rng[:-1])
                elif goal == 'R':
                    pass
                else:
                    ranges.append(rng[:-1] + [goal, ])
                    break

pt2 = 0
for line in accepted:
    val = 1
    for part in line:
        val *= (int(part[1][2:]) - int(part[0][2:]) + 1)
    pt2 += val
print(f'Part 2: {pt2}')
