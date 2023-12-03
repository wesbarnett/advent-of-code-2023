from collections import defaultdict
from itertools import product
import re

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 3, 2
    aoc_input = get_input(year, day)

    schematic = aoc_input.splitlines()

    symbols = "".join([x for x in sorted(list(set(aoc_input))) if not x.isdigit() and x != "\n"])
    star_symbols = defaultdict(list)

    for i, line in enumerate(schematic):
        j = 0
        for s in re.split(fr"([{symbols}])", line):
            if s.isdigit():
                for k, (x, y) in product(range(len(s)), [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]):
                    if x >= 0 and y+k >= 0:
                        try:
                            if schematic[x][y+k] == "*":
                                star_symbols[(x, y+k)].append(int(s))
                                break
                        except IndexError:
                            pass
            j += len(s)

    ans = sum(v[0]*v[1] for v in star_symbols.values() if len(v) == 2)
    submit(ans, year, day, level)
