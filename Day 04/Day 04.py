file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

pt1 = 0
pt2 = {n: 1 for n in range(1, len(data) + 1)}

for line in data:
    # Gather Data
    while '  ' in line:
        line = line.replace('  ', ' ')
    card_no = int(line.split(' ')[1].split(':')[0])
    winners = list(map(int, line.split(': ')[1].split(' |')[0].split(' ')))
    my_cards = list(map(int, line.split('| ')[1].split(' ')))
    # Part 1
    card_score, wins = 0, 0
    for card in my_cards:
        if card in winners:
            wins += 1
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2
    pt1 += card_score
    # Part 2
    for n in range(card_no + 1, card_no + wins + 1):
        pt2[n] += pt2[card_no]
print(f'Part 1: {pt1}')
print(f'Part 2: {sum(pt2.values())}')
