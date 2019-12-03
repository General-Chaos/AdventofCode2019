import os
import mod2

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')


with open(probleminput) as f:
    input_numbers = [int(x) for x in f.read().split(',')]

computer = mod2.ShipComputer(input_numbers)

answer1 = computer.runprogram(12,2)[0]

print(f"The answer to day 2 part 1 is: {answer1}")

answer2 = computer.getnounverb(19690720, 99)

print(f"The answer to day 2 part 2 is: {(100 * answer2[0]) + answer2[1]}")
