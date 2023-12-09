from functools import reduce
from operator import sub

from aoc_tool import get_input, submit


if __name__ == "__main__":
    year, day, level = 2023, 9, 2
    aoc_input = get_input(year, day)
    lines = aoc_input.splitlines()
    ans = 0
    for line in lines:
        first = []
        items = [int(x) for x in line.split()]
        first.append(items[0])
        while not all(x == 0 for x in items):
            items = [j - i for i, j in zip(items[:-1], items[1:])]
            first.append(items[0])
        x = first.pop()
        while first:
            x = first.pop() - x
        ans += x

    submit(ans, year, day, level)
