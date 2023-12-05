from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 5, 1
    aoc_input = get_input(year, day)

    sections = aoc_input.split("\n\n")
    inputs = [int(x) for x in sections[0].partition(": ")[-1].split()]

    for section in sections:
        name, _, data = section.partition(":\n")
        mapper = {}

        for x in data.splitlines():
            dest_start, src_start, range_len = [int(i) for i in x.split()]

            for inp in inputs:
                if src_start <= inp < src_start + range_len:
                    mapper[inp] = (dest_start - src_start) + inp

        for inp in inputs:
            if inp not in mapper:
                mapper[inp] = inp

        new_inputs = []
        for inp in inputs:
            new_inputs.append(mapper[inp])
        ans = min(new_inputs)
        inputs = new_inputs

    submit(ans, year, day, level)
