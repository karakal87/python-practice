"""
Week 2 — File 4: Exceptions & basic OOP

Fill in each function/class body. Run this file to check your work:
    python 04_exceptions_oop.py

AI off. Write it yourself.
"""

from _check import run


def safe_divide(a, b):
    """Return a / b. If b is 0, catch the ZeroDivisionError and return None
    instead of letting it crash. Use try/except.
    Example: safe_divide(10, 2) -> 5.0, safe_divide(10, 0) -> None."""
    raise NotImplementedError


def parse_int_or_default(s, default=0):
    """Try to convert s to an int and return it. If s can't be converted
    (raises ValueError), return `default` instead.
    Example: parse_int_or_default('42') -> 42, parse_int_or_default('abc') -> 0."""
    raise NotImplementedError


class BankAccount:
    """A minimal bank account: holds a balance, supports deposit and
    withdraw, and refuses to go negative.

    Fill in __init__, deposit, withdraw, and get_balance below.
    withdraw should raise ValueError("insufficient funds") if the
    withdrawal would take the balance below zero — don't just clamp it.
    """

    def __init__(self, starting_balance=0):
        raise NotImplementedError

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError

    def get_balance(self):
        raise NotImplementedError


def _bank_account_case():
    """Exercises deposit, withdraw, and the insufficient-funds guard in one go."""
    acct = BankAccount(100)
    acct.deposit(50)
    acct.withdraw(30)
    try:
        acct.withdraw(1000)
        raised_correctly = False
    except ValueError:
        raised_correctly = True
    return (acct.get_balance(), raised_correctly)


if __name__ == "__main__":
    run([
        ("safe_divide", lambda: safe_divide(10, 2), 5.0),
        ("safe_divide by zero", lambda: safe_divide(10, 0), None),
        ("parse_int_or_default (ok)", lambda: parse_int_or_default("42"), 42),
        ("parse_int_or_default (bad)", lambda: parse_int_or_default("abc"), 0),
        ("BankAccount", _bank_account_case, (120, True)),
    ])
