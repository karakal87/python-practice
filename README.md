# Python Practice — Refresher

A self-checking practice repo for rebuilding Python fluency ahead of technical interviews.

## The one rule that matters

**AI off. Clock on.**

At work, using AI to write code is smart and efficient — keep doing that. But interview
tests measure your *unaided* ability. This repo only works if you close the AI assistant,
close the tab with the answers, and write the code yourself. The friction you feel is the
muscle rebuilding. That is the entire point.

## How it works

Each practice file contains a set of function stubs. Each stub has a docstring telling you
what the function should do. Your job: fill in the function body. When you run the file, it
checks your work and tells you which problems pass.

```bash
python phase-a-python-fundamentals/week1/01_warmups.py
```

You'll see something like:

```
  ✓ add_one: passed
  ✗ fizzbuzz: got '3', want 'Fizz'
  ...
  4 / 6 passed
```

Keep going until every problem in a file passes. Then move to the next file.

## The routine

- **~15 min**: one new practice problem set (the files below), AI off.
- **~15 min**: one timed HackerRank or LeetCode *Easy* problem, AI off, clock running.

Thirty minutes a day, every day, beats three hours once a week. Consistency is the strategy.

## Getting stuck

Stuck for more than ~10 minutes on one problem? That's healthy — sit with it a bit longer
first. If you're truly blocked, the `solutions/` folder has worked answers. Read the
solution, understand it, close it, then re-solve from scratch. Don't copy.

## Progress

Tick these off as each file goes fully green:

- [ ] week1/01_warmups.py
- [ ] week1/02_data_structures.py
- [ ] week1/03_comprehensions.py
- [ ] week1/04_functions.py

## Pushing this to your own GitHub

From inside this folder:

```bash
# 1. Create an empty repo on github.com first (no README), then:
git remote add origin https://github.com/<your-username>/python-practice.git
git branch -M main
git push -u origin main
```
