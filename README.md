# ❄️ advent-of-code-2023 ❄️

Personal solutions to [Advent of Code 2023](https://adventofcode.com/2023).

Note that I use my [aoc-tool](https://github.com/wesbarnett/aoc-tool) to download input and submit solutions.

## Personal notes

### Splitting lines

[`str.splitlines()`](https://docs.python.org/3/library/stdtypes.html#str.splitlines) - preferred over `str.split("\n")`. "this method returns an empty list for the empty string, and a terminal line break does not result in an extra line"

*Days 2 onward"

### Overlaps

The overlap of two intervals `x` and `y` (defined as tuples) is:

```python
max(x[0], y[0]), min(x[1], y[1])
```

*Day 5*

### Quadratic formula

Reminder of how to solve a quadratic equation using the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula).

### Sorting by 

[`functools.cmp_to_key`](https://docs.python.org/3/library/functools.html) - Use a comparison function as a key function in a sort.

*Day 7*

### Least common multiple

Can be found using the method [`math.lcm`](https://docs.python.org/3/library/math.html#math.lcm).

*Day 8*

### Area / number of points in a closed loop

Shoelace Formula - Find area in a closed loop / polygon
Pick's Theorem - Find number of points within a polygon or number of points on the boundary

*Day 10*

### Useful itertools methods

* [`itertools.batched`](https://docs.python.org/3/library/itertools.html#itertools.batched) - "Batch data from the iterable into tuples of length n. The last batch may be shorter than n." *Day 5*
* [`itertools.pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise) - "Return successive overlapping pairs taken from the input iterable". *Days 9 and 10*
