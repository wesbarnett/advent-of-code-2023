from itertools import cycle
from aoc_tool import get_input, submit

D = {"L": 0, "R": 1}

if __name__ == "__main__":
    year, day, level = 2023, 8, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.splitlines()
    inst = cycle(lines[0])

    mapper = {}
    for line in lines[2:]:
        src, dest = line.split(" = ")
        dest = tuple(dest.removeprefix("(").removesuffix(")").split(", "))
        mapper[src] = dest

    node = "AAA"
    steps = 0
    while node != "ZZZ":
        steps += 1
        node = mapper[node][D[next(inst)]]

    submit(steps, year, day, level)
