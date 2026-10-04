"""
Week 3 — File 2: Sorting with keys, lambdas, and the built-ins that save lines
(sorted(key=...), zip, enumerate, map, filter, any, all)

Run this file to check your work:
    python 02_sorting_and_builtins.py

AI off. Write it yourself.
"""

from _check import run


def sort_by_length(words):
    """Return words sorted by length, shortest first. Words of equal length
    keep their original order (sorted() is stable, so this is free).
    Example: sort_by_length(['ccc', 'a', 'bb', 'd']) -> ['a', 'd', 'bb', 'ccc']."""
    raise NotImplementedError


def sort_people(people):
    """people is a list of (name, age) tuples. Return them sorted by age
    DESCENDING, then by name ASCENDING to break ties — in one sorted() call.
    Hint: a key can return a tuple, and negating a number flips its order.
    Example: sort_people([('Bo', 30), ('Al', 25), ('Cy', 30)])
             -> [('Bo', 30), ('Cy', 30), ('Al', 25)]."""
    raise NotImplementedError


def pair_up(names, scores):
    """Return a dict mapping each name to its score, pairing the two lists
    position by position. Use zip.
    Example: pair_up(['a', 'b'], [1, 2]) -> {'a': 1, 'b': 2}."""
    raise NotImplementedError


def indices_of(items, target):
    """Return a list of every index where target appears. Use enumerate.
    Example: indices_of(['x', 'y', 'x'], 'x') -> [0, 2]."""
    raise NotImplementedError


def all_positive(nums):
    """Return True if every number is > 0. Use all() with a generator.
    Note what all([]) returns — worth knowing why.
    Example: all_positive([1, 2, 3]) -> True, all_positive([1, -2]) -> False."""
    raise NotImplementedError


def any_long_word(words, n):
    """Return True if any word has more than n characters. Use any().
    Example: any_long_word(['hi', 'there'], 4) -> True."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("sort_by_length",
         lambda: sort_by_length(["ccc", "a", "bb", "d"]), ["a", "d", "bb", "ccc"]),
        ("sort_people",
         lambda: sort_people([("Bo", 30), ("Al", 25), ("Cy", 30)]),
         [("Bo", 30), ("Cy", 30), ("Al", 25)]),
        ("pair_up", lambda: pair_up(["a", "b"], [1, 2]), {"a": 1, "b": 2}),
        ("indices_of", lambda: indices_of(["x", "y", "x"], "x"), [0, 2]),
        ("all_positive (true)", lambda: all_positive([1, 2, 3]), True),
        ("all_positive (false)", lambda: all_positive([1, -2]), False),
        ("all_positive (empty)", lambda: all_positive([]), True),
        ("any_long_word", lambda: any_long_word(["hi", "there"], 4), True),
    ])
