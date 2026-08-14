"""
Week 1 — worked solutions.

Only open this when you've been genuinely stuck on a problem for 10+ minutes.
Read the solution, understand WHY it works, close the file, and re-solve from a
blank function. Don't copy-paste. There is usually more than one good answer —
yours passing the checks is what matters, not matching these exactly.
"""

# ---- 01_warmups ----

def add_one(n):
    return n + 1

def is_even(n):
    return n % 2 == 0

def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def count_vowels(word):
    return sum(1 for ch in word if ch in "aeiou")

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def reverse_string(s):
    out = ""
    for ch in s:
        out = ch + out
    return out
    # or simply: return s[::-1]


# ---- 02_data_structures ----

def second_largest(nums):
    distinct = sorted(set(nums))
    return distinct[-2]

def count_words(sentence):
    counts = {}
    for word in sentence.split(" "):
        counts[word] = counts.get(word, 0) + 1
    return counts

def unique_sorted(nums):
    return sorted(set(nums))

def common_elements(a, b):
    return sorted(set(a) & set(b))

def invert_dict(d):
    return {value: key for key, value in d.items()}

def min_max(nums):
    return (min(nums), max(nums))


# ---- 03_comprehensions ----

def squares(n):
    return [i * i for i in range(n)]

def evens(nums):
    return [x for x in nums if x % 2 == 0]

def lengths(words):
    return {w: len(w) for w in words}

def unique_first_letters(words):
    return {w[0] for w in words}

def flatten(matrix):
    return [x for row in matrix for x in row]


# ---- 04_functions ----

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def total(*nums):
    return sum(nums)

def apply_twice(func, x):
    return func(func(x))

def running_totals(nums):
    out = []
    acc = 0
    for n in nums:
        acc += n
        out.append(acc)
    return out

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
