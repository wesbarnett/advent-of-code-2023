from copy import deepcopy
from itertools import combinations

from aoc_tool import get_input, submit

def expand_universe(universe, galaxies, fact=1_000_000):

    galaxies_orig = deepcopy(galaxies)

    for y, line in enumerate(universe):
        if "#" not in line:
            for i, g in enumerate(galaxies):
                if galaxies_orig[i][1] > y:
                    g[1] += (fact-1)

    universe = transpose(universe)

    for x, line in enumerate(universe):
        if "#" not in line:
            for i, g in enumerate(galaxies):
                if galaxies_orig[i][0] > x:
                    g[0] += (fact-1)

    return galaxies

def transpose(it):
    return zip(*it, strict=True)

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    year, day, level = 2023, 11, 2
    aoc_input = get_input(year, day)

    universe = [list(x) for x in aoc_input.splitlines()]

    galaxies = []
    for y, row in enumerate(universe):
        for x, item in enumerate(row):
            if item == "#":
                galaxies.append([x, y])

    galaxies = expand_universe(universe, galaxies)

    ans = sum(manhattan_dist(a, b) for a, b in combinations(galaxies, r=2))
    submit(ans, year, day, level)
