file = 'input.txt'
# file = 'test.txt'
# file = 'test2.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

class Node:
    def __init__(self, x, y, d, steps_left):
        self.x, self.y = x, y
        self.d, self.s = d, steps_left

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (self.x, self.y, self.d, self.s) == (other.x, other.y, other.d, other.s)

    def __hash__(self):
        # Use hash() on a tuple of the attributes that define the object's identity
        return hash((self.x, self.y, self.d, self.s))


def get_next_node():
    current.sort(key=lambda x: values[x])
    n = current.pop(0)
    if (n.x, n.y) == end_node:
        return values[n]
    if n in visited:
        return None
    visited.add(n)
    for j, direction in enumerate(directions[n.d]):
        if j == 0 and n.s == 0:
            continue
        x, y = (n.x + next_node_dir[direction][0], n.y + next_node_dir[direction][1])
        s = n.s - 1 if j == 0 else 2
        if 0 <= x < len(data[0]) and 0 <= y < len(data):
            next_node = Node(x, y, direction, s)
            if next_node in visited:
                continue
            value = values[n] + int(data[y][x])
            if next_node in current:
                if value < values[next_node]:
                    values[next_node] = value
            else:
                current.append(next_node)
                values[next_node] = value


def get_next_node_pt2():
    current.sort(key=lambda x: values[x])
    n = current.pop(0)
    if (n.x, n.y) == end_node:
        return values[n]
    if n in visited:
        return None
    visited.add(n)
    for j, direction in enumerate(directions[n.d]):
        if j == 0 and n.s == 10:
            continue
        if j != 0 and n.s < 4:
            continue
        x, y = (n.x + next_node_dir[direction][0], n.y + next_node_dir[direction][1])
        s = n.s + 1 if j == 0 else 1
        if s < 4:
            x_min = 0 if direction != 'W' else 4 - s
            x_max = len(data[0]) if direction != 'E' else len(data[0]) - (4 - s)
            y_min = 0 if direction != 'N' else 4 - s
            y_max = len(data) if direction != 'S' else len(data) - (4 - s)
        else:
            x_min, x_max, y_min, y_max = 0, len(data[0]), 0, len(data)
        if x_min <= x < x_max and y_min <= y < y_max:
            next_node = Node(x, y, direction, s)
            if next_node in visited:
                continue
            value = values[n] + int(data[y][x])
            if next_node in current:
                if value < values[next_node]:
                    values[next_node] = value
            else:
                current.append(next_node)
                values[next_node] = value


next_node_dir = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
directions = {'N': ('N', 'E', 'W'), 'E': ('E', 'N', 'S'), 'S': ('S', 'E', 'W'), 'W': ('W', 'N', 'S')}

end_node = (len(data[0]) - 1, len(data) - 1)
current, visited, values = [], set(), dict()
current.append(Node(0, 0, 'E', 3))
values[current[0]] = 0


pt1 = None
while pt1 is None:
    pt1 = get_next_node()
print(f'Part 1: {pt1}')

current, visited, values = [], set(), dict()
current.append(Node(0, 0, 'E', 0))
values[current[0]] = 0

pt2 = None
while pt2 is None:
    pt2 = get_next_node_pt2()
print(f'Part 2: {pt2}')
