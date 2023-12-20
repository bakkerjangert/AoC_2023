import math
from copy import deepcopy
file = 'input.txt'
# file = 'test2.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()


class Button:
    def __init__(self):
        self.name, self.goals = 'Button', ['broadcaster']
        self.pulse = 'low'
        self._type = 'Button'

    def push(self):
        for goal in self.goals:
            waiting_row.append(goal)
            # print(f'{self.name} --> {self.pulse} --> {goal}')
            modules[goal].receive((self.pulse, self.name))
            lows[0] += 1


class FlipFlop:
    def __init__(self, name, goals, state=False):
        self.name, self.goals, self.state = name, goals, state
        self.pulses = []
        self._type = 'FlipFlop'

    def cast(self):
        pulse, sender = self.pulses.pop(0)
        if pulse == 'low':
            self.state = not self.state
            for goal in self.goals:
                waiting_row.append(goal)
                if self.state:
                    # print(f'{self.name} --> {"high"} --> {goal}')
                    modules[goal].receive(('high', self.name))
                    highs[0] += 1
                else:
                    # print(f'{self.name} --> {"low"} --> {goal}')
                    modules[goal].receive(('low', self.name))
                    lows[0] += 1
        else:
            pass

    def receive(self, pulse):
        self.pulses.append(pulse)


class Conjunction:
    def __init__(self, name, goals):
        self.name, self.goals = name, goals
        self.pulses, self.memory = [], dict()
        self._type = 'Conjunction'

    def cast(self):
        pulse, sender = self.pulses.pop(0)
        self.memory[sender] = pulse
        pulse = 'low' if list(self.memory.values()).count('high') == len(self.memory) else 'high'
        for goal in self.goals:
            # print(f'{self.name} --> {pulse} --> {goal}')
            modules[goal].receive((pulse, self.name))
            waiting_row.append(goal)
            if pulse == 'low':
                lows[0] += 1
            else:
                highs[0] += 1

    def all_low(self):
        return True if list(self.memory.values()).count('low') == len(self.memory) else False

    def receive(self, pulse):
        self.pulses.append(pulse)


class BroadCaster:
    def __init__(self, name, goals):
        self.name, self.goals, self.pulses = name, goals, []
        self._type = 'Broadcaster'

    def cast(self):
        pulse, sender = self.pulses.pop(0)
        for goal in self.goals:
            # print(f'{self.name} --> {pulse} --> {goal}')
            modules[goal].receive((pulse, self.name))
            waiting_row.append(goal)
            if pulse == 'low':
                lows[0] += 1
            else:
                highs[0] += 1

    def receive(self, pulse):
        self.pulses.append(pulse)


class EndNode:
    def __init__(self, name):
        self.name, self.pulses = name, []
        self._type = 'EndNode'

    def receive(self, pulse):
        pass

    def cast(self):
        pass


modules, waiting_row = dict(), []
lows, highs = [0], [0]
for line in data:
    if line[0] == 'b':
        modules[line.split()[0]] = BroadCaster('broadcaster', line.split('-> ')[-1].split(', '))
    elif line[0] == '%':
        name = line[1:].split()[0]
        modules[name] = FlipFlop(name, line.split('-> ')[-1].split(', '))
    elif line[0] == '&':
        name = line[1:].split()[0]
        modules[name] = Conjunction(name, line.split('-> ')[-1].split(', '))

for key in list(modules.keys()):
    for goal in modules[key].goals:
        if goal not in modules:
            modules[goal] = EndNode(goal)
        if modules[goal]._type == 'Conjunction':
            modules[goal].memory[key] = 'low'

modules_pt2 = deepcopy(modules)
button = Button()

for buttonPush in range(1000):
    # print('\nNext button Push')
    button.push()
    while waiting_row:
        next_node = waiting_row.pop(0)
        modules[next_node].cast()
print(f'Part 1: {highs[0] * lows[0]}')

# Check input file for rx <-- df <-- [.. .. .. ..]
# If all four [..] values are low, high is given to df and low is give to rx
goals = {'ln': [0], 'xp': [0], 'xl': [0], 'gp': [0]}
values, waiting_row = [], []
modules = deepcopy(modules_pt2)

pushes = 0
while goals:
    pushes += 1
    button.push()
    while waiting_row:
        next_node = waiting_row.pop(0)
        modules[next_node].cast()
        for goal in list(goals.keys()):
            if modules[goal].all_low():
                if pushes != goals[goal][-1]:
                    goals[goal].append(pushes)
                    if len(goals[goal]) == 3:
                        print(f'{goal} --> {goals[goal]}')
                        values.append(pushes)
                        del goals[goal]
print(f'Part 2: {math.lcm(*values)}')
