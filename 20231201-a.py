#!/usr/bin/python
import math
from aocd.models import Puzzle

def firstdigit(word):
    for i in word:
        #print(i)
        if i.isdigit():
            return (i)
    exit(1)

def lastdigit(word):
    i = 1
    while i <= len(word):
        #print(word[-i])
        if word[-i].isdigit():
            return (word[-i])
        else: i += 1

puzzle = Puzzle(year=2023, day=1)
result = 0
for word in puzzle.input_data.split('\n'):
    #print(firstdigit(word)+str(lastdigit(word)))
    result += int(firstdigit(word)+lastdigit(word))
print(result)


