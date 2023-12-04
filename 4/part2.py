from collections import defaultdict
from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 4, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.splitlines()

    cards_num = {i: 1 for i in range(1, len(lines)+1)}

    for i, line in enumerate(lines, start=1):
        winning, mine = line.split(": ")[-1].split(" | ")
        winning = [int(x) for x in winning.split()]
        mine = [int(x) for x in mine.split()]
        matched = len(set(winning) & set(mine))
        for j in range(1, matched+1):
            cards_num[i+j] += cards_num[i]
        
    ans = sum(cards_num.values())
    submit(ans, year, day, level)
