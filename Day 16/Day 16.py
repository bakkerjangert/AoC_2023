def get_next_position(pos, d, splitted_beams):
    next_pos = (pos[0] + directions[d][0], pos[1] + directions[d][1])
    if not (0 <= next_pos[0] < w and 0 <= next_pos[1] < h):
        return None, None, splitted_beams
    char = data[next_pos[1]][next_pos[0]]
    if char == '.':
        return next_pos, d, splitted_beams
    elif char == '/':
        return next_pos, map_slash_up[d], splitted_beams
    elif char == '\\':
        return next_pos, map_slash_down[d], splitted_beams
    elif char == '-':
        if d == 'N' or d == 'S':
            splitted_beams.append((next_pos, 'W',))
            return next_pos, 'E', splitted_beams
        else:
            return next_pos, d, splitted_beams
    elif char == '|':
        if d == 'W' or d == 'E':
            splitted_beams.append((next_pos, 'S',))
            return next_pos, 'N', splitted_beams
        else:
            return next_pos, d, splitted_beams


def energize_flow(start_point, start_dir):
    energized = dict()
    splitted_beams = [(start_point, start_dir)]  # Start outside zto account for mirror on entry point

    while splitted_beams:
        pos, direction = splitted_beams.pop(0)
        while True:
            if pos not in energized:
                energized[pos] = [direction]
            elif direction in energized[pos]:
                break  # Beam already followed; prevents looping
            else:
                energized[pos].append(direction)
            pos, direction, splitted_beams = get_next_position(pos, direction, splitted_beams)
            if pos is None:
                break
    return len(energized) - 1


file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

map_slash_up, map_slash_down = {'N': 'E', 'E': 'N', 'S': 'W', 'W': 'S'}, {'N': 'W', 'E': 'S', 'S': 'E', 'W': 'N'}
directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
h, w = len(data), len(data[0])

print(f'Part 1: {energize_flow((-1,0), "E")}')

max_flow = 0
for x in range(len(data[0])):
    max_flow = max(energize_flow((x, -1), 'S'), max_flow)
    max_flow = max(energize_flow((x, h), 'N'), max_flow)
for y in range(len(data)):
    max_flow = max(energize_flow((-1, y), 'E'), max_flow)
    max_flow = max(energize_flow((w, y), 'W'), max_flow)
print(f'Part 2: {max_flow}')

