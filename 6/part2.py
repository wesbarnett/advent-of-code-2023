from math import sqrt

from aoc_tool import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 6, 2
    aoc_input = get_input(year, day)

    """
    -time_held ** 2 + time * time_held - dist = 0
    time_held = (-time +/- sqrt(time**2 - 4*dist))/2

    """
    lines = aoc_input.splitlines()

    tim = int("".join(lines[0].removeprefix("Time:").split()))
    dist = int("".join(lines[1].removeprefix("Distance:").split()))

    time_held_1 = (-tim + sqrt(tim**2 - 4*dist))/ 2
    time_held_2 = (-tim - sqrt(tim**2 - 4*dist))/ 2
    ans = abs(int(time_held_1) - int(time_held_2))

    print(ans)
    submit(ans, year, day, level)
