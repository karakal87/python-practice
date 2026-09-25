"""
Week 1 — File 4: Functions (arguments, defaults, *args, scope)

Fill in each function body. Run this file to check your work:
    python 04_functions.py

AI off. Write it yourself.
"""

from _check import run


def greet(name, greeting="Hello"):
    """Return '<greeting>, <name>!'. greeting defaults to 'Hello'.
    Example: greet('Tom') -> 'Hello, Tom!', greet('Tom', 'Hi') -> 'Hi, Tom!'."""
    return f'{greeting}, {name}!'
    raise NotImplementedError


def total(*nums): # nums is a TUPLE of all the positional arguments
    """Return the sum of any number of positional arguments.
    Example: total(1, 2, 3) -> 6, total() -> 0."""
    return sum(nums)
    raise NotImplementedError


def apply_twice(func, x):
    """Apply the function `func` to x, twice, and return the result.
    Example: apply_twice(lambda v: v + 1, 5) -> 7."""
    return func(func(x))
    raise NotImplementedError


def running_totals(nums):
    """Return a list of running (cumulative) totals.
    Example: running_totals([1, 2, 3]) -> [1, 3, 6]."""
    # totals = []
    # running_total = 0
    # for num in nums:
    #     running_total += num
    #     totals.append(running_total)
    # return totals
    # return [sum(nums[:i+1]) for i in range(len(nums))]
    from itertools import accumulate
    return list(accumulate(nums))
    raise NotImplementedError


def make_multiplier(factor):
    """Return a FUNCTION that multiplies its argument by `factor` (a closure).
    Example: triple = make_multiplier(3); triple(5) -> 15."""
    return lambda x: factor*x
    raise NotImplementedError


def _make_multiplier_case():
    """Build and call the multiplier in one thunk so closures are tested end to end."""
    triple = make_multiplier(3)
    return triple(5)


if __name__ == "__main__":
    run([
        ("greet default", lambda: greet("Tom"), "Hello, Tom!"),
        ("greet custom", lambda: greet("Tom", "Hi"), "Hi, Tom!"),
        ("total", lambda: total(1, 2, 3), 6),
        ("total empty", lambda: total(), 0),
        ("apply_twice", lambda: apply_twice(lambda v: v + 1, 5), 7),
        ("running_totals", lambda: running_totals([1, 2, 3]), [1, 3, 6]),
        ("make_multiplier", _make_multiplier_case, 15),
    ])
