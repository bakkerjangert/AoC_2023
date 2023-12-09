import math
import numpy as np

class Pt2:
    def __init__(self, pos):
        self.start_pos = pos
        self.pos = pos
        self.steps = 0
        self.ends = dict()

    def __repr__(self):
        return f'Ghost at Position "{self.pos}"'

pt2_paths, pt2_finished_steps = [], []

file = 'input.txt'
# file = 'test.txt'
# file = 'tweakers.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

instructions = list(data[0])
LR = {'L': 0, 'R': 1}
maze = dict()

for line in data[2:]:
    pos = line.split(' =')[0]
    if pos[-1] == 'A':
        pt2_paths.append(Pt2(pos))
    goal_L, goal_R = line.split('(')[1].split(',')[0], line.split(', ')[1].split(')')[0]
    maze[pos] = (goal_L, goal_R)
print(pt2_paths)

steps, pos = 0, 'AAA'
while not (len(pt2_paths) == 0 and pos == 'ZZZ'):
    if len(instructions) == 0:
        instructions = list(data[0])
    instruction = instructions.pop(0)
    if pos != 'ZZZ':
        pos = maze[pos][LR[instruction]]
        print(pos)
        steps += 1
    for path in pt2_paths[:]:
        path.pos = maze[path.pos][LR[instruction]]
        path.steps += 1
        if path.pos[-1] == 'Z':
            path.ends[path.pos] = path.steps
            pt2_finished_steps.append(path.steps)
            pt2_paths.remove(path)
print(f'Part 1: {steps}')
print(f'Part 2: {math.lcm(*pt2_finished_steps)}')
