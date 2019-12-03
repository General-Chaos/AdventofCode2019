import os
import mod1

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')


with open(probleminput) as f:
    input_numbers = [int(x.rstrip('\n')) for x in f.readlines()]

answer1 = mod1.get_fuel_total(input_numbers)

print(f"The answer to day 1 part 1 is: {answer1}")

answer2 = mod1.get_fuel_total(input_numbers, True)

print(f"The answer to day 1 part 2 is: {answer2}")
