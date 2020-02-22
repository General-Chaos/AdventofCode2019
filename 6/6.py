import os
import mod6

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')


with open(probleminput) as f:
    input_strings = [x.rstrip('\n') for x in f.readlines()]

orbits = mod6.process_input(input_strings)

checksum = mod6.calculate_orbit_checksum(orbits)

print(f"The answer to day 6 part 1 is: {checksum}")