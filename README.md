# ❄️ advent-of-code-2023 ❄️

Personal solutions to [Advent of Code 2023](https://adventofcode.com/2023).

Note that I use my [aoc-tool](https://github.com/wesbarnett/aoc-tool) to download input and submit solutions.

## Personal notes

Some concepts / stdlib methods that were new or had been awhile since looking at.

### Day 2 - Splitting lines

[`str.splitlines()`](https://docs.python.org/3/library/stdtypes.html#str.splitlines) - preferred over `str.split("\n")`. "this method returns an empty list for the empty string, and a terminal line break does not result in an extra line"

### Day 5 - Overlaps

The overlap of two intervals `x` and `y` (defined as tuples) is:

```python
max(x[0], y[0]), min(x[1], y[1])
```
 
### Day 6 - Quadratic formula

Reminder of how to solve a quadratic equation using the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula).

```python
d = sqrt(b**2 - 4*a*c)
x0 = (-b + d) / 2*a
x1 = (-b - d) / 2*a
```

### Day 7 - Sorting by a comparison function

[`functools.cmp_to_key`](https://docs.python.org/3/library/functools.html) - Use a comparison function as a key function in a sort.

### Day 8 - Least common multiple

Can be found using the method [`math.lcm`](https://docs.python.org/3/library/math.html#math.lcm).

### Day 10 - Area / number of points in a closed loop

[Shoelace Formula](https://en.wikipedia.org/wiki/Shoelace_formula) - Find area in a closed loop / polygon

```python
area = abs(sum(x1*y2 - y1*x2 for (x1, y1), (x2, y2) in pairwise(points)) / 2)
```

[Pick's Theorem](https://en.wikipedia.org/wiki/Pick's_theorem) - Find number of points within a polygon or number of points on the boundary

```python
area = interior_points + boundary_points/2 - 1
```

### Useful itertools methods

* [`itertools.batched`](https://docs.python.org/3/library/itertools.html#itertools.batched) - "Batch data from the iterable into tuples of length n. The last batch may be shorter than n." *Day 5*
* [`itertools.pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise) - "Return successive overlapping pairs taken from the input iterable". *Days 9 and 10*
