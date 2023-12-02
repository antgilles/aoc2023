#!/usr/bin/python
from aocd.models import Puzzle

def firstdigit(word):
    for i in word:
        if i.isdigit():
            return (i)
    exit(1)

def lastdigit(word):
    i = 1
    while i <= len(word):
        if word[-i].isdigit():
            return (word[-i])
        else: i += 1

puzzle = Puzzle(year=2023, day=1)
result = 0
for word in puzzle.input_data.split('\n'):
    result += int(firstdigit(word)+lastdigit(word))
print(result)


