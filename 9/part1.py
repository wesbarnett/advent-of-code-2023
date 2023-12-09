from aoc_tool import get_input, submit


if __name__ == "__main__":
    year, day, level = 2023, 9, 1
    aoc_input = get_input(year, day)
    lines = aoc_input.splitlines()

    ans = 0
    for line in lines:
        last = []
        items = [int(x) for x in line.split()]
        last.append(items[-1])
        while not all(x == 0 for x in items):
            items = [j - i for i, j in zip(items[:-1], items[1:])]
            last.append(items[-1])
        ans += sum(last)

    submit(ans, year, day, level)
