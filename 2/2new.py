from typing import List, Tuple
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from ShipComputer.shipcomputer import ShipComputer

def getnounverb(instructions: List[int],desiredvalue: int, maxsearch: int) -> Tuple[int, int]:
    computer = ShipComputer(instructions)
    for i in range(maxsearch):
        for j in range(maxsearch):
            if computer.runprogram(i, j)['itr'][0] == desiredvalue:
                return (i, j)
    raise ValueError(
        f"Desired value {desiredvalue} not found in search range {maxsearch}")

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')


with open(probleminput) as f:
    input_numbers = [int(x) for x in f.read().split(',')]

computer = ShipComputer(input_numbers)

answer1 = computer.runprogram(12,2)['itr'][0]

print(f"The answer to day 2 part 1 is: {answer1}")

answer2 = getnounverb(input_numbers, 19690720, 99)

print(f"The answer to day 2 part 2 is: {(100 * answer2[0]) + answer2[1]}")

