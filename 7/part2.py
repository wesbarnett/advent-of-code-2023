from collections import Counter
from functools import cmp_to_key
from aoc_tool import get_input, submit

ORDER = dict((i[1], i[0]) for i in enumerate("J23456789TQKA"))
TYPES = dict((i[1], i[0]) for i in enumerate([(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5, )]))

def get_type(hand):
    return TYPES[tuple(sorted(Counter(hand).values()))]

def get_type_with_jokers(hand):
    return max(get_type(hand.replace("J", k)) for k in set(hand))

def compare(x, y):
    x, y = x[0], y[0]
    xt, yt = get_type_with_jokers(x), get_type_with_jokers(y)

    if xt > yt:
        return -1

    if xt < yt:
        return 1

    for i, j in zip(x, y):
        if ORDER[i] > ORDER[j]:
            return -1
        if ORDER[j] > ORDER[i]:
            return 1

    return 0


if __name__ == "__main__":
    year, day, level = 2023, 7, 2
    aoc_input = get_input(year, day)
    
    lines = aoc_input.splitlines()
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((hand, int(bid)))

    hands = sorted(hands, key=cmp_to_key(compare))
    ans = sum(i*x[1] for i, x in enumerate(reversed(hands), start=1))
    submit(ans, year, day, level)
