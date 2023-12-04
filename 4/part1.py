from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 4, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.splitlines()

    ans = 0
    for line in lines:
        winning, mine = line.split(": ")[-1].split(" | ")
        winning = [int(x) for x in winning.split()]
        mine = [int(x) for x in mine.split()]
        matched = len(set(winning) & set(mine))
        if matched > 0:
            score = 2**(matched-1)
            ans += score
        
    print(ans)
    submit(ans, year, day, level)
