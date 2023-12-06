from aoc_tool import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 1, 1
    aoc_input = get_input(year, day)

    lines = aoc_input.split("\n")

    result = 0
    for line in lines:
        nums = []
        for c in line:
            try:
                nums.append(int(c))
            except:
                pass
        num = nums[0]*10 + nums[-1]
        result += num

    submit(result, year, day, level)
