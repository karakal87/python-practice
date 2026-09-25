"""
Week 2 — File 3: Searching & sorting (the mechanics, not just sorted())

Fill in each function body. Run this file to check your work:
    python 03_searching_sorting.py

AI off. Write it yourself.
"""

from _check import run


def linear_search(nums, target):
    """Return the index of the first occurrence of target in nums, or -1.
    Use a plain loop — this is O(n) and that's fine, it's the baseline.
    Example: linear_search([4, 2, 7, 2], 2) -> 1."""
    raise NotImplementedError


def bubble_sort(nums):
    """Return a NEW list with nums sorted ascending, implemented with bubble
    sort (repeatedly swap adjacent out-of-order pairs). Don't use sorted()
    or .sort() here — the point is to know how a sort actually works.
    Example: bubble_sort([5, 1, 4, 2, 3]) -> [1, 2, 3, 4, 5]."""
    raise NotImplementedError


def find_duplicates(nums):
    """Return a sorted list of values that appear more than once in nums.
    Example: find_duplicates([1, 2, 2, 3, 3, 3, 4]) -> [2, 3]."""
    raise NotImplementedError


def two_sum(nums, target):
    """Return a tuple of the two indices whose values add up to target, or
    None if no such pair exists. Assume at most one valid pair.
    Example: two_sum([2, 7, 11, 15], 9) -> (0, 1).
    This is one of the most-asked interview questions there is — aim for
    O(n) using a dict of value -> index, not the O(n^2) double loop."""
    raise NotImplementedError


def kth_largest(nums, k):
    """Return the kth largest value in nums (k=1 means the largest).
    Example: kth_largest([3, 1, 4, 1, 5, 9], 2) -> 5."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("linear_search", lambda: linear_search([4, 2, 7, 2], 2), 1),
        ("linear_search (missing)", lambda: linear_search([4, 2, 7], 9), -1),
        ("bubble_sort", lambda: bubble_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5]),
        ("find_duplicates", lambda: find_duplicates([1, 2, 2, 3, 3, 3, 4]), [2, 3]),
        ("two_sum", lambda: two_sum([2, 7, 11, 15], 9), (0, 1)),
        ("two_sum (none)", lambda: two_sum([1, 2, 3], 100), None),
        ("kth_largest", lambda: kth_largest([3, 1, 4, 1, 5, 9], 2), 5),
    ])
