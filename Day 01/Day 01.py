file = 'input.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

digits = '123456789'
numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
numbers.update({n: n for n in digits})

pt1, pt2 = 0, 0
for line in data:
    # print(line)
    indexes_digit, indexes_total = dict(), dict()
    for number in numbers:
        string, delta_i = line, 0
        while number in string:
            index = string.find(number) + delta_i
            indexes_total[index] = numbers[number]
            if number in digits: indexes_digit[index] = numbers[number]
            delta_i += string.find(number) + 1
            string = string[string.find(number) + 1:]
    print(indexes_digit)
    print(indexes_total)
    pt1 += int(indexes_digit[min(indexes_digit)] + indexes_digit[max(indexes_digit)])
    pt2 += int(indexes_total[min(indexes_total)] + indexes_total[max(indexes_total)])
    # print('pt1', int(indexes_digit[min(indexes_digit)] + indexes_digit[max(indexes_digit)]))
    # print('pt2', int(indexes_total[min(indexes_total)] + indexes_total[max(indexes_total)]))
print(f'Answer Part 1: {pt1}')
print(f'Answer Part 2: {pt2}')
