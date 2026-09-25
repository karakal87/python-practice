"""
Week 1 — File 3: Comprehensions (list, dict, set)

Fill in each function body USING a comprehension where you can — that's the skill
being drilled here. Run this file to check your work:
    python 03_comprehensions.py

AI off. Write it yourself.
"""

from _check import run


def squares(n):
    """Return a list of squares of 0..n-1.
    Example: squares(4) -> [0, 1, 4, 9]."""
    # [review] BUG the test didn't catch: this hardcodes range(4), so it ignores n.
    #          squares(3) would wrongly return [0, 1, 4, 9]. Use range(n):
    #              return [num * num for num in range(n)]
    #          (Interviews love this: a hidden test case with a different input
    #           exposes exactly this kind of hardcoding.)
    return [num*num for num in range(4)]
    raise NotImplementedError


def evens(nums):
    """Return a list of only the even numbers in `nums`, order preserved.
    Example: evens([1, 2, 3, 4, 6]) -> [2, 4, 6]."""
    return [n for n in nums if n%2==0]
    raise NotImplementedError


def lengths(words):
    """Return a dict mapping each word to its length.
    Example: lengths(['a', 'bb']) -> {'a': 1, 'bb': 2}."""
    return {name: len(name) for name in words}
    raise NotImplementedError


def unique_first_letters(words):
    """Return a set of the first letters of each word.
    Example: unique_first_letters(['apple', 'avocado', 'banana']) -> {'a', 'b'}."""
    return {word[0] for word in words}
    raise NotImplementedError


def flatten(matrix):
    """Return a flat list of all values in a list of lists.
    Example: flatten([[1, 2], [3, 4]]) -> [1, 2, 3, 4]."""
    # The order matches nested loops: first visit each inner list in matrix,
    # then visit each value in that inner list and add it to the result.
    # Equivalent to:
    # result = []
    # for innerlist in matrix:
    #     for num in innerlist:
    #         result.append(num)
    return [num for innerlist in matrix for num in innerlist]
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("squares", lambda: squares(4), [0, 1, 4, 9]),
        ("evens", lambda: evens([1, 2, 3, 4, 6]), [2, 4, 6]),
        ("lengths", lambda: lengths(["a", "bb"]), {"a": 1, "bb": 2}),
        ("unique_first_letters",
         lambda: unique_first_letters(["apple", "avocado", "banana"]), {"a", "b"}),
        ("flatten", lambda: flatten([[1, 2], [3, 4]]), [1, 2, 3, 4]),
    ])
