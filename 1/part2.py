from aoc import get_input, submit

def get_num(line, num_spelled, reverse=False):
    range_ = range(len(line)-1, -1, -1) if reverse else range(len(line))
    for i in range_:
        try:
            x = int(line[i])
            return x
        except:
            for j, ns in enumerate(num_spelled):
                if line[i:].startswith(ns):
                    return j+1

if __name__ == "__main__":
    year, day, level = 2023, 1, 2
    aoc_input = get_input(year, day)

    lines = aoc_input.split("\n")
    num_spelled= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = sum(
        get_num(line, num_spelled)*10 + get_num(line, num_spelled, reverse=True)
        for line in lines
    )
    submit(result, year, day, level)
