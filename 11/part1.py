from itertools import combinations

from aoc_tool import get_input, submit

def expand_universe(universe):
    expanded_universe = []
    for line in universe:
        if all(x == "." for x in line):
            expanded_universe.append(line)
        expanded_universe.append(line)

    universe = transpose(expanded_universe)

    expanded_universe = []
    for line in universe:
        if all(x == "." for x in line):
            expanded_universe.append(line)
        expanded_universe.append(line)

    universe = transpose(expanded_universe)
    return universe

def transpose(it):
    "Swap the rows and columns of the input."
    # transpose([(1, 2, 3), (11, 22, 33)]) --> (1, 11) (2, 22) (3, 33)
    return zip(*it, strict=True)

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    year, day, level = 2023, 11, 1
    aoc_input = get_input(year, day)

    universe = [list(x) for x in aoc_input.splitlines()]
    universe = expand_universe(universe)

    galaxies = set()
    for y, row in enumerate(universe):
        for x, item in enumerate(row):
            if item == "#":
                galaxies.add((x, y))

    ans = sum(manhattan_dist(a, b) for a, b in combinations(galaxies, r=2))
    submit(ans, year, day, level)
