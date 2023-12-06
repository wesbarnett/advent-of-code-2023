from aoc_tool import get_input, submit

def check_game_is_possible(sets):
    bag = {"blue": 14, "green": 13, "red": 12}

    for s in sets.split(";"):
        for x in s.split(","):
            k, v = x.lstrip(" ").split(" ")[::-1]
            if int(v) > bag[k]:
                return False

    return True

if __name__ == "__main__":
    year, day, level = 2023, 2, 1
    aoc_input = get_input(year, day)
    all_sets = [line.partition(":")[-1] for line in aoc_input.splitlines()]
    ans = sum(i for i, sets in enumerate(all_sets, start=1) if check_game_is_possible(sets))
    submit(ans, year, day, level)
