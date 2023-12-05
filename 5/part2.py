from aoc import get_input, submit

if __name__ == "__main__":
    year, day, level = 2023, 5, 2
    aoc_input = get_input(year, day)
    aoc_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    sections = aoc_input.split("\n\n")
    seeds = [int(x) for x in sections[0].partition(": ")[-1].split()]

    i = 0
    inputs = []
    while i < len(seeds):
        start, range_ = seeds[i], seeds[i+1]
        for x in range(start, start+range_):
            inputs.append(x)
        i += 2

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

    print(ans)
    #submit(ans, year, day, level)
