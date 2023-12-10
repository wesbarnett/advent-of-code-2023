from enum import auto, Enum
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
            raise Exception(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "-":
        if entered == CardinalDirection.E:
            return CardinalDirection.E
        elif entered == CardinalDirection.W:
            return CardinalDirection.W
        else:
            raise Exception(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "L":
        if entered == CardinalDirection.N:
            return CardinalDirection.W
        elif entered == CardinalDirection.E:
            return CardinalDirection.S
        else:
            raise Exception(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "J":
        if entered == CardinalDirection.N:
            return CardinalDirection.E
        elif entered == CardinalDirection.W:
            return CardinalDirection.S
        else:
            raise Exception(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "F":
        if entered == CardinalDirection.S:
            return CardinalDirection.W
        elif entered == CardinalDirection.E:
            return CardinalDirection.N
        else:
            raise Exception(f"Entering {pipe_type} from {entered} not possible")

    elif pipe_type == "7":
        if entered == CardinalDirection.W:
            return CardinalDirection.N
        elif entered == CardinalDirection.S:
            return CardinalDirection.E
        else:
            raise Exception(f"Entering {pipe_type} from {entered} not possible")
    else:
        raise ValueError(pipe_type)

if __name__ == "__main__":
    year, day, level = 2023, 10, 1
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
    counts = []
    for pipe_start, enter_dir_start in starting_configs:
        x, y = start_x, start_y
        pipe = pipe_start
        enter_dir = enter_dir_start
        count = 0
        while pipe != "S":
            try:
                enter_dir = get_next_enter_dir(pipe, enter_dir)
            except:
                count = -1
                break
            y, x = move(enter_dir, y, x)
            pipe = tiles[y][x]
            count += 1 
        try:
            enter_dir = get_next_enter_dir(pipe_start, enter_dir)
        except:
            count = -1
        counts.append(count)
    ans = max(counts) // 2
    submit(ans, year, day, level)
