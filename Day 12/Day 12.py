import numpy as np
from copy import deepcopy
from functools import cache


class PuzzleState:
    def __init__(self, puzzle, instructions):
        self.puzzle = np.append(puzzle, '.')
        self.puzzle = np.insert(self.puzzle, 0, '.')
        self.start_index = 1
        self.instructions = instructions
        self.original_instructions = self.instructions[:]

    def simplify(self):
        pass



file = 'input.txt'
# file = 'test.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

pt1, pt2 = 0, 0
for line in data:
    puzzle, instructions = np.array(list(line.split()[0])), list(map(int, line.split()[1].split(',')))
    puzzles = {PuzzleState(puzzle, instructions)}
    solutions = 0
    while len(puzzles) > 0:
        next_puzzle = puzzles.pop()
        n = next_puzzle.instructions.pop(0)
        for i in range(next_puzzle.start_index, next_puzzle.puzzle.shape[0] - n):
            if np.count_nonzero(next_puzzle.puzzle[i: i + n] == '.') == 0:
                if next_puzzle.puzzle[i - 1] != '#' and next_puzzle.puzzle[i + n] != '#':
                    postions_left = np.count_nonzero(next_puzzle.puzzle[i + n:] == '#') + np.count_nonzero(next_puzzle.puzzle[i + n:] == '?')
                    if postions_left < sum(next_puzzle.instructions):
                        break
                    next_puzzle.start_index = i + n
                    solution = deepcopy(next_puzzle)
                    solution.puzzle[i: i + n] = ['#'] * n
                    if len(solution.instructions) == 0:
                        solution_instruction, count = [], 0
                        for char in solution.puzzle:
                            if char != '#':
                                if count != 0:
                                    solution_instruction.append(count)
                                    count = 0
                            else:
                                count += 1
                        if solution_instruction == solution.original_instructions:
                            solutions += 1
                    else:
                        puzzles.add(solution)
    pt1 += solutions
print(f'Part 1: {pt1}')


@cache
def solver(puzzle_string, instructions, end_of_fill=False):
    # check if all instructions full-filled at end of line
    if len(puzzle_string) == 0:
        return 0 if instructions else 1
    # check if no # left at end of instructions
    if not instructions:
        return 0 if puzzle_string.count('#') > 0 else 1
    # progress if next point in line is '.'
    if puzzle_string[0] == '.':
        return solver(puzzle_string[1:], instructions)
    # do not start new fill at end of previous fill
    if end_of_fill:
        return solver(puzzle_string[1:], instructions) if puzzle_string[0] != '#' else 0

    fill_length, number_of_solutions = instructions[0], 0
    # add fill if possible and continue next node wit end_fill property
    if puzzle_string[: fill_length].count('.') == 0 and len(puzzle_string) >= fill_length:
        number_of_solutions += solver(puzzle_string[fill_length:], instructions[1:], end_of_fill=True)
    # add '.' for ? if possible
    if puzzle_string[0] == '?':
        number_of_solutions += solver(puzzle_string[1:], instructions)

    return number_of_solutions


pt2 = 0
for i, line in enumerate(data):
    # print(f'{line} at {i + 1} of {len(data)}')
    puzzle, instructions = '?'.join([line.split()[0]] * 5), tuple(map(int, line.split()[1].split(','))) * 5
    pt2 += solver(puzzle, instructions)
print(f'Part 2: {pt2}')

# Answer = 548241300348335? According to other tweaker
