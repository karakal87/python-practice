"""
Week 2 — File 1: Strings (methods, slicing, formatting)

Fill in each function body. Run this file to check your work:
    python 01_strings.py

AI off. Write it yourself.
"""

from _check import run


def is_palindrome(s):
    """Return True if s reads the same forwards and backwards, else False.
    Assume s is already lowercase with no spaces or punctuation.
    Example: is_palindrome('racecar') -> True, is_palindrome('hello') -> False."""
    raise NotImplementedError


def title_case(sentence):
    """Return the sentence with the first letter of every word capitalised.
    Words are separated by single spaces.
    Example: title_case('the cat sat') -> 'The Cat Sat'.
    (You may use str.title(), but also think about why it can misfire on
    words like "o'clock" — worth being able to explain either way.)"""
    raise NotImplementedError


def is_anagram(a, b):
    """Return True if strings a and b are anagrams of each other (same letters,
    same counts, order doesn't matter). Assume lowercase, no spaces.
    Example: is_anagram('listen', 'silent') -> True."""
    raise NotImplementedError


def caesar_shift(s, shift):
    """Return s with every lowercase letter shifted forward by `shift` positions
    in the alphabet, wrapping around from z to a. Non-letters pass through unchanged.
    Example: caesar_shift('abc', 1) -> 'bcd'. caesar_shift('xyz', 2) -> 'zab'.
    Hint: ord() and chr() convert between a character and its code point."""
    raise NotImplementedError


def most_common_char(s):
    """Return the single most frequently occurring character in s.
    Assume no ties in the test cases below.
    Example: most_common_char('aabbbc') -> 'b'."""
    raise NotImplementedError


def compress(s):
    """Run-length encode a string: each run of repeated characters becomes
    the character followed by its count.
    Example: compress('aaabbc') -> 'a3b2c1'. compress('') -> ''."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("is_palindrome (true)", lambda: is_palindrome("racecar"), True),
        ("is_palindrome (false)", lambda: is_palindrome("hello"), False),
        ("title_case", lambda: title_case("the cat sat"), "The Cat Sat"),
        ("is_anagram (true)", lambda: is_anagram("listen", "silent"), True),
        ("is_anagram (false)", lambda: is_anagram("listen", "silents"), False),
        ("caesar_shift", lambda: caesar_shift("abc", 1), "bcd"),
        ("caesar_shift wrap", lambda: caesar_shift("xyz", 2), "zab"),
        ("most_common_char", lambda: most_common_char("aabbbc"), "b"),
        ("compress", lambda: compress("aaabbc"), "a3b2c1"),
        ("compress empty", lambda: compress(""), ""),
    ])
