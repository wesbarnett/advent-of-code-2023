from collections import defaultdict
from itertools import product
import re

from aoc_tool import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 3, 2
    aoc_input = get_input(year, day)

    schematic = aoc_input.splitlines()

    star_symbols = defaultdict(list)

    for i, line in enumerate(schematic):
        j = 0
        for s in re.split(r"([^0-9])", line):
            if s.isdigit():
                checked = set()
                for k, m, n in product(range(len(s)), (-1, 0, 1), (-1, 0, 1)):
                    x, y = i + m, j + k + n
                    if (m == n == 0) or (x, y) in checked:
                        continue
                    checked.add((x, y))
                    try:
                        if x >= 0 and y >= 0 and schematic[x][y] == "*":
                            star_symbols[(x, y)].append(int(s))
                            break
                    except IndexError:
                        pass
            j += len(s)

    ans = sum(v[0]*v[1] for v in star_symbols.values() if len(v) == 2)
    submit(ans, year, day, level)
