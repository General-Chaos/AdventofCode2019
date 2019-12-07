import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from ShipComputer import ShipComputer

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    input_numbers = [int(x) for x in f.read().split(',')]

computer = ShipComputer(input_numbers)

answer1 = computer.runprogram(inputs=[1])

print(f"The answer to day 5 part 1 is: {answer1['output'][-1]}")

answer2 = computer.runprogram(inputs=[5])

print(f"The answer to day 5 part 2 is: {answer2['output'][0]}")
