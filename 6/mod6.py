import re
from typing import List, Dict


def process_input(input_strings: List[str]) -> Dict[str, List[str]]:
    results = dict()
    for i in input_strings:
        m = re.match(r"(\w+)\)(\w+)", i)
        results.setdefault(m.group(1), list())
        results.setdefault(m.group(2), list())
        results[m.group(1)].append(m.group(2))
    return results

def get_child_orbits(input_orbits: Dict[str, List[str]], target: str) -> List[str]:
    for i in input_orbits[target]:
        yield i
        yield from get_child_orbits(input_orbits, i)


def calculate_orbit_checksum(input_orbits: Dict[str, List[str]]) -> int:
    checksum = 0
    for k in input_orbits.keys():
        checksum += len(list(get_child_orbits(input_orbits, k)))
    return checksum


if __name__ == "__main__":
    test_input = (
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L"
    )
    orbits = process_input(test_input)
    checksum = calculate_orbit_checksum(orbits)
    print(checksum)