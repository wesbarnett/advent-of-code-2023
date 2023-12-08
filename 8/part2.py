from itertools import cycle
from math import lcm
from aoc_tool import get_input, submit

D = {"L": 0, "R": 1}

if __name__ == "__main__":
    year, day, level = 2023, 8, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.splitlines()
    inst = cycle(lines[0])

    mapper = {}
    for line in lines[2:]:
        src, dest = line.split(" = ")
        dest = tuple(dest.removeprefix("(").removesuffix(")").split(", "))
        mapper[src] = dest

    nodes = [x for x in mapper.keys() if x.endswith("A")]
    all_steps = []
    steps = 0
    for node in nodes:
        inst = cycle(lines[0])
        steps = 0
        while not node.endswith("Z"):
            steps += 1
            node = mapper[node][D[next(inst)]]
        all_steps.append(steps)

    ans = lcm(*all_steps)
    submit(ans, year, day, level)
