import os
import mod3

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

grid = mod3.WireGrid()

with open(probleminput) as f:
    for i in f.readlines():
        grid.addwireinstructions(i.split(','))

answer1 = mod3.getminimummanhatten(grid.getintersections())

print(f"The answer to day 3 part 1 is: {answer1}")

answer2 = mod3.getminimumsteps(grid.getintersections())

print(f"The answer to day 3 part 2 is: {answer2}")
