import numpy as np
import networkx as nx

file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

grid = np.array(list(map(list, data)))
start, end = (1, 0), (grid.shape[1] - 2, grid.shape[0] - 1)
trails = [(start,)]
finished = []

while trails:
    trail = trails.pop(0)
    for d in (1, 0, '>'), (0, 1, 'v'), (-1, 0, ''), (0, -1, ''):
        next_pos = (trail[-1][0] + d[0], trail[-1][1] + d[1])
        if next_pos[0] < 0 or next_pos[1] < 0:
            continue
        if next_pos == end:
            finished.append(trail + (next_pos,))
        elif grid[next_pos[1], next_pos[0]] in '.' + d[2] and next_pos not in trail:
            trails.append(trail + (next_pos,))
finished.sort(key=lambda x: len(x), reverse=True)
print(f'Part 1: {len(finished[0]) - 1}')  # -1 because startpoint is in trail and not a step


def print_grid():
    for row in grid:
        print(''.join(row))


def find_longest_path(graph, start_node, end_node):
    # Function to perform depth-first search for finding the longest path
    def dfs(node, path, path_weight):
        nonlocal max_path, max_weight
        if node == end_node:
            # Found a path to the end node, update max_path if longer
            if path_weight > max_weight:
                max_path = path.copy()
                max_weight = path_weight
            return None
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                edge_weight = graph[node][neighbor]['weight']
                dfs(neighbor, path + [neighbor], path_weight + edge_weight)
    max_path = []
    max_weight = float('-inf')
    for neighbor in graph.neighbors(start_node):
        edge_weight = graph[start_node][neighbor]['weight']
        dfs(neighbor, [start_node, neighbor], edge_weight)
    return max_path, max_weight


graph = nx.Graph()
grid = np.array(list(map(list, data)))
grid = np.where(grid == '>', '.', grid)
grid = np.where(grid == 'v', '.', grid)
grid[0, 1], grid[-1, -2] = 'S', 'E'

names = list('ABCDFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrstuvwxyz')
names_org = names[:]
open_connections = [('S', (1, 1))]

while open_connections:
    prev_node, position = open_connections.pop(0)
    steps, next_positions = 0, [position]
    while len(next_positions) == 1:
        position = next_positions[0]
        if grid[position[1], position[0]] == '*':
            break
        grid[position[1], position[0]] = '*'
        next_positions = []
        steps += 1
        for d in (1, 0), (0, 1), (-1, 0), (0, -1):
            next_position = (position[0] + d[0], position[1] + d[1])
            if grid[next_position[1], next_position[0]] == '.':
                next_positions.append(next_position)
            if grid[next_position[1], next_position[0]] in names_org and grid[next_position[1], next_position[0]] != prev_node:
                graph.add_edge(prev_node, grid[next_position[1], next_position[0]], weight=steps + 1)
            if grid[next_position[1], next_position[0]] == 'E':
                graph.add_edge(prev_node, 'E', weight=steps + 1)
                break
    if len(next_positions) > 1:
        next_node = names.pop(0)
        graph.add_edge(prev_node, next_node, weight=steps)
        grid[position[1], position[0]] = next_node
        for pos in next_positions:
            open_connections.append((next_node, pos))
    if not open_connections:
        break

print(f'Part 2: {find_longest_path(graph, "S", "E")[1]}')

# grid = np.where(grid == '*', '.', grid)
# print_grid()
# for edge in graph.edges(data=True):
#     print(edge)
# print(graph)
# pos = nx.spring_layout(graph)  # Set layout for nodes
# nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
# plt.show()


