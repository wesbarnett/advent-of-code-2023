from aoc_tool import get_input, submit

def get_num(line, reverse=False):
    range_ = range(len(line)-1, -1, -1) if reverse else range(len(line))
    for i in range_:
        try:
            x = int(line[i])
            return x
        except ValueError:
            num_spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            for j, x in enumerate(num_spelled, start=1):
                if line[i:].startswith(x):
                    return j

if __name__ == "__main__":
    year, day, level = 2023, 1, 2
    result = sum(get_num(line)*10 + get_num(line, reverse=True) for line in get_input(year, day).split("\n"))
    submit(result, year, day, level)
