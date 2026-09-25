"""
Week 2 — worked solutions.

Only open this when you've been genuinely stuck on a problem for 10+ minutes.
Read the solution, understand WHY it works, close the file, and re-solve from a
blank function. Don't copy-paste.
"""

# ---- 01_strings ----

def is_palindrome(s):
    return s == s[::-1]

def title_case(sentence):
    return " ".join(word[0].upper() + word[1:] for word in sentence.split(" "))

def is_anagram(a, b):
    return sorted(a) == sorted(b)

def caesar_shift(s, shift):
    out = []
    for ch in s:
        if ch.isalpha():
            base = ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)

def most_common_char(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return max(counts, key=counts.get)

def compress(s):
    if not s:
        return ""
    out = []
    current = s[0]
    count = 1
    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            out.append(f"{current}{count}")
            current = ch
            count = 1
    out.append(f"{current}{count}")
    return "".join(out)


# ---- 02_recursion ----

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def reverse_list(items):
    if not items:
        return []
    return reverse_list(items[1:]) + [items[0]]

def binary_search(sorted_nums, target, lo=0, hi=None):
    if hi is None:
        hi = len(sorted_nums) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if sorted_nums[mid] == target:
        return mid
    if sorted_nums[mid] < target:
        return binary_search(sorted_nums, target, mid + 1, hi)
    return binary_search(sorted_nums, target, lo, mid - 1)


# ---- 03_searching_sorting ----

def linear_search(nums, target):
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1

def bubble_sort(nums):
    result = list(nums)
    n = len(result)
    for i in range(n):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def find_duplicates(nums):
    seen = set()
    dupes = set()
    for n in nums:
        if n in seen:
            dupes.add(n)
        seen.add(n)
    return sorted(dupes)

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return (seen[complement], i)
        seen[n] = i
    return None

def kth_largest(nums, k):
    return sorted(nums, reverse=True)[k - 1]


# ---- 04_exceptions_oop ----

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def parse_int_or_default(s, default=0):
    try:
        return int(s)
    except ValueError:
        return default

class BankAccount:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance
