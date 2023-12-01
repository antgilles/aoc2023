#!/usr/bin/python
import math
from aocd.models import Puzzle

def preparestr(word):
    numbers = { "one": "1", "two": "2", "three": "3", "four": "4", "five":  "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
    newword = ""
    for i in  range(0,len(word)):
        if word[i].isdigit():
            newword += word[i]
        else:
            for key, value in numbers.items():
                if i + len(key) <= len(word):
                    if word[i:i + len(key)] == key:
                        newword += value
    return newword

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
    word = preparestr(word)
    result += int(firstdigit(word)+lastdigit(word))
print(result)


