file = 'input.txt'
# file = 'test.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

times = list(map(int, data[0].split(':')[1].split()))
distances = list(map(int, data[1].split(':')[1].split()))

times.append(int(''.join((map(str, times)))))
distances.append(int(''.join(map(str, distances))))

pt1, pt2 = 1, 1
for d, t in zip(distances, times):
    seconds = ((t + (t ** 2 - 4 * d) ** 0.5) / 2, (t - (t ** 2 - 4 * d) ** 0.5) / 2)
    s1, s2 = int(min(seconds)), int(max(seconds))  # int truncates number; add 1 for s1, s2 should be correct
    # account for edge case that sqrt() result in int number
    while s1 * (t - s1) <= d:
        s1 += 1
    while s2 * (t - s2) <= d:
        s2 -= 1
    if t != times[-1]:
        pt1 *= (s2 - s1 + 1)
    else:
        pt2 *= (s2 - s1 + 1)
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')

# d = s * (t - s) --> d = st - s2 --> s2 - st + d = 0 --> Use ABC formula to get s; see var seconds above