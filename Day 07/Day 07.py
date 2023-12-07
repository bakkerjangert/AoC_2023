class Hand:
    def __init__(self, card, score):
        self.card, self.score = card, score
        self._type = self.get_type(self.card)
        self.J_type = self.set_Jtype(self.card)

    def get_type(self, card):
        set_card = set(card)
        _type = None
        if len(set_card) == 1:
            _type = types[0]
        elif len(set_card) == 2:
            for c in set_card:
                if card.count(c) == 4:
                    _type = types[1]
            if _type is None:
                _type = types[2]
        elif len(set_card) == 3:
            for c in set_card:
                if card.count(c) == 3:
                    _type = types[3]
            if _type is None:
                _type = types[4]
        elif len(set_card) == 4:
            _type = types[5]
        elif len(set_card) == 5:
            _type = types[6]
        return _type

    def set_Jtype(self, card):
        if card.count('J') == 5 or card.count('J') == 0:
            return self.get_type(card)
        choices = set(card)
        choices.remove('J')
        J_cards = [card]
        new_cards = []
        while len(J_cards) > 0:
            card = J_cards.pop(0)
            for i, char in enumerate(card):
                if char == 'J':
                    for new_char in choices:
                        new_card = card[:i] + new_char + card[i + 1:]
                        if 'J' in new_card:
                            J_cards.append(new_card)
                        else:
                            new_cards.append(new_card)
        new_types = []
        for card in new_cards:
            new_types.append(self.get_type(card))
        new_types.sort(key=lambda x: (types.index(x)))
        return new_types[0]

    def __repr__(self):
        return f'Card {self.card} is a {self._type} and has score {self.score}\n' \
               f'Joker type = {self.J_type}'


types = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card']
card_order = 'AKQJT98765432'
card_order_J = 'AKQT98765432J'

file = 'input.txt'
# file = 'test.txt'
file = 'tweakers.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

cards = []

for line in data:
    card, score = line.split()[0], int(line.split()[1])
    cards.append(Hand(card, score))

sorted_cards = sorted(cards, key=lambda x: (types.index(x._type), [card_order.index(i) for i in list(x.card)]))
sorted_cards_pt2 = sorted(cards, key=lambda x: (types.index(x.J_type), [card_order_J.index(i) for i in list(x.card)]))
factor = len(cards)
pt1, pt2 = 0, 0
for card_pt1, card_pt2 in zip(sorted_cards, sorted_cards_pt2):
    pt1 += card_pt1.score * factor
    pt2 += card_pt2.score * factor
    factor -= 1
print(f'Part 1: {pt1}')
print(f'Part 2: {pt2}')
