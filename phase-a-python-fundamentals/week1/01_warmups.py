"""
Week 1 — File 1: Warmups (syntax, loops, conditionals)

Fill in each function body. Run this file to check your work:
    python 01_warmups.py

AI off. Write it yourself.
"""

from _check import run


def add_one(n):
    """Return n plus 1."""
    # TODO: replace this
    raise NotImplementedError


def is_even(n):
    """Return True if n is even, else False."""
    raise NotImplementedError


def sum_to(n):
    """Return the sum of all integers from 1 to n inclusive.
    Example: sum_to(5) -> 15. Use a loop, not the formula."""
    raise NotImplementedError


def count_vowels(word):
    """Return the number of vowels (a, e, i, o, u) in the lowercase string `word`.
    Example: count_vowels('banana') -> 3."""
    raise NotImplementedError


def fizzbuzz(n):
    """Return 'Fizz' if n divisible by 3, 'Buzz' if divisible by 5,
    'FizzBuzz' if divisible by both, otherwise the number as a string.
    Example: fizzbuzz(15) -> 'FizzBuzz', fizzbuzz(4) -> '4'."""
    raise NotImplementedError


def reverse_string(s):
    """Return the string s reversed. Example: reverse_string('abc') -> 'cba'.
    Try it with a loop before reaching for slicing."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("add_one", lambda: add_one(4), 5),
        ("is_even (even)", lambda: is_even(10), True),
        ("is_even (odd)", lambda: is_even(7), False),
        ("sum_to", lambda: sum_to(5), 15),
        ("count_vowels", lambda: count_vowels("banana"), 3),
        ("fizzbuzz 3", lambda: fizzbuzz(3), "Fizz"),
        ("fizzbuzz 5", lambda: fizzbuzz(5), "Buzz"),
        ("fizzbuzz 15", lambda: fizzbuzz(15), "FizzBuzz"),
        ("fizzbuzz 4", lambda: fizzbuzz(4), "4"),
        ("reverse_string", lambda: reverse_string("abc"), "cba"),
    ])
