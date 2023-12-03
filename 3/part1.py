from itertools import product
import re

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 3, 1
    aoc_input = get_input(year, day)

    ans = 0
    schematic = aoc_input.splitlines()

    symbols = "".join([x for x in set(aoc_input) if not x.isdigit() and x != "\n"])

    for i, line in enumerate(schematic):
        j = 0
        for s in re.split(fr"([{symbols}])", line):
            if s.isdigit():
                for k, (x, y) in product(range(len(s)), [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]):
                    if x >= 0 and y+k >= 0:
                        try:
                            if (not schematic[x][y+k].isdigit() and schematic[x][y+k] != "."):
                                ans += int(s)
                                break
                        except IndexError:
                            pass
            j += len(s)

    submit(ans, year, day, level)
