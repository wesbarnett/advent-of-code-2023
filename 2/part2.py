from collections import Counter
from functools import reduce

from aoc import get_input, submit

def f(sets):
    """
    Get fewest number of cubes of each color that could have been in the bag to make game possible and return the power
    of the bag counts. The fewest number of cubes of each color that could have been in the bag will be the max of each
    color seen in the game.
    """

    bag = Counter()

    for x in sets.replace(";", ",").split(","):
        v, k = x.lstrip(" ").split(" ")
        bag[k] = max(int(v), bag[k])

    return reduce((lambda a, b: a*b), list(bag.values()))

if __name__ == "__main__":
    year, day, level = 2023, 2, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.split("\n")

    ans = sum(f(line.split(":")[-1]) for line in lines)
    submit(ans, year, day, level)
