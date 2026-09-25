"""
Week 2 — File 2: Recursion

Fill in each function body USING recursion (a function calling itself) —
that's the skill being drilled here, even where a loop would be simpler.
Run this file to check your work:
    python 02_recursion.py

AI off. Write it yourself.
"""

from _check import run


def factorial(n):
    """Return n! (n factorial) recursively. factorial(0) -> 1.
    Example: factorial(5) -> 120.
    Think about the base case first: what's the smallest n you can answer
    without recursing?"""
    raise NotImplementedError


def fibonacci(n):
    """Return the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1), recursively.
    Example: fibonacci(6) -> 8."""
    raise NotImplementedError


def sum_digits(n):
    """Return the sum of the digits of non-negative integer n, recursively.
    Example: sum_digits(1234) -> 10.
    Hint: n % 10 gives the last digit, n // 10 drops it."""
    raise NotImplementedError


def reverse_list(items):
    """Return a new list with items in reverse order, recursively (no slicing,
    no built-in reverse — recurse on the rest of the list).
    Example: reverse_list([1, 2, 3]) -> [3, 2, 1]."""
    raise NotImplementedError


def binary_search(sorted_nums, target):
    """Return the index of target in sorted_nums (ascending order), or -1 if
    not present, using recursive binary search.
    Example: binary_search([1, 3, 5, 7, 9], 7) -> 3.
    binary_search([1, 3, 5, 7, 9], 4) -> -1.
    This is the classic interview warm-up: know it cold."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("factorial 0", lambda: factorial(0), 1),
        ("factorial 5", lambda: factorial(5), 120),
        ("fibonacci", lambda: fibonacci(6), 8),
        ("sum_digits", lambda: sum_digits(1234), 10),
        ("reverse_list", lambda: reverse_list([1, 2, 3]), [3, 2, 1]),
        ("binary_search (found)", lambda: binary_search([1, 3, 5, 7, 9], 7), 3),
        ("binary_search (missing)", lambda: binary_search([1, 3, 5, 7, 9], 4), -1),
    ])
