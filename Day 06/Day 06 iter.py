file = 'input.txt'
# file = 'test.txt'
# file = 'tweak.txt'

with open(file, 'r') as f:
    data = f.read().splitlines()

times = list(map(int, data[0].split(':')[1].split()))
distances = list(map(int, data[1].split(':')[1].split()))

times.append(int(''.join((map(str, times)))))
distances.append(int(''.join(map(str, distances))))

print(times)
print(distances)

pt1, pt2, eps = 1, 1, 0.0001
for i, (d, t) in enumerate(zip(distances, times)):
    d, t = (d, t)
    t_min, t_max = 0, t / 2
    t_guess = (t_max + t_min) / 2
    d_t = t_guess * (t - t_guess)
    while not d - eps < d_t < d + eps:
        t_guess = (t_min + t_max) / 2
        # sometimes infinite loop occurs if average(t_min, t_max) == t_min or t_max; break out if that is happening.
        if t_guess in (t_min, t_max):
            break
        d_t =  t_guess * (t - t_guess)
        # print(t_min, t_max, t_guess, d_t)
        if d_t < d:
            t_min = t_guess
        else:
            t_max = t_guess
    t1 = int(t_guess)
    while t1 * (t - t1) <= d:
        t1 += 1
    t2 = t - t1
    if i < len(distances) - 1:
        pt1 *= (t2 - t1 + 1)
    else:
        pt2 *= (t2 - t1 + 1)
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
