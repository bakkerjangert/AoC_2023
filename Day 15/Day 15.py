def get_val(string, val=0):
    for char in string:
        val = ((val + ord(char)) * 17) % 256
    return val


file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

boxes = {i: dict() for i in range(256)}  # use fact that dicts are ordered now in python
pt1, pt2 = 0, 0

for string in data[0].split(','):
    pt1 += get_val(string)
    index = max(string.find('='), string.find('-'))  # use fact that if character not found returned index = -1
    name, box = string[:index], get_val(string[:index])
    if '=' in string:
        boxes[box][name] = int(string[index + 1:])  # replaced if key exists, otherwise added at bottom
    elif '-' in string and name in boxes[box]:
        del boxes[box][name]  # neat that dicts are ordered now in python

for box in boxes:
    for pos, focus in enumerate(boxes[box].values()):
        pt2 += (box + 1) * (pos + 1) * focus

print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
