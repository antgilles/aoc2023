#!/usr/bin/python
from aocd.models import Puzzle


puzzle = Puzzle(year=2023, day=2)
result = 0
gamenum = 1
maxvalue = {"red" : 12, "green": 13, "blue": 14}

for game in puzzle.input_data.split('\n'):
    possible = True
    gamedata = game.split(':')[1].split(';')
    for gamesets in gamedata:
        gameset = [ s.strip() for s in gamesets.split(",")]
        for num, color in [s.split(' ') for s in gameset]:
            if int(num) > maxvalue[color]:
                possible = False
    if possible:
        result += gamenum
    gamenum += 1

print(result)


