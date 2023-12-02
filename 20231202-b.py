#!/usr/bin/python
from aocd.models import Puzzle


puzzle = Puzzle(year=2023, day=2)
result = 0
gamenum = 1
input = puzzle.input_data
#input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
for game in input.split('\n'):
    minvalue = {"red" : 0, "green": 0, "blue": 0}
    gamedata = game.split(':')[1].split(';')
    for gamesets in gamedata:
        gameset = [ s.strip() for s in gamesets.split(",")]
        for num, color in [s.split(' ') for s in gameset]:
            if int(num) > minvalue[color]:
                minvalue[color] = int(num)
    res = 1
    for value in minvalue.values():
        res *= value
    result += res
    gamenum += 1

print(result)


