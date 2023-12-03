from itertools import product
import re

from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 3, 1
    aoc_input = get_input(year, day)

    ans = 0
    schematic = aoc_input.splitlines()

    for i, line in enumerate(schematic):
        j = 0
        for s in re.split(fr"([^0-9])", line):
            if s.isdigit():
                for k, m, n in product(range(len(s)), (-1, 0, 1), (-1, 0, 1)):
                    x, y = i + m, j + k + n
                    if x >= 0 and y >= 0:
                        try:
                            if (not schematic[x][y].isdigit() and schematic[x][y] != "."):
                                ans += int(s)
                                break
                        except IndexError:
                            pass
            j += len(s)

    submit(ans, year, day, level)
