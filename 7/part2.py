from collections import Counter
from functools import cmp_to_key
from aoc_tool import get_input, submit

def get_type(hand):
    counts = Counter(hand)
    c = sorted(counts.values())
    if c == [5]:
        return 6
    elif c == [1, 4]:
        return 5
    elif c == [2, 3]:
        return 4
    elif c == [1, 1, 3]:
        return 3
    elif c == [1, 2, 2]:
        return 2
    elif c == [1, 1, 1, 2]:
        return 1
    elif c == [1, 1, 1, 1, 1]:
        return 0

def get_type_with_jokers(hand):
    return max(get_type(hand.replace("J", k)) for k in hand)

def compare(x, y):
    x, y = x[0], y[0]
    order = {"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0}
    xt = get_type_with_jokers(x)
    yt = get_type_with_jokers(y)

    if xt > yt:
        return -1

    if xt < yt:
        return 1

    for i, j in zip(x, y):
        if order[i] > order[j]:
            return -1
        if order[j] > order[i]:
            return 1

    return 0


if __name__ == "__main__":
    year, day, level = 2023, 7, 2
    aoc_input = get_input(year, day)
    
    lines = aoc_input.splitlines()
    hands = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        hands.append((hand, bid))

    hands = sorted(hands, key=cmp_to_key(compare))
    ans = sum(i*x[1] for i, x in enumerate(reversed(hands), start=1))
    submit(ans, year, day, level)