from aoc import get_input, submit

def check_game_is_possible(sets):
    bag = {"blue": 14, "green": 13, "red": 12}

    for s in sets.split(";"):
        for x in s.split(","):
            v, k = x.lstrip(" ").split(" ")
            if int(v) > bag[k]:
                return False

    return True

if __name__ == "__main__":
    year, day, level = 2023, 2, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.split("\n")

    ans = 0
    for line in lines:
        game, sets = line.split(":")
        game = int(game.split(" ")[-1].rstrip(":"))
        if check_game_is_possible(sets):
            ans += game

    submit(ans, year, day, level)
