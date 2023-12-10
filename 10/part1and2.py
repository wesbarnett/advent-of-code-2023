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

def get_next_enter_dir(pipe_type, entered):

    if pipe_type == "|":
        if entered == CardinalDirection.S:
            return CardinalDirection.S
        elif entered == CardinalDirection.N:
            return CardinalDirection.N
        else:
            raise ValueError(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "-":
        if entered == CardinalDirection.E:
            return CardinalDirection.E
        elif entered == CardinalDirection.W:
            return CardinalDirection.W
        else:
            raise ValueError(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "L":
        if entered == CardinalDirection.N:
            return CardinalDirection.W
        elif entered == CardinalDirection.E:
            return CardinalDirection.S
        else:
            raise ValueError(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "J":
        if entered == CardinalDirection.N:
            return CardinalDirection.E
        elif entered == CardinalDirection.W:
            return CardinalDirection.S
        else:
            raise ValueError(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "F":
        if entered == CardinalDirection.S:
            return CardinalDirection.W
        elif entered == CardinalDirection.E:
            return CardinalDirection.N
        else:
            raise ValueError(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "7":
        if entered == CardinalDirection.W:
            return CardinalDirection.N
        elif entered == CardinalDirection.S:
            return CardinalDirection.E
        else:
            raise ValueError(f"Entering {pipe_type} from {entered} not possible")
    else:
        raise ValueError(pipe_type)

if __name__ == "__main__":
    year, day = 2023, 10
    aoc_input = get_input(year, day)

    tiles  = aoc_input.splitlines()
    start_y, start_x = find_start(tiles)

    starting_configs  = [
        ("F", CardinalDirection.S),
        ("7", CardinalDirection.W),
        ("|", CardinalDirection.N),
        ("J", CardinalDirection.W),
        ("-", CardinalDirection.E),
        ("L", CardinalDirection.E),
    ]
    for pipe_start, enter_dir_start in starting_configs:
        x, y, pipe, enter_dir = start_x, start_y, pipe_start, enter_dir_start
        loop = [(x, y)]
        try:
            while pipe != "S":
                enter_dir = get_next_enter_dir(pipe, enter_dir)
                y, x = move(enter_dir, y, x)
                loop.append((x, y))
                pipe = tiles[y][x]
            enter_dir = get_next_enter_dir(pipe_start, enter_dir)
        except ValueError:
            continue
        else:
            break

    ans = len(loop) // 2

    print(f"Part 1: {ans}")
    submit(ans, year, day, 1)

    # Shoelace formula
    A = abs(sum(x1*y2 - y1*x2 for (x1, y1), (x2, y2)  in pairwise(loop)) / 2)

    # Pick's theroem
    ans = int(A - len(loop)//2 + 1)

    print(f"Part 2: {ans}")
    submit(ans, year, day, 2)
