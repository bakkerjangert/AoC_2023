def get_val(string, val=0):
    for char in string:
        val = ((val + ord(char)) * 17) % 256
    return val


file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

boxes = {i: dict() for i in range(256)}
pt1, pt2 = 0, 0
for string in data[0].split(','):
    pt1 += get_val(string)
    index = max(string.find('='), string.find('-'))
    name, box = string[:index], get_val(string[:index])
    if '=' in string:
        boxes[box][name] = int(string[index + 1:])
    elif '-' in string:
        if name in boxes[box]:
            del boxes[box][name]
for box in boxes:
    for pos, lens in enumerate(boxes[box]):
        pt2 += (box + 1) * (pos + 1) * boxes[box][lens]
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
