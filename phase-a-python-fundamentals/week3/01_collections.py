"""
Week 3 — File 1: The collections module (Counter, defaultdict, deque, namedtuple)

These four come up constantly in interview solutions because they turn
five lines of dict/list fiddling into one. Use them here — that's the drill.
Run this file to check your work:
    python 01_collections.py

AI off. Write it yourself.
"""

from collections import Counter, defaultdict, deque, namedtuple

from _check import run


def top_k_words(sentence, k):
    """Return the k most common words as a list of (word, count) tuples,
    most common first. Words are separated by spaces, all lowercase.
    Use Counter.
    Example: top_k_words('a b a c a b', 2) -> [('a', 3), ('b', 2)]."""
    return Counter(sentence.split()).most_common(k)
    raise NotImplementedError


def group_by_length(words):
    """Return a dict mapping word length -> list of words with that length,
    in the order they appear. Use defaultdict(list).
    Example: group_by_length(['hi', 'cat', 'to', 'dog'])
             -> {2: ['hi', 'to'], 3: ['cat', 'dog']}.
    (Return a plain dict at the end: dict(your_defaultdict).)"""
    # defaultdict adds a default (in this case a blank list) to a dictionary for a key, if the dictionary is accessed with that key,
    # and the key doesn't exist yet. so it creates key:[] pairs on the fly. 
    len_dict = defaultdict(list) # note here how we give it a default value of list (which is a type) to do this
    for word in words: len_dict[len(word)].append(word)
    return len_dict
    raise NotImplementedError


def last_n(items, n):
    """Return a list of the last n items seen, using a deque with maxlen=n.
    Feed every item into the deque one at a time — don't slice.
    Example: last_n([1, 2, 3, 4, 5], 3) -> [3, 4, 5]."""
    # its a 'double ended queue'.
    # here its keeps the last 'n' things seen as we iterate over items
    my_q = deque(maxlen=n)
    for item in items:
        my_q.append(item)
    return list(my_q)
    raise NotImplementedError


def rotate_right(items, k):
    """Return a new list with items rotated k places to the right, using
    deque.rotate().
    Example: rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]."""
    my_q = deque(items)
    my_q.rotate(k)
    return list(my_q)
    raise NotImplementedError


Point = namedtuple("Point", ["x", "y"])


def furthest_from_origin(points):
    """Given a list of Point namedtuples, return the one furthest from (0, 0).
    Access coordinates by name (p.x, p.y), not by index.
    Example: furthest_from_origin([Point(1, 1), Point(3, 4), Point(0, 2)])
             -> Point(x=3, y=4)."""
    raise NotImplementedError


if __name__ == "__main__":
    run([
        ("top_k_words", lambda: top_k_words("a b a c a b", 2), [("a", 3), ("b", 2)]),
        ("group_by_length",
         lambda: group_by_length(["hi", "cat", "to", "dog"]),
         {2: ["hi", "to"], 3: ["cat", "dog"]}),
        ("last_n", lambda: last_n([1, 2, 3, 4, 5], 3), [3, 4, 5]),
        ("rotate_right", lambda: rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]),
        ("furthest_from_origin",
         lambda: furthest_from_origin([Point(1, 1), Point(3, 4), Point(0, 2)]),
         Point(3, 4)),
    ])
