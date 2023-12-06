from math import prod

from aoc_tool import get_input, submit

def calc_dist(tim, t):
    return (tim - t) * t

def calc_max_time(tim):
    """Time held to achieve max distance."""
    return int(tim / 2)

if __name__ == "__main__":
    year, day, level = 2023, 6, 2
    aoc_input = get_input(year, day)

    """
    Some math:
    (time - time_held) * time_held = dist
    -time_held ** 2 + time * time_held = dist
    -2*time_held + time = 0
    time_held = time/2
    """
    lines = aoc_input.splitlines()

    tim = int("".join(lines[0].removeprefix("Time:").split()))
    dist = int("".join(lines[1].removeprefix("Distance:").split()))

    ways_to_win = 0

    max_time = calc_max_time(tim)
    t = max_time
    d = calc_dist(tim, t)
    while d > dist:
        ways_to_win += 1
        t += 1
        d = calc_dist(tim, t)

    t = max_time - 1
    d = calc_dist(tim, t)
    while d > dist:
        ways_to_win += 1
        t -= 1
        d = calc_dist(tim, t)

    ans = ways_to_win
    print(ans)
    submit(ans, year, day, level)
