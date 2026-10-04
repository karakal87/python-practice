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
    return s == s[::-1]
    raise NotImplementedError


def title_case(sentence):
    """Return the sentence with the first letter of every word capitalised.
    Words are separated by single spaces.
    Example: title_case('the cat sat') -> 'The Cat Sat'.
    (You may use str.title(), but also think about why it can misfire on
    words like "o'clock" — worth being able to explain either way.)"""
    # words = sentence.split(" ")
    # capitalized_list_of_words = [word.capitalize() for word in words]
    # return " ".join(capitalized_list_of_words)
    return " ".join([word.capitalize() for word in sentence.split(" ")])
    raise NotImplementedError


def is_anagram(a, b):
    """Return True if strings a and b are anagrams of each other (same letters,
    same counts, order doesn't matter). Assume lowercase, no spaces.
    Example: is_anagram('listen', 'silent') -> True."""
    from collections import Counter # module, then something inside the module
    # this is wrong, as could have aabcc abbca (len(a)==len(b)) and (set(a) == set(b))
    # sorted(a) == sorted(b)
    return Counter(a) == Counter(b)
    raise NotImplementedError


def caesar_shift(s, shift):
    """Return s with every lowercase letter shifted forward by `shift` positions
    in the alphabet, wrapping around from z to a. Non-letters pass through unchanged.
    Example: caesar_shift('abc', 1) -> 'bcd'. caesar_shift('xyz', 2) -> 'zab'.
    Hint: ord() and chr() convert between a character and its code point."""
    return "".join(
        chr((ord(char) - ord("a") + shift) %26 + ord("a"))
        if "a" <= char <= "z" 
        else char # for non lower case alphas       
        for char in s
        )
    raise NotImplementedError


def most_common_char(s):
    """Return the single most frequently occurring character in s.
    Assume no ties in the test cases below.
    Example: most_common_char('aabbbc') -> 'b'."""
    from collections import Counter
    return Counter(s).most_common(1)[0][0] # give me the 1 most common item (comes back as a list), take the 0 item, and the 0 element of the tuple
    raise NotImplementedError


def compress(s):
    """Run-length encode a string: each run of repeated characters becomes
    the character followed by its count.
    Example: compress('aaabbc') -> 'a3b2c1'. compress('') -> ''."""
    # Not a solution as groups letters together
    # from collections import Counter
    # string = ''
    # for name, value in Counter(s).items():
    #     string+= name+str(value)
    # return string
    current = ''
    count = 0
    char_list = []
    if not s:
        return ''
    else:
        current = s[0]
    for char in s:
        new = char
        if new == current:
            count+=1
        else:
            char_list.append(current+str(count))
            count = 1
            current = new
    char_list.append(current+str(count))
    return ''.join(char_list)
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
