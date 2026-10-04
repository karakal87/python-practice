"""
Week 3 — File 3: Generators and iterators (yield, lazy evaluation)

A generator produces values one at a time instead of building the whole
list in memory. That's why they matter for data work: you can stream a
10 GB file line by line. Each function below must use `yield` (except
where it says otherwise). The checks call list(...) on your generator.
Run this file to check your work:
    python 03_generators_iterators.py

AI off. Write it yourself.
"""

from _check import run


def count_up_to(n):
    """Yield 1, 2, ..., n.
    Example: list(count_up_to(3)) -> [1, 2, 3]."""
    raise NotImplementedError


def evens_forever():
    """Yield 0, 2, 4, 6, ... forever (an infinite generator).
    The check only takes the first 5 values, so this won't hang — that's
    the point of laziness.
    Example: first five -> [0, 2, 4, 6, 8]."""
    raise NotImplementedError


def chunks(items, size):
    """Yield successive lists of length `size` from items; the last chunk
    may be shorter.
    Example: list(chunks([1, 2, 3, 4, 5], 2)) -> [[1, 2], [3, 4], [5]].
    (This exact pattern is how you batch API calls or DB writes.)"""
    raise NotImplementedError


def fib_gen():
    """Yield the Fibonacci sequence forever: 0, 1, 1, 2, 3, 5, ...
    Compare with last week's recursive version: this one is O(n), not O(2^n).
    Example: first seven -> [0, 1, 1, 2, 3, 5, 8]."""
    raise NotImplementedError


class Countdown:
    """An ITERATOR class (no yield allowed here): Countdown(3) produces 3, 2, 1.
    Implement __iter__ (return self) and __next__ (return the next value,
    or raise StopIteration when done). This is what a for-loop calls
    under the hood.
    Example: list(Countdown(3)) -> [3, 2, 1]."""

    def __init__(self, start):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError


def _take(gen, n):
    """Helper for the checks: pull n values from a (possibly infinite) iterator."""
    from itertools import islice
    return list(islice(gen, n))


if __name__ == "__main__":
    run([
        ("count_up_to", lambda: list(count_up_to(3)), [1, 2, 3]),
        ("evens_forever", lambda: _take(evens_forever(), 5), [0, 2, 4, 6, 8]),
        ("chunks", lambda: list(chunks([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]]),
        ("fib_gen", lambda: _take(fib_gen(), 7), [0, 1, 1, 2, 3, 5, 8]),
        ("Countdown", lambda: list(Countdown(3)), [3, 2, 1]),
    ])
