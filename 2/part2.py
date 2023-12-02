from collections import Counter
from math import prod

from aoc import get_input, submit

def f(sets):
    """
    Get fewest number of cubes of each color that could have been in the bag to make game possible and return the power
    of the bag counts. The fewest number of cubes of each color that could have been in the bag will be the max of each
    color seen in the game.
    """

    bag = Counter()

    for x in sets.replace(";", ",").split(","):
        k, v = x.lstrip(" ").split(" ")[::-1]
        bag[k] = max(int(v), bag[k])

    return prod(bag.values())

if __name__ == "__main__":
    year, day, level = 2023, 2, 2
    aoc_input = get_input(year, day)
    lines = aoc_input.splitlines()

    ans = sum(f(line.partition(":")[-1]) for line in lines)
    submit(ans, year, day, level)
