def get_val(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val


file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

boxes = []
for box_no in range(256):
    boxes.append([])
pt1, pt2 = 0, 0
for string in data[0].split(','):
    pt1 += get_val(string)
    index = max(string.find('='), string.find('-'))
    box = get_val(string[:index])
    if '=' in string:
        name, focus, in_box = string[:index], int(string[index + 1:]), False
        for i, lens in enumerate(boxes[box]):
            if lens[0] == name:
                boxes[box][i], in_box = (name, focus), True
        if not in_box:
            boxes[box].append((name, focus))
    elif '-' in string:
        name = string[:index]
        for i, lens in enumerate(boxes[box][:]):
            if lens[0] == name:
                del boxes[box][i]
                break
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        pt2 += (i + 1) * (j + 1) * lens[1]
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')