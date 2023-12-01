import numpy as np

file = 'input.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

numbers = '0123456789'
answer_part_1 = 0
for line in data:
    n = ''
    for char in line:
        if char in numbers:
            n += char
            break
    for char in line[::-1]:
        if char in numbers:
            n += char
            break
    answer_part_1 += int(n)
print(f'Part 1: {answer_part_1}')

# written_numbers = {3: ('one', 'two', 'six'),
#                    4: ('four', 'five', 'nine'),
#                    5: ('three', 'seven', 'eight')}
written_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

answer_part_2 = 0
for line in data:
    # print(line)
    indexes = dict()
    for number in numbers:
        if number in line:
            index = line.find(number)
            index_rev = line[::-1].find(number)
            index_rev = len(line) - 1 - index_rev
            indexes[index] = number
            indexes[index_rev] = number
            # print(f'Found {number} at {index} and {index_rev}')
    for written_number in written_numbers:
        if written_number in line:
            index = line.find(written_number)
            index_rev = line[::-1].find(written_number[::-1])
            index_rev = len(line) - 1 - index_rev - len(written_number) + 1
            indexes[index] = str(written_numbers[written_number])
            indexes[index_rev] = str(written_numbers[written_number])
            # print(f'Found {written_number} at {index} and {index_rev}')
    number = indexes[min(indexes)] + indexes[max(indexes)]
    answer_part_2 += int(number)
    # print(indexes)
    # print(number)
print(f'Part 2: {answer_part_2}')


