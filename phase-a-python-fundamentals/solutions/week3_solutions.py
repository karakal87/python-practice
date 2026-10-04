"""
Week 3 — worked solutions.

Only open this when you've been genuinely stuck on a problem for 10+ minutes.
Read the solution, understand WHY it works, close the file, and re-solve from a
blank function. Don't copy-paste.
"""

from collections import Counter, defaultdict, deque
from itertools import islice


# ---- 01_collections ----

def top_k_words(sentence, k):
    return Counter(sentence.split()).most_common(k)

def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)

def last_n(items, n):
    window = deque(maxlen=n)
    for item in items:
        window.append(item)  # oldest item falls off automatically once full
    return list(window)

def rotate_right(items, k):
    d = deque(items)
    d.rotate(k)
    return list(d)

def furthest_from_origin(points):
    return max(points, key=lambda p: p.x ** 2 + p.y ** 2)  # no sqrt needed to compare


# ---- 02_sorting_and_builtins ----

def sort_by_length(words):
    return sorted(words, key=len)

def sort_people(people):
    return sorted(people, key=lambda p: (-p[1], p[0]))

def pair_up(names, scores):
    return dict(zip(names, scores))

def indices_of(items, target):
    return [i for i, item in enumerate(items) if item == target]

def all_positive(nums):
    return all(n > 0 for n in nums)  # all([]) is True: no counter-example exists

def any_long_word(words, n):
    return any(len(w) > n for w in words)


# ---- 03_generators_iterators ----

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

def evens_forever():
    n = 0
    while True:
        yield n
        n += 2

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# ---- 04_oop_deeper ----

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __lt__(self, other):
        return self.amount < other.amount

class Shape:
    def area(self):
        raise NotImplementedError

    def describe(self):
        return f"{type(self).__name__} with area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)
