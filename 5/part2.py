from collections import deque
from itertools import batched

from aoc import get_input, submit


def get_overlaps(x, y):

    # Not overlapping. Note that x[1] is the upper bound so its being equal to lower bound of y is still not an overlap.
    if y[0] >= x[1] or x[0] > y[1]:
        return tuple(), [x]

    overlap = (max(x[0], y[0]), min(x[1], y[1]))

    rem = []

    if x[0] < y[0]:
        rem.append((x[0], y[0]))

    if y[1] < x[1]:
        rem.append((y[1], x[1]))

    return overlap, rem


if __name__ == "__main__":
    year, day, level = 2023, 5, 2
    aoc_input = get_input(year, day)

    sections = aoc_input.split("\n\n")
    seeds_line = [int(x) for x in sections[0].partition(": ")[-1].split()]

    seeds = {(start, start+range_) for start, range_ in batched(seeds_line, 2)}

    lowest = []

    # Process a single seed range at a time
    for seed in seeds:

        inputs = deque([seed])

        # Move the seed range through the process, section by section
        for section in sections[1:]:

            dest_ranges = set()

            # Each section has multiple range "rules" that each range needs to go through. Sometimes part of a range 
            # will map to a destination range but the other part won't. That "remainder" range will then need to go
            # through each of the rules to see if it also maps to a destination range. If it makes it through all rules 
            # and never has any piece of it mapping to a destination, it then is mapped 1-1.
            while inputs:

                inp_range = inputs.popleft()
                overlapped = False

                # Move this range through all of the range "rules"
                for x in section.partition(":\n")[-1].splitlines():

                    dest_start, src_start, range_len = [int(i) for i in x.split()]
                    src_range = (src_start, src_start + range_len)
                    
                    # Remaining range that did not overlap will need to be checked with other range rules. inters is
                    # the range that overlapped with src_rang
                    inters, remain = get_overlaps(inp_range, src_range)

                    # If there was an overlapping range, that now needs to be mapped to the destination range
                    if inters:
                        shift = dest_start - src_start
                        dest_ranges.add((inters[0] + shift, inters[1] + shift))
                        overlapped = True

                    # Any remaining ranges that did not overlap will need to be brought through all of this section's
                    # range rules on their own
                    for rem in remain:
                        if rem not in inputs and rem != inp_range:
                            inputs.append(rem)

                # If this input range never overlapped any of the source ranges, that means it should be mapped to a
                # destination range 1-1
                if not overlapped:
                    dest_ranges.add(inp_range)

            # Populate the next sections inputs
            inputs = deque(list(dest_ranges))

        # Keep track of the lowest value for this seed range
        lowest.append(min(x for x, _ in inputs))

    ans = min(lowest)
    submit(ans, year, day, level)
