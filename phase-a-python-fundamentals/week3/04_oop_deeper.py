"""
Week 3 — File 4: OOP, one level deeper
(inheritance, super(), dunder methods, @property, @classmethod)

Last week's BankAccount was a class with methods. This week is about making
classes behave like built-in Python objects — printable, comparable,
sortable. Run this file to check your work:
    python 04_oop_deeper.py

AI off. Write it yourself.
"""

from _check import run


class Money:
    """An amount of money in a currency.

    - __init__(amount, currency)
    - __repr__ should return e.g. "Money(10, 'GBP')"
    - __eq__: equal if amount AND currency match
    - __add__: adding two Money objects of the same currency returns a new
      Money; different currencies raise ValueError("currency mismatch")
    - __lt__: compare by amount (assume same currency). Defining __lt__ is
      what lets sorted() work on a list of Money objects.
    """

    def __init__(self, amount, currency):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError


class Shape:
    """Base class. Subclasses must implement area(). describe() is shared:
    it returns "<ClassName> with area <area rounded to 2 dp>".
    Hint: type(self).__name__ gives the subclass's name."""

    def area(self):
        raise NotImplementedError

    def describe(self):
        raise NotImplementedError


class Rectangle(Shape):
    """Rectangle(width, height). area = width * height."""

    def __init__(self, width, height):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


class Square(Rectangle):
    """Square(side). Reuse Rectangle — call super().__init__(side, side)
    rather than re-implementing area()."""

    def __init__(self, side):
        raise NotImplementedError


class Temperature:
    """Stores a temperature in Celsius.

    - __init__(celsius)
    - `fahrenheit` is a read-only @property computed from celsius:
      F = C * 9/5 + 32
    - from_fahrenheit is a @classmethod alternative constructor:
      Temperature.from_fahrenheit(212).celsius -> 100.0
    """

    def __init__(self, celsius):
        raise NotImplementedError

    # add @property fahrenheit here

    # add @classmethod from_fahrenheit here


def _money_case():
    a = Money(10, "GBP")
    b = Money(5, "GBP")
    total = a + b
    try:
        a + Money(1, "USD")
        mismatch_raised = False
    except ValueError:
        mismatch_raised = True
    ordered = sorted([Money(30, "GBP"), a, b])
    return (repr(total), total == Money(15, "GBP"), mismatch_raised, [m.amount for m in ordered])


def _shapes_case():
    return [Rectangle(2, 3).describe(), Square(1.5).describe(), isinstance(Square(1), Rectangle)]


def _temperature_case():
    t = Temperature(100)
    return (t.fahrenheit, Temperature.from_fahrenheit(32).celsius)


if __name__ == "__main__":
    run([
        ("Money", _money_case, ("Money(15, 'GBP')", True, True, [5, 10, 30])),
        ("Shape / Rectangle / Square", _shapes_case,
         ["Rectangle with area 6.00", "Square with area 2.25", True]),
        ("Temperature", _temperature_case, (212.0, 0.0)),
    ])
