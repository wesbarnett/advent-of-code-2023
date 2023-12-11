from enum import auto, Enum
from itertools import pairwise

from aoc_tool import get_input, submit

class CardinalDirection(Enum):
    N = auto()
    S = auto()
    E = auto()
    W = auto()

def find_start(tiles):
    for y, row in enumerate(tiles):
        for x in range(len(row)):
            if tiles[y][x] == "S":
                return y, x

def move(from_direction, y, x):
    if from_direction == CardinalDirection.S:
        return (y-1, x)
    if from_direction == CardinalDirection.N:
        return (y+1, x)
    if from_direction == CardinalDirection.E:
        return (y, x-1)
    if from_direction == CardinalDirection.W:
        return (y, x+1)


if __name__ == "__main__":
    year, day = 2023, 10
    aoc_input = get_input(year, day)

    tiles  = aoc_input.splitlines()
    start_y, start_x = find_start(tiles)

    # Map the direction entered the pipe to the direction entered from in the next pipe
    enter_dir_map = {
        "|": {CardinalDirection.S: CardinalDirection.S, CardinalDirection.N: CardinalDirection.N},
        "-": {CardinalDirection.E: CardinalDirection.E, CardinalDirection.W: CardinalDirection.W},
        "L": {CardinalDirection.N: CardinalDirection.W, CardinalDirection.E: CardinalDirection.S},
        "J": {CardinalDirection.N: CardinalDirection.E, CardinalDirection.W: CardinalDirection.S},
        "F": {CardinalDirection.S: CardinalDirection.W, CardinalDirection.E: CardinalDirection.N},
        "7": {CardinalDirection.W: CardinalDirection.N, CardinalDirection.S: CardinalDirection.E},
    }
    # Try out each potential shape of the pipe for the starting location and one direction
    # since a success will be looped no need to check both directions
    starting_configs  = [(k, list(v.keys())[0]) for k, v in enter_dir_map.items()]
    for pipe_start, enter_dir_start in starting_configs:
        x, y, pipe, enter_dir = start_x, start_y, pipe_start, enter_dir_start
        loop = [(x, y)]
        try:
            # Traverse the pipe and if at any point the next pipe segment is not connected
            # to the current pipe, a KeyError will be raised and this is an invalid starting
            # shape
            while pipe != "S":
                enter_dir = enter_dir_map[pipe][enter_dir]
                y, x = move(enter_dir, y, x)
                loop.append((x, y))
                pipe = tiles[y][x]
            # Check that we can actually enter the starting segment pipe after making the
            # complete loop
            enter_dir = enter_dir_map[pipe_start][enter_dir]
        except KeyError:
            continue
        else:
            break

    ans = len(loop) // 2

    print(f"Part 1: {ans}")
    #submit(ans, year, day, 1)

    # Shoelace formula
    A = abs(sum(x1*y2 - y1*x2 for (x1, y1), (x2, y2)  in pairwise(loop)) / 2)

    # Pick's theroem
    ans = int(A - len(loop)//2 + 1)

    print(f"Part 2: {ans}")
    #submit(ans, year, day, 2)

    # Ray-casting
    c = 0
    ncols, nrows = len(tiles[0]), len(tiles)
    for y in range(nrows):
        tp = bp = 0
        for x in range(ncols):
            if (x, y) in loop: 
                if tiles[y][x] in "|LJ": 
                    tp += 1
                if tiles[y][x] in "|F7": 
                    bp += 1
            elif bp % 2 == 1 and tp % 2 == 1:
                tmp = list(tiles[y])
                tmp[x] = "·"
                tiles[y] = "".join(tmp)
                c += 1

    # Printing
    for y in range(nrows):
        tiles[y] = tiles[y].replace("7", "┓").replace("F", "┏").replace("J", "┛").replace("L", "┗").replace("|", "┃").replace("-", "━")
        tmp = list(tiles[y])
        for x in range(ncols):
            if (x, y) not in loop and tiles[y][x] != "·":
                tmp[x] = " "
            tiles[y] = "".join(tmp)
        print(tiles[y])
