"""
Week 1 — File 2: Data structures (lists, dicts, sets, tuples)

Fill in each function body. Run this file to check your work:
    python 02_data_structures.py

AI off. Write it yourself.
"""

from _check import run


def second_largest(nums: list):
    """Return the second largest DISTINCT value in the list `nums`.
    Example: second_largest([4, 1, 7, 7, 3]) -> 4."""
    # l = list(set(nums)) # 
    # l.sort() # sort is a list method, and inplace as it returns none, so used like this
    # return l[-2]
    l = sorted(set(nums))[-2] # sorted is a built in function on any iterable, inc strings, generates a new iterable
    return l
    raise NotImplementedError


def count_words(sentence):
    """Return a dict mapping each word to how many times it appears.
    Words are separated by single spaces, all lowercase.
    Example: count_words('a b a') -> {'a': 2, 'b': 1}."""
    raise NotImplementedError


def unique_sorted(nums):
    """Return a sorted list of the unique values in `nums`.
    Example: unique_sorted([3, 1, 2, 3, 1]) -> [1, 2, 3]."""
    raise NotImplementedError


def common_elements(a, b):
    """Return a sorted list of values that appear in BOTH lists a and b.
    Example: common_elements([1, 2, 3], [2, 3, 4]) -> [2, 3]."""
    raise NotImplementedError


def invert_dict(d):
    """Return a new dict with keys and values swapped.
    Assume values are unique and hashable.
    Example: invert_dict({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}."""
    raise NotImplementedError


def min_max(nums):
    """Return a tuple (minimum, maximum) of the list `nums`.
    Example: min_max([3, 1, 9, 4]) -> (1, 9)."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("second_largest", lambda: second_largest([4, 1, 7, 7, 3]), 4),
        ("count_words", lambda: count_words("a b a"), {"a": 2, "b": 1}),
        ("unique_sorted", lambda: unique_sorted([3, 1, 2, 3, 1]), [1, 2, 3]),
        ("common_elements", lambda: common_elements([1, 2, 3], [2, 3, 4]), [2, 3]),
        ("invert_dict", lambda: invert_dict({"a": 1, "b": 2}), {1: "a", 2: "b"}),
        ("min_max", lambda: min_max([3, 1, 9, 4]), (1, 9)),
    ])
